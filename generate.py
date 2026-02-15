#!/usr/bin/env python3
import json
import re
from pathlib import Path

PACKAGES_FILE = Path("packages.json")
PKGBUILD_STABLE = Path("PKGBUILD")
PKGBUILD_GIT = Path("PKGBUILD-git")

def load_packages():
    with open(PACKAGES_FILE, "r") as f:
        return json.load(f)

def generate_dependency_string(packages, is_git=False):
    deps = []
    for item in packages:
        if isinstance(item, list):
            if is_git:
                deps.append(create_quoted_string(item[1]))
            else:
                deps.append(create_quoted_string(item[0]))
        else:
            deps.append(create_quoted_string(item))
    return f"depends=({' '.join(deps)})"

def create_quoted_string(s):
    return f"'{s}'"

def update_pkgbuild(file_path, new_depends_line):
    if not file_path.exists():
        print(f"Warning: {file_path} not found.")
        return

    with open(file_path, "r") as f:
        content = f.read()
    
    pattern = r"depends=\(.*\)"
    if re.search(pattern, content):
        new_content = re.sub(pattern, new_depends_line, content)
        
        with open(file_path, "w") as f:
            f.write(new_content)
        print(f"Updated {file_path}")
    else:
        print(f"Error: Could not find 'depends=' line in {file_path}")

def main():
    if not PACKAGES_FILE.exists():
        print(f"Error: {PACKAGES_FILE} not found.")
        return

    packages = load_packages()

    depends_stable = generate_dependency_string(packages, is_git=False)
    depends_git = generate_dependency_string(packages, is_git=True)

    print(f"Stable dependencies: {depends_stable}")
    print(f"Git dependencies:    {depends_git}")

    update_pkgbuild(PKGBUILD_STABLE, depends_stable)
    update_pkgbuild(PKGBUILD_GIT, depends_git)

if __name__ == "__main__":
    main()
