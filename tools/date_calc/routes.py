from flask import Blueprint, render_template, request
from datetime import datetime, timedelta
import os
date_calc_bp = Blueprint("date_calc", __name__, template_folder="templates")

@date_calc_bp.route("/", methods=["GET", "POST"])
def calculate_duration():
    result = {}
    if request.method == "POST":
        try:
            start_date_str = request.form.get("start_date")
            end_date_str = request.form.get("end_date")
            include_today = request.form.get("include_today") == "on"

            if not start_date_str:
                raise ValueError("Date de début manquante.")

            start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
            end_date = (
                datetime.strptime(end_date_str, "%Y-%m-%d").date()
                if end_date_str
                else datetime.today().date()
            )

            if include_today:
                delta = end_date - start_date + timedelta(days=1)
            else:
                delta = end_date - start_date

            # Inverse if end < start
            if delta.days < 0:
                start_date, end_date = end_date, start_date
                delta = end_date - start_date

            days = delta.days

            result = {
                "start_date": start_date.strftime("%d/%m/%y"),
                "end_date": end_date.strftime("%d/%m/%y"),
                "time_duration_days": days,
                "time_duration_months": round(days / 30, 2),
                "time_duration_years": round(days / 365, 2),
                "time_duration_remaining_days_in_month": days % 30,
                "time_duration_seconds": days * 86400,
                "time_duration_minutes": days * 1440,
                "time_duration_hours": days * 24,
                "time_duration_weeks": round(days / 7, 2),
                "time_duration_percentage": round(days / 365 * 100, 2),
                "current_year": end_date.year,
                "calculation_done": True,
                "include_today": include_today,
                "environment": os.getenv("FLASK_ENV", "dev"),
                "app_version": os.getenv("APP_VERSION", "1.0.0"),
            }
        except Exception as e:
            result = {"error": str(e)}

    return render_template("calculate_duration.html", result=result)
