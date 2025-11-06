"""
Combine all README.md files from subfolders into a single root README.md.

- Walks the repository from the script's directory (assumed project root).
- Finds README.md in each subdirectory (case-sensitive).
- For each README.md, writes a heading with its folder path, then the file content.
- Inserts a blank line between each imported README.
- Writes/overwrites ./README.md in the project root.

You can tweak EXCLUDED_DIRS if needed.
"""

from __future__ import annotations
import os
from pathlib import Path

# Folders to skip entirely (add more if needed)
EXCLUDED_DIRS = {
    ".git",
    ".hg",
    ".svn",
    ".idea",
    ".vscode",
    "__pycache__",
    "node_modules",
    ".venv",
    "venv",
    ".mypy_cache",
    ".pytest_cache",
}


def is_excluded_dir(dirname: str) -> bool:
    name = os.path.basename(dirname)
    return name in EXCLUDED_DIRS or name.startswith(".git")


def main() -> None:
    project_root = Path(__file__).resolve().parent
    output_file = project_root / "README.md"

    # Collect all README.md paths except the root output itself
    readmes: list[Path] = []
    for root, dirs, files in os.walk(project_root):
        # prune excluded dirs
        dirs[:] = [d for d in dirs if not is_excluded_dir(os.path.join(root, d))]
        root_path = Path(root)

        # skip the project root README (we're generating it)
        if root_path == project_root:
            # but still allow scanning files at root in case you want to combine other readmes by name
            pass

        if "README.md" in files:
            candidate = root_path / "README.md"
            # Don't include the output file (in case it already exists)
            if candidate.resolve() == output_file.resolve():
                continue
            readmes.append(candidate)

    # Sort paths deterministically (by relative path)
    readmes.sort(key=lambda p: str(p.relative_to(project_root)).lower())

    # Build the combined README
    lines: list[str] = []
    lines.append("# Combined READMEs\n")
    for i, readme_path in enumerate(readmes, start=1):
        rel_dir = readme_path.parent.relative_to(project_root)
        # Heading for this imported README
        heading_text = f"## {rel_dir if str(rel_dir) != '.' else 'root'}"
        lines.append(heading_text + "\n")

        try:
            content = readme_path.read_text(encoding="utf-8").rstrip()
        except UnicodeDecodeError:
            # Fallback if encoding is odd
            content = readme_path.read_text(errors="replace")

        lines.append(content)
        # blank line between readmes
        lines.append("")  # ensures exactly one blank line gap

    # Write/overwrite root README.md
    output_file.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {output_file} with {len(readmes)} imported README(s).")


if __name__ == "__main__":
    main()
