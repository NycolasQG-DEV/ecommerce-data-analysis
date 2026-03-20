# Ecommerce Data Analysis

## Overview
This project performs an end-to-end analysis of e-commerce data, transforming raw transactional data into actionable business insights and an interactive dashboard.

It simulates a real-world data workflow, including data processing, analysis, visualization, and reporting.

---

## Tech Stack

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-orange)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)

---

## Project Structure

- data/ → raw and processed data  
- src/ → data pipeline and analysis  
- dashboard/ → interactive application  
- reports/ → generated visualizations  
- main.py → pipeline execution  

---

## Data Pipeline

The project follows a structured ETL pipeline:

1. Data Loading (CSV files)  
2. Data Transformation (joins and cleaning)  
3. Feature Engineering (revenue calculation)  
4. Data Export (processed dataset)  
5. Analysis & Visualization  

---

## Visualizations

### Revenue by Category
<p align="center">
  <img src="reports/category_revenue.png" width="700"/>
</p>

---

### Revenue Over Time
<p align="center">
  <img src="reports/revenue_over_time.png" width="700"/>
</p>

---

### Top Products
<p align="center">
  <img src="reports/top_products.png" width="700"/>
</p>

---

### Top Customers
<p align="center">
  <img src="reports/top_customers.png" width="700"/>
</p>

## Dashboard

<p align="center">
  <img src="reports/dashboard.png" width="900"/>
</p>

---

## Key Insights

- Electronics is the leading revenue category, indicating strong demand for technology products  
- Revenue varies over time, suggesting possible seasonality patterns  
- A small number of products generate a large portion of total revenue (Pareto effect)  
- High-value customers contribute significantly to overall revenue  

---

## How to Run

Install dependencies:
pip install -r requirements.txt

Run data pipeline:
python main.py

Run dashboard:
streamlit run dashboard/app.py

---

## Dataset

The dataset used in this project is publicly available on Kaggle:
https://www.kaggle.com/datasets/marthadimgba/online-shop-2024

---

## Conclusion

This project demonstrates:

- Data analysis and transformation skills  
- Business-oriented thinking  
- Data visualization techniques  
- Project structuring best practices  
- Dashboard development  

---

## Future Improvements

- Add customer lifetime value (CLV) analysis  
- Deploy dashboard to the cloud  
- Integrate with real-time data sources  