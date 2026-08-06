SELECT 
    p.product_id,
    COALESCE(latest_prices.new_price, 10) AS price
FROM (
    SELECT DISTINCT product_id 
    FROM Products
) p
LEFT JOIN (
    SELECT 
        product_id,
        new_price,
        RANK() OVER(PARTITION BY product_id ORDER BY change_date DESC) as rnk
    FROM Products
    WHERE change_date <= '2019-08-16'
) latest_prices 
ON p.product_id = latest_prices.product_id AND latest_prices.rnk = 1;
