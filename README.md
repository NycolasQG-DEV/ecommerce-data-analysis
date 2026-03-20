# Ecommerce Data Analysis

## Overview
End-to-end e-commerce data analysis project, transforming raw data into business insights and an interactive dashboard.

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
- dashboard/ → interactive app  
- reports/ → visual outputs  
- main.py → execution pipeline  

---

## Data Pipeline

1. Data Loading  
2. Data Transformation  
3. Feature Engineering  
4. Data Export  
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

<p align="center">
  <img src="reports/dashboard.png" width="800"/>
</p>

---

## Key Insights

- Electronics is the leading revenue category  
- Sales show temporal variation (possible seasonality)  
- Revenue is concentrated in a small number of products  
- High-value customers drive a significant portion of revenue  

---

## How to Run

Install dependencies:
    pip install -r requirements.txt

Run pipeline:
    python main.py

Run dashboard:
    streamlit run dashboard/app.py

---

## Dataset

https://www.kaggle.com/datasets/marthadimgba/online-shop-2024

---

## Conclusion

This project demonstrates:
- Data analysis and transformation  
- Business insight generation  
- Data visualization  
- Dashboard development  
