import re

from model import Module, Function

EXPORT_RE = re.compile(
    r"^\s*(\d+)\s+([0-9A-F]+)\s+([0-9A-F]+)\s+([A-Za-z0-9_]+)$"
)


def parse_dumpbin(text: str):

    module = Module(name="FTD2XX")

    lines = text.splitlines()

    for line in lines:

            # DLL Name
            if "Section contains the following exports for" in line:
                module.name = line.split("for")[-1].strip()
                continue

            m = EXPORT_RE.match(line)

            if not m:
                continue

            ordinal = int(m.group(1))
            hint = int(m.group(2), 16)
            rva = int(m.group(3), 16)
            name = m.group(4)

            module.functions.append(
                Function(
                    name=name,
                    ordinal=ordinal,
                    hint=hint,
                    rva=rva,
                )
            )

    return module