import argparse
import shutil
from pathlib import Path

CATEGORIES = {
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"},
    "Documents": {".pdf", ".doc", ".docx", ".txt", ".xlsx", ".pptx", ".csv", ".md"},
    "Videos": {".mp4", ".mkv", ".mov", ".avi", ".webm"},
    "Audio": {".mp3", ".wav", ".flac", ".aac", ".ogg"},
    "Archives": {".zip", ".rar", ".7z", ".tar", ".gz"},
    "Code": {".py", ".js", ".html", ".css", ".java", ".cpp", ".c", ".json"},
}


def categorize(extension):
    for category, extensions in CATEGORIES.items():
        if extension.lower() in extensions:
            return category
    return "Others"


def organize(folder, dry_run):
    folder = Path(folder).expanduser().resolve()
    if not folder.is_dir():
        print(f"'{folder}' is not a valid directory.")
        return

    moved = 0
    for item in folder.iterdir():
        if item.is_dir():
            continue  # don't touch existing subfolders

        category = categorize(item.suffix)
        destination_folder = folder / category
        destination = destination_folder / item.name

        if dry_run:
            print(f"[DRY RUN] Would move: {item.name}  ->  {category}/")
        else:
            destination_folder.mkdir(exist_ok=True)
            shutil.move(str(item), str(destination))
            print(f"Moved: {item.name}  ->  {category}/")
        moved += 1

    if moved == 0:
        print("No files to organize. The folder is already tidy!")
    else:
        action = "would be moved" if dry_run else "moved"
        print(f"\n{moved} file(s) {action}.")


def build_parser():
    parser = argparse.ArgumentParser(description="Organize a folder's files by type.")
    parser.add_argument("folder", help="Path to the folder to organize")
    parser.add_argument(
        "--dry-run", action="store_true", help="Preview changes without moving files"
    )
    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()
    organize(args.folder, args.dry_run)


if __name__ == "__main__":
    main()