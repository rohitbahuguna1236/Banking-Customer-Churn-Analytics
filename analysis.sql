-- 1. Total Customers
SELECT COUNT(*) AS total_customers
FROM customers;

-- 2. Total Churned Customers
SELECT COUNT(*) AS churned_customers
FROM customers
WHERE churn = 1;

-- 3. Churn by Country
SELECT country,
       COUNT(*) AS total_customers,
       SUM(churn) AS churned_customers
FROM customers
GROUP BY country
ORDER BY churned_customers DESC;

-- 4. Churn by Gender
SELECT gender,
       COUNT(*) AS total_customers,
       SUM(churn) AS churned_customers
FROM customers
GROUP BY gender;

-- 5. Churn by Number of Products
SELECT products_number,
       COUNT(*) AS total_customers,
       SUM(churn) AS churned_customers
FROM customers
GROUP BY products_number
ORDER BY products_number;
SELECT COUNT(*) AS total_customers
FROM customers;