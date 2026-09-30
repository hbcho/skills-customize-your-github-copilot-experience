from pathlib import Path
import json
import shutil


def list_files(source_folder: Path) -> list[Path]:
    """Return files directly inside source_folder."""
    # TODO: Validate the folder and return only direct child files.
    return []


def organize_files(source_folder: Path, destination_folder: Path) -> list[dict[str, str]]:
    """Move source files into extension-based folders and return a move log."""
    move_log: list[dict[str, str]] = []

    for file_path in list_files(source_folder):
        # TODO: Choose an extension category, create its folder, and move the file.
        # Use "other" for files without an extension.
        pass

    return move_log


def save_log(log_path: Path, move_log: list[dict[str, str]]) -> None:
    """Save the move results as readable JSON."""
    log_data = {
        "total_moved": len(move_log),
        "files": move_log,
    }
    # TODO: Write log_data to log_path with UTF-8 encoding.
    pass


if __name__ == "__main__":
    source = Path("sample_files")
    destination = Path("organized")
    log_file = Path("organization-log.json")

    moves = organize_files(source, destination)
    save_log(log_file, moves)
    print(f"Moved {len(moves)} file(s). Log saved to {log_file}.")
