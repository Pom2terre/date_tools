from datetime import datetime

def calculate_duration_between_datetimes(start_date, start_time, end_date, end_time):
    try:
        start_dt = datetime.strptime(f"{start_date} {start_time}", "%Y-%m-%d %H:%M:%S")
        end_dt = datetime.strptime(f"{end_date} {end_time}", "%Y-%m-%d %H:%M:%S")
        duration = end_dt - start_dt
        return {
            "total_seconds": int(duration.total_seconds()),
            "days": duration.days,
            "hours": duration.seconds // 3600,
            "minutes": (duration.seconds % 3600) // 60,
            "seconds": duration.seconds % 60
        }
    except Exception as e:
        return {"error": str(e)}
