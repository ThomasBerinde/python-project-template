#!/usr/bin/env python3
import re
from pathlib import Path

# Paths
script_path = Path(__file__).resolve()
root = script_path.parent
project_name = re.sub("-", "_", root.name)
pyproject = root / "pyproject.toml"
src_old = root / "src" / "project_name"
src_new = root / "src" / project_name

print(f"🔧 Setting up project: {project_name}")

# 1️. Replace in pyproject.toml
if pyproject.exists():
    text = pyproject.read_text(encoding="utf-8")
    if "project_name" in text:
        pyproject.write_text(text.replace("project_name", project_name), encoding="utf-8")
        print("✅ Updated pyproject.toml")

# 2️. Rename src/project_name → src/<project_name>
if src_old.exists():
    src_old.rename(src_new)
    print(f"📁 Renamed folder: src/project_name → src/{project_name}")

# 3️. Delete this script
try:
    script_path.unlink()
    print(f"🧹 Removed setup script: {script_path.name}")
except Exception as e:
    print(f"⚠️ Could not delete {script_path.name}: {e}")

print(f"\n✨ Done! Project initialized as '{project_name}'.")
