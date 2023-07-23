from datetime import datetime, timedelta

def calculate_remaining_time(target_date_str):
    try:
        # Convert the target date string to a datetime object
        target_date = datetime.strptime(target_date_str, '%Y-%m-%d %H:%M:%S')

        # Get the current date and time
        current_date = datetime.now()

        # Calculate the time difference
        remaining_time = target_date - current_date

        # Round seconds to the nearest whole number
        remaining_seconds = int(remaining_time.total_seconds())
        remaining_time = timedelta(seconds=round(remaining_seconds))

        return remaining_time
    except ValueError:
        return None