import os
import subprocess

try:
    # Lecture du tag Git si dispo (local)
    APP_VERSION = subprocess.check_output(["git", "describe", "--tags"]).decode().strip()
except Exception:
    # Sinon, variable d'env (Azure)
    APP_VERSION = os.getenv("APP_VERSION", "dev") 
