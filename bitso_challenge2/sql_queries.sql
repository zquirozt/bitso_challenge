-- How many users were active on a given day (they made a deposit or withdrawal)
SELECT COUNT(DISTINCT user_id) AS num_active_users
FROM (
    SELECT DISTINCT user_id FROM deposit_sample_data WHERE DATE(event_timestamp) = '2020-03-26'
    UNION
    SELECT DISTINCT user_id FROM withdrawals_sample_data WHERE DATE(event_timestamp) = '2020-03-26'
) AS active_users;

-- Identify users haven't made a deposit

SELECT DISTINCT user_id
FROM user_id_sample_data
WHERE user_id NOT IN (
    SELECT DISTINCT user_id FROM deposit_sample_data
);

-- Identify on a given day which users have made more than 5 deposits historically

SELECT user_id
FROM deposit_sample_data
WHERE DATE(event_timestamp) <= '2024-04-14'
GROUP BY user_id
HAVING COUNT(*) > 5;

-- When was the last time a user a user made a login

SELECT user_id, MAX(event_timestamp) AS last_login_time
FROM event_sample_data
WHERE user_id = '5dd53e1664525233d42f0464ecfb47f1' AND lowercase(event_name) LIKE '%login%';

-- How many times a user has made a login between two dates
SELECT COUNT(*) AS login_count
FROM event_sample_data
WHERE user_id = '5dd53e1664525233d42f0464ecfb47f1'
AND lowercase(event_name) LIKE '%login%'
AND event_timestamp >= '2020-03-26'
AND event_timestamp <= '2024-12-31';

-- Number of unique currencies deposited on a given day
SELECT COUNT(DISTINCT currency) AS num_unique_currencies_deposited
FROM deposit_sample_data
WHERE DATE(event_timestamp) = '2020-03-26';

-- Number of unique currencies withdrew on a given day
SELECT COUNT(DISTINCT currency) AS num_unique_currencies_withdrew
FROM withdrawals_sample_data
WHERE DATE(event_timestamp) = '020-03-26';

-- Total amount deposited of a given currency on a given day

SELECT SUM(amount) AS total_deposited
FROM withdrawals_sample_data
WHERE DATE(deposit_date) = '020-03-26' and currency = 'usd';
