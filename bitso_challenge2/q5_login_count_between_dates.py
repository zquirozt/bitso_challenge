import pandas as pd


# How many times a user has made a login between two dates
def login_count_between_dates(user_id, start_date, end_date, event_sample_data):
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)
    user_logins = event_sample_data[
        (event_sample_data["event_name"].str.lower().str.contains("login", case=False))
        & (event_sample_data["user_id"] == user_id)
    ]
    login_count = user_logins[
        (user_logins["event_timestamp"] >= start_date)
        & (user_logins["event_timestamp"] <= end_date)
    ]
    return len(login_count)
