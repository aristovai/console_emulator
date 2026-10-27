import argparse
from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class Config:
    vfs_path: Path | None
    script_path: Path | None

def parse_arguments(argv: list[str] | None = None) -> Config:
    """Прочитать параметры командной строки."""
    parser = argparse.ArgumentParser(
        description="VFS Shell Emulator"
    )

    parser.add_argument(
        "--vfs",
        type=Path,
        default=None,
        help="Path to the virtual filesystem"
    )

    parser.add_argument(
        "--script",
        type=Path,
        default=None,
        help="Path to the startup script"
    )

    args = parser.parse_args(argv)

    return Config(
        vfs_path=args.vfs,
        script_path=args.script
    )
