from flask import Flask, render_template, request
from tools.day_of_week.routes import day_of_week_bp
from tools.date_calc.routes import date_calc_bp
from version import APP_VERSION
import os

app = Flask(__name__)
app.config["APP_VERSION"] = APP_VERSION
# Set config based on environment
env = os.getenv("FLASK_ENV", "production")
app.config["ENVIRONMENT"] = env
app.debug = env == "development"

app.register_blueprint(day_of_week_bp, url_prefix="/day-of-week")
app.register_blueprint(date_calc_bp, url_prefix="/calculate-duration")

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
    import os
    from version import APP_VERSION

    return f"""
    <pre>
    🌐 Version Flask : {APP_VERSION}
    🔧 ENV (app.config) : {app.config.get("ENVIRONMENT", "N/A")}
    🐞 DEBUG : {app.debug}
    🔄 APP_VERSION via os.environ : {os.getenv("APP_VERSION", "N/A")}
    </pre>
    """

if __name__ == "__main__":
    # Pour exécution en local uniquement
    app.run(debug=True)


