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
    remaining_days = 0

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

    while remaining_days >= -50:
        remaining_time = utils.calculate_remaining_time(target_date_str)
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

if __name__ == "__main__":
    main()