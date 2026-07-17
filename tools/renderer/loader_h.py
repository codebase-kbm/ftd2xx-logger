from pathlib import Path

from model import Module
from renderer.common import cpp_typedef, cpp_extern


def render(module: Module, outdir: Path) -> None:

    outdir.mkdir(parents=True, exist_ok=True)

    filename = outdir / "loader.h"

    lines = []

    lines.append("#pragma once")
    lines.append("")
    lines.append("#include <windows.h>")
    lines.append('#include "ftd2xx.h"')
    lines.append("")

    lines.append("extern HMODULE g_OriginalDll;")
    lines.append("")

    for fn in module.functions:
        lines.append(cpp_typedef(fn))

    lines.append("")

    for fn in module.functions:
        lines.append(cpp_extern(fn))

    lines.append("")
    lines.append("bool LoadOriginalDLL();")
    lines.append("void UnloadOriginalDLL();")

    filename.write_text(
        "\n".join(lines) + "\n",
        encoding="utf-8",
    )