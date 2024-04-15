# When was the last time a user made a login
def last_login_date(user_id, event_sample_data):
    user_logins = event_sample_data[
        (event_sample_data["event_name"] == "login_api")
        & (event_sample_data["user_id"] == user_id)
    ]
    if len(user_logins) > 0:
        return user_logins["event_timestamp"].max().date()
    else:
        return None
