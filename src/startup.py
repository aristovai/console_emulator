from pathlib import Path
def load_script(path: Path) -> list[str]:
    """Прочитать команды, пропустив комментарии."""
    commands = []

    with path.open("r", encoding="utf-8") as file:
        for line in file:
            command = line.strip()

            if not command:
                continue

            if command.startswith("#"):
                continue

            commands.append(command)

    return commands
