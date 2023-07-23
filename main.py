import streamlit as st
import time
import utils

# Function to initialize Streamlit session state if needed
def init_session_state():
    if "initialized" not in st.session_state:
        st.session_state.initialized = True

# Main function
def main():
    # Initialize Streamlit session state
    init_session_state()
    target_date_str = '2023-11-28 23:59:59'
    quotes_refresh_time = 1800
    remaining_days = 0
    baby_emoji = "👶"
    st.title(f"{baby_emoji}Nandu entry countdown App{baby_emoji}")

    st.empty()
    row1_1, row1_2 = st.columns(2)
    row2_1 = st.text("")
    quotes = utils.get_quotes()
    # Display the countdown timer in the first column
    with row1_1:
        countdown_placeholder = st.empty()
        countdown_placeholder.write("Remaining time: {countdown_str}")
    # Display the countdown timer in the second column
    with row1_2:
        week_placeholder = st.empty()
        week_placeholder.write("Remaining week: {countdown_str}")
    # Display the countdown timer in the second column
    with row2_1:
        quotes_placeholder = st.empty()
        quotes_placeholder.write(quotes)

    time_counter = 0
    while remaining_days >= -50:
        remaining_time = utils.calculate_remaining_time(target_date_str)
        # Extract the number of days
        remaining_days = remaining_time.days
        # Calculate the number of weeks
        remaining_weeks = remaining_days // 7
        remaining_weeks = remaining_weeks + 1
        remaining_time_str = str(remaining_time)
        remaining_weeks_str = str(remaining_weeks)

        with row1_1:
            countdown_placeholder.metric("Remaining time", remaining_time_str)
        with row1_2:
            week_placeholder.metric("Remaining weeks", remaining_weeks_str)
        with row2_1:
            quotes_placeholder.write(quotes)
        time.sleep(1)
        time_counter = time_counter + 1
        
        if time_counter == quotes_refresh_time:
            time_counter = 0
            quotes = utils.get_quotes()


if __name__ == "__main__":
    main()