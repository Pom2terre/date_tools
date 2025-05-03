from flask import Blueprint, render_template, request
from .utils import analyze_date

day_of_week_bp = Blueprint("day_of_week", __name__, template_folder="templates")

@day_of_week_bp.route("/", methods=["GET", "POST"])
def day_of_week():
    result = None
    if request.method == "POST":
        date_str = request.form.get("date")  # Récupère la date du champ unique
        if date_str:
            # Convertit 'YYYY-MM-DD' → 'DD/MM/YY' attendu par analyze_date()
            parts = date_str.split("-")
            if len(parts) == 3:
                year, month, day = parts
                short_year = year[-2:]
                reformatted = f"{int(day):02d}/{int(month):02d}/{short_year}"
                result = analyze_date(reformatted)
    return render_template("day_of_week.html", result=result)
