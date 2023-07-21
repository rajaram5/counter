import streamlit as st
import time
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


# Example usage
target_date_str = '2023-11-28 23:59:59'
remaining_days = 0

print("days left : {}".format(str(remaining_days)))

st.set_page_config()
st.title("Nandu entry countdown timer App")


st.empty()
col1, col2 = st.columns(2)
# Display the countdown timer in the first column
with col1:
    countdown_placeholder = st.empty()
    countdown_placeholder.write("Remaining time: {countdown_str}")

# Display the countdown timer in the second column
with col2:
    week_placeholder = st.empty()
    week_placeholder.write("Remaining week: {countdown_str}")

while remaining_days >= -200:
    remaining_time = calculate_remaining_time(target_date_str)
    # Extract the number of days
    remaining_days = remaining_time.days
    # Calculate the number of weeks
    remaining_weeks = remaining_days // 7

    remaining_weeks = remaining_weeks + 1

    remaining_time_str = str(remaining_time)
    remaining_weeks_str = str(remaining_weeks)

    with col1:
        countdown_placeholder.metric("Remaining time", remaining_time_str)
    with col2:
        week_placeholder.metric("Remaining weeks", remaining_weeks_str)
    time.sleep(1)