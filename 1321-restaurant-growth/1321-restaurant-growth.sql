SELECT 
    visited_on,
    amount,
    average_amount
FROM (
    SELECT 
        visited_on,
        -- 1. Calculate the 7-day rolling sum using our sliding box
        SUM(daily_amount) OVER(
            ORDER BY visited_on 
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ) AS amount,
        -- 2. Calculate the 7-day rolling average and round to 2 decimals
        ROUND(SUM(daily_amount) OVER(
            ORDER BY visited_on 
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ) / 7, 2) AS average_amount,
        -- 3. Row number to help us drop the first 6 days later
        ROW_NUMBER() OVER(ORDER BY visited_on) AS row_num
    FROM (
        -- Layer 1: Collapse data so 1 row = 1 day
        SELECT visited_on, SUM(amount) AS daily_amount
        FROM Customer
        GROUP BY visited_on
    ) AS daily_summary
) AS rolling_calculations
-- Layer 3: Only show results from the 7th day onward
WHERE row_num >= 7;
