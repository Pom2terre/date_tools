from flask import Blueprint, render_template, request, current_app
from datetime import datetime

date_time_calc_bp = Blueprint("date_time_calc_bp", __name__, template_folder="templates")

def try_parse_datetime(date_str):
    for fmt in ("%d-%m-%Y %H:%M", "%Y-%m-%d %H:%M:%S"):
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    raise ValueError(f"Format de date invalide : {date_str}")

@date_time_calc_bp.route("/datetime-duration", methods=["GET", "POST"])
def duration_between_datetimes():
    result = None

    if request.method == "POST":
        try:
            start_str = request.form.get("start_datetime", "").strip()
            end_str = request.form.get("end_datetime", "").strip()

            if not start_str and not end_str:
                raise ValueError("Il faut au moins une date/heure de début ou de fin.")

            now = datetime.now()

            # Déduire les dates
            start_dt = try_parse_datetime(start_str) if start_str else now
            end_dt = try_parse_datetime(end_str) if end_str else now


            duration = end_dt - start_dt

            result = {
                "total_seconds": int(duration.total_seconds()),
                "days": duration.days,
                "hours": duration.seconds // 3600,
                "minutes": (duration.seconds % 3600) // 60,
                "seconds": duration.seconds % 60,
                "end_auto": not bool(end_str),
                "start_str_formatted": start_dt.strftime("%d:%m:%Y %H:%M"),
                "end_str_formatted": end_dt.strftime("%d:%m:%Y %H:%M")
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
