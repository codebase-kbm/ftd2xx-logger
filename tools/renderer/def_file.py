from pathlib import Path

from model import Module


def render(module: Module, outdir: Path) -> None:
    """
    Generate a module definition (*.def) file.
    """

    outdir.mkdir(parents=True, exist_ok=True)

    filename = outdir / f"{module.name.lower()}.def"

    lines = []

    lines.append(f"LIBRARY {module.name}")
    lines.append("")
    lines.append("EXPORTS")
    lines.append("")

    for fn in sorted(module.functions, key=lambda f: f.ordinal):
        lines.append(f"{fn.name:<35} @{fn.ordinal}")

    filename.write_text(
        "\n".join(lines) + "\n",
        encoding="utf-8",
    )