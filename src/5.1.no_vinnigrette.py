import datetime
import random

"""Generate a random date between two dates and check if it's a Monday."""
def no_vinnigrete(start_date, end_date):
    try:
        # Convert input strings to datetime objects
        start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        print("One or both of the dates are not in the correct format. Use YYYY-MM-DD.")
        return

    if start_date > end_date:
        start_date, end_date = end_date, start_date

    total_days = (end_date - start_date).days
    random_offset = random.randint(0, total_days)
    random_date = start_date + datetime.timedelta(days=random_offset)

    is_monday = random_date.weekday() == 0

    print("Ain't gettin' no vinaigrette today :(" if is_monday else "It's not Monday.")

def main() -> None:
    date1 = "1912-06-23"
    date2 = "1954-06-07"

    no_vinnigrete(date1, date2)

if __name__ == '__main__':
    main()
