# Retail-Analysis-
This project provides business insight into a fictional superstore's operations through deep exploratory data analysis. Visual and statistical techniques were applied to discover patterns in regional performance, customer behavior, and operational logistics.


#Superstore Retail Data Analysis

A complete exploratory data analysis (EDA) project conducted on the Sample Superstore dataset, originally sourced from https://public.tableau.com/app/learn/sample-data. This analysis simulates a real-world retail business case study, with the goal of extracting actionable insights through structured data preparation, visual exploration, and statistical evaluation.

📌 Objectives

This project is centered around five business-focused objectives:

1. Analyze monthly and yearly profit trends to understand seasonality.
2. Evaluate region-wise profitability to identify high- and low-performing markets.
3. Assess product return frequency by category to gauge product satisfaction.
4. Examine shipping duration patterns to evaluate delivery performance.
5. Analyze customer segments (Consumer, Corporate, Home Office) based on sales, quantity, and profit.



 Key Insights

- December consistently shows the highest profit across years, pointing to seasonal sales spikes.
- The West region leads in profitability, while the **South region** underperforms comparatively.
- Technology products have the highest return rate, suggesting a potential quality or customer expectation gap.
- Shipping is mostly completed within **2–3 days**, indicating operational efficiency.
- The Consumer segment drives volume, while Corporate customers yield higher profit margins.


 EDA Process

- Data loaded from Excel (Orders & Returns sheets)
- Cleaning and type conversions performed using `pandas`
- Feature engineering:
  - `Returned_flag` (binary return indicator)
  - `Shipping Duration` (days between Order and Ship Date)
  - `Month` and `Year` (for temporal grouping)
- Outlier detection using IQR method
- Aggregations via `groupby()` for trends and comparisons



# Visualizations

Visuals created using `matplotlib` and `seaborn`:

- **Line plots**: Profit trends over time
- **Bar charts**: Region-wise and segment-wise performance
- **Pie charts**: Return distribution by category
- **Histograms**: Shipping durations
- **Subplots**: Multi-metric comparisons (sales, profit, quantity)

---

 Tools & Skills Demonstrated

- Data Cleaning & Transformation
- Feature Engineering
- Business-Oriented EDA
- Data Visualization & Storytelling
- Analytical Thinking

---

## References

- Sample Dataset: [Tableau Public – Sample Data](https://public.tableau.com/app/learn/sample-data)  
- [Pandas Documentation](https://pandas.pydata.org/)  
- [Seaborn Documentation](https://seaborn.pydata.org/)  
- [Matplotlib Documentation](https://matplotlib.org/)  
- [Python Official Docs](https://docs.python.org/3/)



> ✨ *This project was built as part of my learning journey in data analytics, combining business intuition with analytical depth.*
