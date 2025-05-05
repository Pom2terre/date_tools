from datetime import datetime, date
import calendar
import locale

# Use French locale for month/day names
try:
    locale.setlocale(locale.LC_TIME, "fr_FR.UTF-8")
except locale.Error:
    locale.setlocale(locale.LC_TIME, "")

def analyze_date(date_str):
    try:
        input_date = datetime.strptime(date_str, "%d/%m/%y").date()
        year = input_date.year
        month = input_date.month
        weekday_num = input_date.weekday()  # 0 = Monday, 6 = Sunday
        weekday = input_date.strftime("%A")
        month_name = input_date.strftime("%B")
        day_of_year = input_date.timetuple().tm_yday
        total_days_year = 366 if calendar.isleap(year) else 365
        days_left = total_days_year - day_of_year
        total_days_month = calendar.monthrange(year, month)[1]

        all_weekdays_year = [
            d for m in range(1, 13)
            for d in (date(year, m, day) for day in range(1, calendar.monthrange(year, m)[1] + 1))
            if d.weekday() == weekday_num
        ]
        all_weekdays_month = [d for d in all_weekdays_year if d.month == month]

        weekday_index_year = all_weekdays_year.index(input_date) + 1
        weekday_index_month = all_weekdays_month.index(input_date) + 1

        return {
            "original_date": input_date.strftime("%d %B %Y"),
            "weekday": weekday,
            "day_of_year": day_of_year,
            "days_left": days_left,
            "weekday_index_year": weekday_index_year,
            "weekday_total_year": len(all_weekdays_year),
            "weekday_index_month": weekday_index_month,
            "weekday_total_month": len(all_weekdays_month),
            "year_days": total_days_year,
            "month_days": total_days_month
        }

    except Exception as e:
        return {"error": str(e)}
