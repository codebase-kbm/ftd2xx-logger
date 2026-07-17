from pathlib import Path


def render(module, output: Path):

    with open(output / "proxy.cpp", "w", encoding="utf-8") as f:

        f.write('#include "loader.h"\n\n')

        for fn in module.functions:
            render_function(f, fn)

def render_function(f, fn):

    args = ", ".join(
        f"{a.type} {a.name}"
        for a in fn.arguments
    )

    f.write(
        f"{fn.return_type} {fn.calling} {fn.name}({args})\n"
    )

    f.write("{\n")

    call = ", ".join(a.name for a in fn.arguments)

    if fn.return_type == "void":
        f.write(f"    p{fn.name}({call});\n")
    else:
        f.write(f"    return p{fn.name}({call});\n")

    f.write("}\n\n")