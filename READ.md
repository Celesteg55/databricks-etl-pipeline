# 🚀 Azure Databricks Pipeline Simulation

This project simulates a **data engineering workflow in Azure Databricks**, showcasing how raw sales data can be ingested, cleaned, transformed, and delivered to multiple destinations (Excel + Power BI).  

It demonstrates how to migrate a **Jupyter Notebook/Pandas pipeline** into a **PySpark + Databricks-ready workflow** with automation and documentation in mind.

---

## 📂 Project Structure

azure-databricks-pipeline-simulation/
│── notebooks/
│ └── sales_pipeline_notebook.py # PySpark ETL notebook
│── data/
│ └── raw_sales.json # Mock input data
│── outputs/
│ ├── cleaned_sales.parquet # Delta Lake-style storage
│ └── sales_summary.xlsx # Business-friendly report
│── pipeline.py # End-to-end Python runner
│── README.md # Documentation


---

## ⚙️ Workflow Overview
1. **Ingestion**  
   - Mock sales data (`raw_sales.json`) simulates data from Salesforce/Excel/SQL.  

2. **Transformation (PySpark)**  
   - Clean & validate sales records  
   - Aggregate metrics (total sales, average order value, etc.)  
   - Save processed data in **Parquet (Delta Lake style)**  

3. **Delivery**  
   - Export final report to **Excel (`sales_summary.xlsx`)**  
   - Ready for **Power BI dashboards**  

---

## 🔑 Skills Demonstrated
- **Databricks Workflow Simulation** (notebooks + jobs)  
- **ETL Pipeline Design** (extract → transform → load)  
- **PySpark Transformations** (scalable vs. Pandas)  
- **Delta Lake Simulation** using Parquet  
- **Excel + Power BI Integration** for reporting  
- **Documentation & Best Practices**  

---

## 🚀 Next Steps (if deploying to real Azure)
- Replace mock JSON with **Salesforce API** or **Azure SQL**  
- Deploy PySpark notebook in **Azure Databricks**  
- Automate pipeline with **Databricks Jobs / Azure Data Factory**  
- Secure credentials with **Azure Key Vault**  

---

## 📖 How to Run Locally
1. Clone the repo  
   ```bash
   git clone https://github.com/Celesteg55/azure-databricks-pipeline-simulation.git
   cd azure-databricks-pipeline-simulation

2. Install dependencies

pip install pyspark pandas openpyxl

3. Run pipeline 

python pipeline.py

4. Outputs will be generated in the outputs/folder.

---