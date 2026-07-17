from pathlib import Path
import re

from model import Module, Argument


def parse_header(filename: str | Path, module: Module) -> Module:
    """
    Liest ftd2xx.h ein und ergänzt die Funktionsinformationen
    im bereits durch dumpbin erzeugten Modul.
    """

    filename = Path(filename)

    print(f"[HEADER] {filename.resolve()}")

    if not filename.exists():
        raise FileNotFoundError(filename)

    text = filename.read_text(encoding="utf-8", errors="ignore")

    print(f"[HEADER] {len(text)} Bytes")

    #
    # Alle Deklarationen finden
    #
    pattern = re.compile(
        r"""
        FTD2XX_API\s*
        (?P<return>\w+)\s+
        (?P<calling>\w+)\s+
        (?P<name>FT_\w+)\s*
        \(
            (?P<args>.*?)
        \)
        \s*;
        """,
        re.MULTILINE | re.DOTALL | re.VERBOSE,
    )

    matches = list(pattern.finditer(text))

    print(f"[HEADER] {len(matches)} Funktionen gefunden")

    lookup = {f.name: f for f in module.functions}

    for match in matches:

        name = match.group("name")

        if name not in lookup:
            print(f"Nicht im Export gefunden: {name}")
            continue

        fn = lookup[name]

        fn.return_type = match.group("return")
        fn.calling = match.group("calling")

        args = match.group("args").strip()

        if args in ("", "void"):
            continue

        for arg in args.split(","):

            arg = arg.strip()

            if not arg:
                continue

            parts = arg.split()

            if len(parts) == 1:
                fn.arguments.append(
                    Argument(
                        type=parts[0],
                        name=""
                    )
                )
                continue

            arg_name = parts[-1]
            arg_type = " ".join(parts[:-1])

            while arg_name.startswith("*"):
                arg_type += " *"
                arg_name = arg_name[1:]

            fn.arguments.append(
                Argument(
                    type=arg_type,
                    name=arg_name
                )
            )

    return module