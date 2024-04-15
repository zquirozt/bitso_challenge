import pandas as pd

from bitso_challenge2.generate_output import generate_output_file
from bitso_challenge2.load_csv_df import load_csv_df
from bitso_challenge2.q1_active_users_on_day_out import active_users_on_day
from bitso_challenge2.q2_users_without_deposit import users_without_deposit
from bitso_challenge2.q3_users_with_more_than_5_deposits import (
    users_with_more_than_5_deposits,
)
from bitso_challenge2.q4_last_login_date import last_login_date
from bitso_challenge2.q5_login_count_between_dates import login_count_between_dates
from bitso_challenge2.q6_unique_currencies_deposited_on_day import (
    unique_currencies_deposited_on_day,
)
from bitso_challenge2.q7_unique_currencies_withdrew_on_day import (
    unique_currencies_withdrew_on_day,
)
from bitso_challenge2.q8_total_amount_deposited_of_currency_on_day import (
    total_amount_deposited_of_currency_on_day,
)

source_directory = "./sources/"
output_directory = "./outputs/"
start_date = pd.to_datetime("2020-03-26")
end_date = pd.to_datetime("2024-12-31")
user_id = "5dd53e1664525233d42f0464ecfb47f1"
currency = "usd"

if __name__ == "__main__":
    path_files = source_directory
    dataframes = load_csv_df(path_files)
    # for df_name in dataframes.keys():
    #     print(df_name)
    event_sample_data = dataframes["event_sample_data"]
    withdrawals_sample_data = dataframes["withdrawals_sample_data"]
    user_id_sample_data = dataframes["user_id_sample_data"]
    deposit_sample_data = dataframes["deposit_sample_data"]

    # question 1
    # How many users were active on a given day (they made a deposit or withdrawal)
    active_users_on_day_out = active_users_on_day(
        start_date, withdrawals_sample_data, deposit_sample_data
    )
    generate_output_file(
        "q1_active_users_on_day_out", active_users_on_day_out, output_directory
    )

    # question 2
    # Identify users haven't made a deposit
    users_without_deposit_out = users_without_deposit(
        user_id_sample_data, deposit_sample_data
    )
    generate_output_file(
        "q2_users_without_deposit_out", users_without_deposit_out, output_directory
    )

    # question 3
    # Identify on a given day which users have made more than 5 deposits historically
    users_with_more_than_5_deposits_out = users_with_more_than_5_deposits(
        start_date, deposit_sample_data
    )
    generate_output_file(
        "q3_users_with_more_than_5_deposits_out",
        users_with_more_than_5_deposits_out,
        output_directory,
    )

    # question 4
    # When was the last time a user made a login
    last_login_date_out = last_login_date(user_id, event_sample_data)
    generate_output_file(
        "q4_last_login_date_out", last_login_date_out, output_directory
    )

    # question 5
    # How many times a user has made a login between two dates
    login_count_between_dates_out = login_count_between_dates(
        user_id, start_date, end_date, event_sample_data
    )
    generate_output_file(
        "q5_login_count_between_dates_out",
        login_count_between_dates_out,
        output_directory,
    )

    # question 6
    # Number of unique currencies deposited on a given day
    unique_currencies_deposited_on_day_out = unique_currencies_deposited_on_day(
        start_date, deposit_sample_data
    )
    generate_output_file(
        "q6_unique_currencies_deposited_on_day_out",
        unique_currencies_deposited_on_day_out,
        output_directory,
    )

    # question 7
    # Number of unique currencies withdrew on a given day
    unique_currencies_withdrew_on_day_out = unique_currencies_withdrew_on_day(
        start_date, withdrawals_sample_data
    )
    generate_output_file(
        "q7_unique_currencies_withdrew_on_day_out",
        unique_currencies_withdrew_on_day_out,
        output_directory,
    )

    # question 8
    # Total amount deposited of a given currency on a given day
    total_amount_deposited_of_currency_on_day_out = (
        total_amount_deposited_of_currency_on_day(
            currency, start_date, deposit_sample_data
        )
    )
    generate_output_file(
        "q8_total_amount_deposited_of_currency_on_day_out",
        total_amount_deposited_of_currency_on_day_out,
        output_directory,
    )
