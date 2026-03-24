#!/usr/bin/env bash
# create_appian_package.sh
# Run this script on Mac or Linux to create TestCodeSandbox_Appian.zip
# Requires Python 3 to be installed.

set -e

# Change to the directory where this script lives (repo root)
cd "$(dirname "$0")"

echo "============================================================"
echo " Appian Package Creator"
echo "============================================================"
echo ""

# Prefer python3, fall back to python
if command -v python3 &>/dev/null; then
    PYTHON=python3
elif command -v python &>/dev/null; then
    PYTHON=python
else
    echo "ERROR: Python was not found. Please install Python 3."
    echo "  macOS  : brew install python"
    echo "  Ubuntu : sudo apt-get install python3"
    exit 1
fi

echo "Using: $($PYTHON --version)"
echo ""
echo "Running create_appian_package.py ..."
echo ""

$PYTHON create_appian_package.py

echo ""
echo "Done! Import TestCodeSandbox_Appian.zip into Appian Designer."
