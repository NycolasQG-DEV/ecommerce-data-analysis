# Ecommerce Data Analysis

## Overview
This project performs an end-to-end analysis of e-commerce data, transforming raw transactional data into actionable business insights and an interactive dashboard.

It simulates a real-world data workflow, including data processing, analysis, visualization, and reporting.

---

## Objectives
- Analyze revenue distribution across product categories  
- Identify top-performing products and customers  
- Evaluate sales trends over time  
- Build a clean and reproducible data pipeline  
- Create an interactive dashboard for data exploration  

---

## Tech Stack

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white"/>
  <img src="https://img.shields.io/badge/Matplotlib-20232A?style=for-the-badge&logo=plotly&logoColor=white"/>
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
</p>

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
  <img src="reports/category_revenue.png" width="500"/>
</p>

---

### Revenue Over Time
<p align="center">
  <img src="reports/revenue_over_time.png" width="500"/>
</p>

---

### Top Products
<p align="center">
  <img src="reports/top_products.png" width="500"/>
</p>

---

### Top Customers
<p align="center">
  <img src="reports/top_customers.png" width="500"/>
</p>

---

## Dashboard

An interactive dashboard was built using Streamlit to explore the data dynamically.

<p align="center">
  <img src="reports/dashboard.png" width="800"/>
</p>

---

## Key Insights

- Electronics is the leading revenue category, indicating strong demand for tech products  
- Revenue varies over time, suggesting possible seasonality patterns  
- A small number of products generate a large portion of total revenue (Pareto effect)  
- High-value customers contribute significantly to overall revenue  

---

## How to Run

Install dependencies:
```bash
pip install -r requirements.txt
