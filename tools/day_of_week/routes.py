from flask import Blueprint, render_template, request
from .utils import analyze_date

day_of_week_bp = Blueprint("day_of_week", __name__, template_folder="templates")

@day_of_week_bp.route("/", methods=["GET", "POST"])
def day_of_week():
    result = None
    if request.method == "POST":
        day = request.form.get("day")
        month = request.form.get("month")
        year = request.form.get("year")
        if day and month and year:
            date_str = f"{int(day):02d}/{int(month):02d}/{int(year):02d}"
            result = analyze_date(date_str)
    return render_template("day_of_week.html", result=result)
