# How to Import the Appian Package

This guide explains how to create a valid **Appian-importable ZIP** from this repository and import it into your Appian environment.

---

## Why a Special Script Is Needed

When you download a GitHub repository as a ZIP and try to re-zip a subfolder, the folder structure often becomes nested one level too deep — `META-INF/` ends up inside a parent folder instead of at the ZIP root. Appian requires `META-INF/MANIFEST.MF` to be at the **root** of the ZIP, and will reject the package with error `APNX-1-4154-000` otherwise.

The `create_appian_package.py` script handles this automatically.

---

## Step 1 — Get the Repository

**Option A — Download ZIP (no Git required)**

1. Go to <https://github.com/shpawarsmu-oss/AI-Code>
2. Click the green **`<> Code`** button → **Download ZIP**
3. Extract the ZIP to a folder on your computer (e.g. `C:\Downloads\AI-Code-main\`)

**Option B — Clone with Git**

```bash
git clone https://github.com/shpawarsmu-oss/AI-Code.git
```

---

## Step 2 — Run the Package Creator

### 🪟 Windows (double-click)

1. Open the extracted `AI-Code-main` (or `AI-Code`) folder
2. Double-click **`create_appian_package.bat`**
3. A console window opens, builds the ZIP, then closes

### 🍎 Mac / Linux (terminal)

```bash
cd AI-Code          # or AI-Code-main if you downloaded the ZIP
chmod +x create_appian_package.sh
./create_appian_package.sh
```

### 🐍 Any platform — Python directly

```bash
cd AI-Code
python create_appian_package.py
```

> **Requirement:** Python 3 must be installed. Download from <https://www.python.org/downloads/>  
> No third-party packages are needed — only the Python standard library is used.

---

## Step 3 — Verify the Output

After the script runs you will see `TestCodeSandbox_Appian.zip` in the same folder. Open it with 7-Zip, WinZip, or your OS archive tool and confirm the structure looks like this:

```
TestCodeSandbox_Appian.zip
├── META-INF/                        ← MUST be here at the root
│   ├── MANIFEST.MF
│   └── export.log
├── application/
│   └── ac666b41-f00b-43e9-81b6-b402be1ae607.xml
├── content/
│   ├── 6dd9ebbc-5f0e-41ce-a132-92165db432fb.xml
│   ├── 9aa3e491-531c-4fdf-98b6-14b13035fda5.xml
│   ├── BannerMessage.xml
│   ├── _a-0000ef01-21b7-8000-bad0-01ef9001ef90_1096443.xml
│   ├── _a-0000ef01-21b7-8000-bad0-01ef9001ef90_1096460.xml
│   ├── _a-0000ef01-21b7-8000-bad0-01ef9001ef90_1096623.xml
│   ├── a3c5e7f9-b2d4-4a6c-8e0f-1b3d5f7a9c2e.xml
│   ├── adc46f5b-b3a3-4bd2-875f-95dc1b9d0abc.xml
│   ├── b26fc0d0-477a-4f37-9eaf-d3e658beb1b4.xml
│   ├── f33cfbf7-3d0e-41d9-8c5d-1d232db2aef9.xml
│   └── isNotNullOrEmptyOrZero.expression
├── group/
│   ├── 1c1de46b-4b0a-4216-8551-3bbfcaf460ad.xml
│   └── fd6d09ad-4a10-4aff-8e17-f5f9a58dccce.xml
├── processModel/
│   └── b66e24bb-aa86-4add-9717-f17e6139edf0.xml
├── processModelFolder/
│   └── f0822154-67a7-4f04-9d4e-3caed55fbc4d.xml
└── recordType/
    ├── 654a9376-f983-4729-9e04-3416bec1dc59.xml
    ├── 935291e5-21cd-4303-bec4-49aacd414213.xml
    └── edb6b43f-1d34-46dd-8e03-30ed591381f6.xml
```

> ⚠️ If you see a `Test Code  Sandbox/` folder **inside** the ZIP wrapping all of the above, the ZIP is wrong and Appian will reject it with `APNX-1-4154-000`. Run the script again instead of zipping manually.

---

## Step 4 — Import into Appian

1. Log in to your **Appian Designer** environment
2. Open (or create) the target application
3. Click **⋮** (more options) → **Import**
4. Select `TestCodeSandbox_Appian.zip`
5. Follow the import wizard and click **Import**

A successful import will show a green confirmation. All 20+ objects (expression rules, interfaces, groups, record types, process models) will be available in your application.

---

## Included Objects

| Folder | Object Type | Count |
|--------|-------------|-------|
| `META-INF/` | Package metadata (Appian 25.3.640.0) | — |
| `application/` | Application manifest | 1 |
| `content/` | Expression Rules, Interfaces, Constants | 11 |
| `group/` | Groups | 2 |
| `processModel/` | Process Models | 1 |
| `processModelFolder/` | Process Model Folders | 1 |
| `recordType/` | Record Types | 3 |

---

## Troubleshooting

| Error | Cause | Fix |
|-------|-------|-----|
| `APNX-1-4154-000` | `META-INF/` not at ZIP root | Use the Python script — do **not** manually re-zip |
| `Python was not found` | Python not installed | Install from <https://www.python.org/downloads/> |
| `Source folder not found` | Script not run from repo root | `cd` into the `AI-Code` folder first |
