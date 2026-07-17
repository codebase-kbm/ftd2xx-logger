from pathlib import Path


def render(module, output: Path):

    with open(output / "loader.cpp", "w", encoding="utf-8") as f:

        f.write('#include "loader.h"\n\n')

        f.write("HMODULE g_OriginalDll = nullptr;\n\n")

        for fn in module.functions:
            f.write(f"PFN_{fn.name} p{fn.name} = nullptr;\n")
        f.write("\n")
        f.write("bool LoadOriginalDll()\n")
        f.write("{\n")
        f.write('    g_OriginalDll = LoadLibraryW(L"ftd2xx1.dll");\n\n')
        f.write("    if (!g_OriginalDll)\n")
        f.write("        return false;\n\n")
        f.write("    return true;\n")
        
        for fn in module.functions:
            f.write(
                f'    p{fn.name} = (PFN_{fn.name})GetProcAddress(g_OriginalDll, "{fn.name}");\n'
            )

        f.write("\n")
        f.write("    return true;\n")
        f.write("}\n")