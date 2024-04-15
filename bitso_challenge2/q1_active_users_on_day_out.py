# How many users were active on a given day (they made a deposit or withdrawal)
import pandas as pd


def active_users_on_day(date, withdrawals_df, deposit_df):
    date = pd.to_datetime(date)
    active_users = set(
        withdrawals_df.loc[
            withdrawals_df['event_timestamp'].dt.strftime('%Y-%m-%d') == date.strftime('%Y-%m-%d'), 'user_id'])
    active_users.update(
        set(deposit_df.loc[
                deposit_df['event_timestamp'].dt.strftime('%Y-%m-%d') == date.strftime('%Y-%m-%d'), 'user_id']))
    return len(active_users)
    # print(len(active_users))


