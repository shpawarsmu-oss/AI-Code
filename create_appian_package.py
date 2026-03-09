#!/usr/bin/env python3
"""
create_appian_package.py

Creates a valid Appian-importable ZIP file (TestCodeSandbox_Appian.zip) from
the 'Test Code  Sandbox' folder in this repository.

The ZIP is built so that META-INF/ is at the ROOT of the archive, which is
required by Appian (error APNX-1-4154-000 occurs when it is nested).

Usage:
    python create_appian_package.py
"""

import os
import zipfile

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SOURCE_DIR = os.path.join(SCRIPT_DIR, "Test Code  Sandbox")
EXTRA_FILE = os.path.join(SCRIPT_DIR, "isNotNullOrEmptyOrZero.expression")
OUTPUT_ZIP = os.path.join(SCRIPT_DIR, "TestCodeSandbox_Appian.zip")


def build_zip():
    if not os.path.isdir(SOURCE_DIR):
        raise FileNotFoundError(
            f"Source folder not found: {SOURCE_DIR}\n"
            "Make sure you are running this script from the repository root."
        )

    files_added = []

    with zipfile.ZipFile(OUTPUT_ZIP, "w", zipfile.ZIP_DEFLATED) as zf:
        # Walk the 'Test Code  Sandbox' directory and add every file,
        # stripping the leading 'Test Code  Sandbox/' prefix so that
        # META-INF/, content/, etc. appear at the ZIP root.
        for root, dirs, files in os.walk(SOURCE_DIR):
            # Sort for deterministic output
            dirs.sort()
            for filename in sorted(files):
                abs_path = os.path.join(root, filename)
                # Build the archive name relative to SOURCE_DIR
                rel_path = os.path.relpath(abs_path, SOURCE_DIR)
                # Normalize to forward slashes (required inside ZIP)
                arc_name = rel_path.replace(os.sep, "/")
                zf.write(abs_path, arc_name)
                files_added.append(arc_name)
                print(f"  Added: {arc_name}")

        # Add isNotNullOrEmptyOrZero.expression under content/ in the ZIP
        if os.path.isfile(EXTRA_FILE):
            arc_name = "content/isNotNullOrEmptyOrZero.expression"
            zf.write(EXTRA_FILE, arc_name)
            files_added.append(arc_name)
            print(f"  Added: {arc_name}")
        else:
            print(f"  Warning: extra file not found, skipping: {EXTRA_FILE}")

    print()
    print(f"Total files added : {len(files_added)}")
    print(f"Output ZIP created: {OUTPUT_ZIP}")
    print()
    print("You can now import TestCodeSandbox_Appian.zip into Appian Designer.")


if __name__ == "__main__":
    print("Building Appian import package...")
    print(f"Source : {SOURCE_DIR}")
    print(f"Output : {OUTPUT_ZIP}")
    print()
    build_zip()
