from pathlib import Path


def render(module, output: Path):

    with open(output / "loader.cpp", "w", encoding="utf-8") as f:

        f.write('#include "loader.h"\n\n')

        f.write("HMODULE g_OriginalDll = nullptr;\n\n")

        for fn in module.functions:
            f.write(f"PFN_{fn.name} p{fn.name} = nullptr;\n")