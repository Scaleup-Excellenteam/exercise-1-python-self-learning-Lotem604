import datetime
import random

def no_vinigrete(start_date: str, end_date: str) -> bool:
    """
    Generate a random date between two given dates and check if it's a Monday.

    Args:
        start_date (str): Start date in 'YYYY-MM-DD' format.
        end_date (str): End date in 'YYYY-MM-DD' format.

    Returns:
        bool: True if the random date is a Monday, False otherwise.
    """
    try:
        start_dt = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        end_dt = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Dates must be in 'YYYY-MM-DD' format.") 

    if start_dt > end_dt:
        start_dt, end_dt = end_dt, start_dt

    total_days = (end_dt - start_dt).days
    random_offset = random.randint(0, total_days)
    random_date = start_dt + datetime.timedelta(days=random_offset)

    is_monday = random_date.weekday() == 0
    print("Ain't gettin' no vinaigrette today :(" if is_monday else "It's not Monday.")

def main() -> None:
    """Main function to run the Vinigrete checker program."""
    date1 = input("Enter the first date (YYYY-MM-DD): ")
    date2 = input("Enter the second date (YYYY-MM-DD): ")
    no_vinigrete(date1, date2)
if __name__ == '__main__':
    main()
