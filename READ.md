# Salesforce → Databricks-Style Data Pipeline Simulation

## 📊 Project Overview
This project simulates a data pipeline that extracts sales data from an API, transforms it using PySpark (Databricks-style), and loads the results into Power BI–ready Excel and Parquet formats.  
The goal is to demonstrate experience with **ETL, Databricks workflows, PySpark, and Delta Lake concepts**.

---

## 🔹 Workflow
1. **Extract**  
   - Load sales data from a mock API / JSON file.  

2. **Transform** (Databricks Simulation with PySpark)  
   - Clean missing values  
   - Aggregate sales by customer and month  
   - Save results in Parquet (Delta-style format)  

3. **Load**  
   - Export cleaned dataset into Excel for Power BI dashboarding  

---

## 🛠️ Tech Used
- Python (pandas, requests, openpyxl)  
- PySpark (for Databricks-like transformations)  
- Parquet files (simulate Delta Lake storage)  
- Power BI (connects to exported Excel dataset)  

---

## 📂 Project Structure

azure-databricks-pipeline-simulation/
│── notebooks/
│ └── sales_pipeline_notebook.py # PySpark ETL notebook
│── data/
│ └── raw_sales.json # Mock input data
│── outputs/
│ ├── cleaned_sales.parquet
│ └── sales_summary.xlsx
│── pipeline.py # End-to-end Python runner
│── README.md # Documentation


---

## 🚀 Next Steps
- Replace mock API with **Salesforce REST API** or Azure SQL  
- Deploy PySpark notebook in **Azure Databricks**  
- Schedule job execution with **Databricks Jobs / Azure Data Factory**  
- Secure credentials using **Azure Key Vault**  

---

## 🔑 Key Skills Demonstrated
✅ ETL Pipeline Design  
✅ Databricks Notebook Workflow  
✅ PySpark Transformations  
✅ Delta Lake Simulation (Parquet)  
✅ Power BI Export & Automation  