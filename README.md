# Ecommerce Data Analysis

## Overview
End-to-end e-commerce data analysis project focused on transforming raw data into actionable business insights and an interactive dashboard for decision-making.

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

- data/ → raw and processed datasets  
- src/ → data processing and analysis modules  
- dashboard/ → interactive Streamlit application  
- reports/ → generated visualizations and outputs  
- main.py → pipeline execution entry point  

---

## Data Pipeline

1. Data Loading  
2. Data Cleaning and Transformation  
3. Feature Engineering  
4. Data Export  
5. Analysis and Visualization  

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

<p align="center">
  <img src="reports/dashboard.png" width="800"/>
</p>

---

## Key Insights

- Electronics is the top-performing revenue category  
- Sales exhibit temporal variation, indicating possible seasonality  
- Revenue is highly concentrated in a small subset of products  
- High-value customers contribute significantly to total revenue  

---

## How to Run

### Install dependencies
pip install -r requirements.txt

### Run data pipeline
python main.py

### Run dashboard
streamlit run dashboard/app.py

---

## Dataset

Public dataset available at:
https://www.kaggle.com/datasets/marthadimgba/online-shop-2024

---

## Conclusion

This project demonstrates:

- End-to-end data analysis workflow  
- Data cleaning and transformation techniques  
- Business insight extraction  
- Data visualization and reporting  
- Interactive dashboard development  
