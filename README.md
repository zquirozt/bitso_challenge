# **Data Engineering - Challenge 2**

The objective provide data deposit, withdrawal, event and user for the downstream users Business Intelligence, Machine Learning, Experimentation and Marketing. 

### ERD of the data model:

I used an Entity-Relationship (ER) Modeling.

![ERD.png](bitso_challenge2%2FERD.png)

These tables are related through the user ID, which acts as a primary key in the user_id_sample_data table and as a foreign key in the other tables to relate the user's information to the deposits, withdrawals, and events associated with their account.

**user_id_sample_data:**

Relationship with "deposit_sample_data" and "withdrawal_sample_data": One to many (one user can make many deposits and withdrawals).
Relationship to "event_sample_data": One to many (a user can have multiple events associated with it, such as login, etc.).


**deposit_sample_data:**

Relationship to "user_id_sample_data": Many to one (each bucket is associated with a single user).

**withdrawal_sample_data:**


Relationship to "user_id_sample_data": Many to one (each withdrawal is associated with a single user).

**event_sample_data:**

Relationship to "user_id_sample_data": Many to one (each event is associated with a single user).

The potential downside of this approach is:
- The ER modeling process can be complex, especially for large, complex systems. Identifying all relevant entities, attributes, and relationships may require detailed and exhaustive analysis.
- As data requirements evolve, it can be difficult to modify an existing ER model to accommodate those changes without affecting data integrity or system functionality.
- May not capture all business complexities: In some cases, the ER model may not fully capture all business complexities or business rules, which may lead to incomplete or inadequate database design.

### Load csv files and call functions to generate the answer questions:

In the python file `challenge2.py` I called the following functions:

**load_csv_df:**  Load the files found in the `sources` folder into dataframes.

**active_users_on_day:**  Resolve the question 1: How many users were active on a given day (they made a deposit or withdrawal).

**users_without_deposit:**  Resolve the question 2: Identify users haven't made a deposit.

**users_with_more_than_5_deposits:**  Resolve the question 3: Identify on a given day which users have made more than 5 deposits historically
.

**last_login_date:**  Resolve the question 4: When was the last time a user a user made a login.

**login_count_between_dates:**  Resolve the question 5: How many times a user has made a login between two dates.

**unique_currencies_deposited_on_day:**  Resolve the question 6: Number of unique currencies deposited on a given day.

**unique_currencies_withdrew_on_day:**  Resolve the question 7: Number of unique currencies withdrew on a given day.

**total_amount_deposited_of_currency_on_day:**  Resolve the question 8: Total amount deposited of a given currency on a given day.

#### For each execution that solves a question, a file is generated in the `outputs` folder with the result

### Other files:

- `index.py`, This code sets up an Airflow DAG called "etl_pipeline" that will run a data loading task every day at 9am. The data loading itself is implemented in the load_csv_df function of the load_csv_df module.
- `sql_queries`, SQL file with the queries that will answer the 8 questions
- `get_header_csv`, This is a Python script that reads CSV files in a sources directory, gets the header and data types of each column from each CSV file, and then saves that information to a CSV file called "all_sources_header.csv" in the outputs directory.


