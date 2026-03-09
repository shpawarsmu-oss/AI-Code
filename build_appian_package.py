import os, zipfile
SOURCE = "Test Code  Sandbox"
OUTPUT = "TestCodeSandbox_Appian_IMPORT.zip"
with zipfile.ZipFile(OUTPUT, "w", zipfile.ZIP_DEFLATED) as zf:
    for root, dirs, files in os.walk(SOURCE):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for f in files:
            if f.startswith('.'): continue
            full = os.path.join(root, f)
            arc  = os.path.relpath(full, SOURCE)
            zf.write(full, arc)
print("Done:", OUTPUT)