-- Total number of schemes
SELECT COUNT(*) FROM scheme_master;

-- Average AUM by category
SELECT category,
AVG(aum_crore)
FROM scheme_performance
GROUP BY category;

-- Top 10 funds by Sharpe Ratio
SELECT scheme_name,
sharpe_ratio
FROM scheme_performance
ORDER BY sharpe_ratio DESC
LIMIT 10;

-- Average Returns by Risk Grade
SELECT risk_grade,
AVG(return_3yr_pct)
FROM scheme_performance
GROUP BY risk_grade;

-- Top Fund Houses by AUM
SELECT fund_house,
SUM(aum_crore)
FROM scheme_performance
GROUP BY fund_house
ORDER BY SUM(aum_crore) DESC;