from pathlib import Path
import subprocess

DUMPBIN = Path(
    r"C:\Program Files (x86)\Microsoft Visual Studio\18\BuildTools\VC\Tools\MSVC\14.51.36231\bin\Hostx64\x86\dumpbin.exe"
)


def dump_exports(dll: Path) -> str:
    result = subprocess.run(
        [
            str(DUMPBIN),
            "/exports",
            str(dll),
        ],
        capture_output=True,
        text=True,
        check=True,
    )

    return result.stdout