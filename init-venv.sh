set -e
echo "Deleting virtual environment if exists"
if [ -d venv ]; then rm -rf venv; fi

echo "Creating virtual environment"
python -m venv venv

echo "Installing dependancies"
venv/scripts/python.exe -m pip install --upgrade pip
venv/scripts/pip install -r requirements.txt -r requirements-dev.txt