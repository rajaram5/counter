from datetime import datetime, timedelta
import requests
import random
import json
import os
import streamlit
import pytz

ninjas_key = os.environ["ninjas_key"]

#@st.cache(suppress_st_warning=True)
def calculate_remaining_time(target_date_str):
    try:
        # Convert the target date string to a datetime object
        target_date = datetime.strptime(target_date_str, '%Y-%m-%d %H:%M:%S')
        # Get the timezone object for the Netherlands
        netherlands_tz = pytz.timezone('Europe/Amsterdam')

        # Get the current time in the Netherlands timezone
        current_time = datetime.now(netherlands_tz)

        # Calculate the time difference
        remaining_time = target_date - current_time

        # Round seconds to the nearest whole number
        remaining_seconds = int(remaining_time.total_seconds())
        remaining_time = timedelta(seconds=round(remaining_seconds))

        return remaining_time
    except ValueError:
        return None
#@st.cache(suppress_st_warning=True)
def get_quotes():
    categories = ['age', 'beauty', 'family', 'funny', 'future', 'happiness', 'home', 'life', 'mom']
    category = random.choice(categories)
    api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
    response = requests.get(api_url, headers={'X-Api-Key': ninjas_key})
    if response.status_code == requests.codes.ok:
        print(response.text)
        data_list = json.loads(response.text)
        quote = data_list[0]["quote"]
        quote = "<" + category + " quote> " + quote
        return quote
    else:
        print("Error:", response.status_code, response.text)
