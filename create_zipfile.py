import zipfile
import os

exclude = {'.git', '.github', 'venv', '__pycache__', 'deploy.zip', '.DS_Store'}

def should_include(filepath):
    for part in filepath.split(os.sep):
        if part in exclude:
            return False
    return True

with zipfile.ZipFile('deploy.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk('.'):
        for file in files:
            filepath = os.path.join(root, file)
            relpath = os.path.relpath(filepath, '.')
            if should_include(relpath):
                zipf.write(filepath, relpath)

print("✅ deploy.zip créé avec succès.")
