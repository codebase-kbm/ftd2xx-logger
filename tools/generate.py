from pathlib import Path
from dumpbin import dump_exports
from dumpbin_parser import parse_dumpbin
from header_parser import parse_header
from validator import validate

from renderer import def_file
from renderer import loader_h
from renderer import loader_cpp


def main():

    root = Path(__file__).resolve().parent.parent

    definition = root / "definitions" / "ftd2xx"

    dll = next(definition.glob("*.dll"))
    header = next(definition.glob("*.h"))

    output = root / "generated" / "ftd2xx"

    # ----------------------------------------------------------
    # Parse
    # ----------------------------------------------------------

    module = parse_dumpbin(
        dump_exports(dll)
    )

    parse_header(header, module)
    exports = {f.name for f in module.functions}

    print("\nFehlende Signaturen:")

    for fn in module.functions:
        if fn.return_type is None:
            print("  ", fn.name)

    # ----------------------------------------------------------
    # Validate
    # ----------------------------------------------------------

    validate(module)

    # ----------------------------------------------------------
    # Render
    # ----------------------------------------------------------

    def_file.render(module, output)
    loader_h.render(module, output)
    loader_cpp.render(module, output)
    
    print(f"Generated {len(module.functions)} functions.")



if __name__ == "__main__":
    main()