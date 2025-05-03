from flask import Flask, render_template, request
from tools.day_of_week.routes import day_of_week_bp
from tools.date_calc.routes import date_calc_bp
from version import APP_VERSION

app = Flask(__name__)
app.config["APP_VERSION"] = APP_VERSION
app.config["ENVIRONMENT"] = "development"
app.debug = True

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

if __name__ == "__main__":
    app.run(debug=True)
