from flask import Blueprint, render_template, request, current_app
from datetime import datetime
import os


date_time_calc_bp = Blueprint("date_time_calc_bp", __name__, template_folder="templates")

@date_time_calc_bp.route("/datetime-duration", methods=["GET", "POST"])
def duration_between_datetimes():
    result = None
    if request.method == "POST":
        try:
            start_str = request.form.get("start_datetime", "").strip()
            end_str = request.form.get("end_datetime", "").strip()

            if not start_str:
                raise ValueError("La date de début est obligatoire.")

            start_dt = datetime.strptime(start_str, "%Y-%m-%d %H:%M:%S")

            if end_str:
                end_dt = datetime.strptime(end_str, "%Y-%m-%d %H:%M:%S")
                end_auto = False
            else:
                end_dt = datetime.now()
                end_auto = True

            duration = end_dt - start_dt

            result = {
                "total_seconds": int(duration.total_seconds()),
                "days": duration.days,
                "hours": duration.seconds // 3600,
                "minutes": (duration.seconds % 3600) // 60,
                "seconds": duration.seconds % 60,
                "end_auto": end_auto,
            }

        except Exception as e:
            result = {"error": f"Erreur lors du calcul : {str(e)}"}

    return render_template(
        "date_time_duration.html",
        result=result,
        app_version=current_app.config.get("APP_VERSION"),
        environment=current_app.config.get("ENVIRONMENT"),
        debug=current_app.debug
)
