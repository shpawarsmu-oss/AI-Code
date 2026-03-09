import os
import zipfile

# ============================================================
# Appian Package Builder
# Builds a valid Appian import ZIP from the repo folder
# Run: python build_appian_package.py
# ============================================================

SOURCE_FOLDER = "Test Code  Sandbox"
OUTPUT_ZIP    = "TestCodeSandbox_Appian_IMPORT.zip"

def build_zip():
    if not os.path.isdir(SOURCE_FOLDER):
        print(f"ERROR: Source folder not found: '{SOURCE_FOLDER}'")
        print("Make sure you run this script from inside the AI-Code repo root folder.")
        return

    file_count = 0
    with zipfile.ZipFile(OUTPUT_ZIP, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(SOURCE_FOLDER):
            # Skip hidden folders like .git
            dirs[:] = [d for d in dirs if not d.startswith(".")]
            for file in files:
                if file.startswith("."):
                    continue
                full_path = os.path.join(root, file)
                # Strip the source folder prefix so META-INF is at root of ZIP
                arcname = os.path.relpath(full_path, SOURCE_FOLDER)
                zf.write(full_path, arcname)
                print(f"  Added: {arcname}")
                file_count += 1

    print(f"\n✅ SUCCESS! ZIP created: {OUTPUT_ZIP}")
    print(f"   Total files: {file_count}")
    print(f"\n📦 Now import '{OUTPUT_ZIP}' into Appian Designer → Import Package")
    print("\n⚠️  VERIFY: Open the ZIP and confirm META-INF/ is at the ROOT (not inside a subfolder)")

if __name__ == "__main__":
    build_zip()