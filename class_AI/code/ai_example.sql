-- Extracting a feature set for Churn Prediction
-- This combines user info, transaction history, and login logs
WITH user_activity AS (
    SELECT
        u.user_id,
        u.registration_date,
        COUNT(DISTINCT t.transaction_id) as total_transactions,
        SUM(t.amount) as total_spent,
        MAX(t.transaction_date) as last_purchase_date,
        DATEDIFF(day, MAX(t.transaction_date), GETDATE()) as days_since_last_purchase,
        COUNT(DISTINCT CASE WHEN l.login_date >= DATEADD(month, -1, GETDATE()) THEN l.login_id END) as logins_last_30_days
    FROM users u
    LEFT JOIN transactions t ON u.user_id = t.user_id
    LEFT JOIN login_logs l ON u.user_id = l.user_id
    GROUP BY u.user_id, u.registration_date
)
SELECT
    user_id,
    total_transactions,
    total_spent,
    days_since_last_purchase,
    logins_last_30_days,
    -- Creating a target label: 1 if they haven't logged in for 60 days (Churned)
    CASE WHEN days_since_last_purchase > 60 THEN 1 ELSE 0 END as is_churned
FROM user_activity
WHERE registration_date < DATEADD(year, -1, GETDATE()) -- Only users older than 1 year
AND total_transactions > 0; -- Exclude users who never bought anything
