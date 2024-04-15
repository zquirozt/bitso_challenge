# Identify users haven't made a deposit
def users_without_deposit(user_id_sample_data, deposit_sample_data):
    all_users = set(user_id_sample_data["user_id"])
    deposit_users = set(deposit_sample_data["user_id"])
    users_no_deposit = all_users - deposit_users
    return users_no_deposit
