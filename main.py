from flask import Flask, render_template, request
from tools.day_of_week.routes import day_of_week_bp
from tools.date_calc.routes import date_calc_bp
from tools.date_time_calc.routes import date_time_calc_bp
import os
import subprocess

app = Flask(__name__)

# Récupère la dernière version Git (fallback si pas définie côté Azure)
def get_git_version():
    try:
        return subprocess.check_output(
            ["git", "describe", "--tags", "--abbrev=0"],
            stderr=subprocess.DEVNULL
        ).decode("utf-8").strip()
    except Exception:
        return "N/A"

# Version : priorité à la variable d'env définie par Azure, sinon Git
app.config["APP_VERSION"] = os.environ.get("APP_VERSION") or get_git_version()

# Détection de l'environnement
is_azure = os.getenv("WEBSITE_SITE_NAME") is not None
is_local = not is_azure

# Environnement et debug
app.config["ENVIRONMENT"] = "development" if is_local else "production"
app.debug = is_local

# Blueprints
app.register_blueprint(day_of_week_bp, url_prefix="/day-of-week")
app.register_blueprint(date_calc_bp, url_prefix="/calculate-duration")
app.register_blueprint(date_time_calc_bp, url_prefix="/date-time-calc")

# Routes
@app.route("/")
def menu():
    return render_template(
        "menu.html",
        app_version=app.config["APP_VERSION"],
        environment=app.config["ENVIRONMENT"],
        debug=app.debug
    )

@app.route("/hello")
def hello():
    return "Flask is running on Azure!"

@app.route("/version-debug")
def version_debug():
    return f"""
    <pre>
    🧩 Version dans app.config["APP_VERSION"] : {app.config.get("APP_VERSION", "❌ absente")}
    🔄 Version via os.environ["APP_VERSION"]  : {os.getenv("APP_VERSION", "❌ absente")}
    🔧 ENV (app.config["ENVIRONMENT"])       : {app.config.get("ENVIRONMENT", "N/A")}
    🐞 DEBUG                                 : {app.debug}
    🌍 Hébergeur                            : {"Azure" if is_azure else "Local"}
    </pre>
    """

# Injection globale dans tous les templates
@app.context_processor
def inject_globals():
    return {
        "app_version": app.config.get("APP_VERSION", "N/A"),
        "environment": app.config.get("ENVIRONMENT", "N/A"),
        "debug": app.debug
    }

# Lancement local
if __name__ == "__main__":
    app.run(debug=app.debug, use_reloader=app.debug)

