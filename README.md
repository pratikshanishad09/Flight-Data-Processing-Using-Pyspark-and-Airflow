# ✈️ Flight Data Processing using PySpark & Airflow

This project is an end-to-end **Data Engineering Pipeline** built for processing flight booking data using **PySpark**, storing it in **Delta Lake**, and orchestrating the entire workflow using **Apache Airflow** (running via Docker).

---

## 🚀 Project Overview

**Objective:**  
To build a data pipeline that:
- Ingests raw flight booking data (CSV format)
- Cleans and transforms it using PySpark
- Saves the output as a Delta Lake table
- Automates the process with Apache Airflow

---

## 🛠️ Tech Stack

| Tool           | Purpose                         |
|----------------|----------------------------------|
| **PySpark**    | Data processing & transformations |
| **Delta Lake** | Data storage in ACID format      |
| **Apache Airflow** | Workflow orchestration        |
| **Docker**     | Containerized environment         |
| **Pandas**     | Data preview & local operations   |

---

## 📂 Folder Structure

Flight-Data-Pipeline/

│

├── dags/

│ └── flight_etl_pipeline.py # Airflow DAG file

├── data/

│ └── clean_flight_data.csv # Cleaned sample data (optional)

├── docker-compose.yml # Docker setup for Airflow

├── requirements.txt # (Optional) Python package list

├── README.md # Project overview

└── .gitignore # Git ignore rules


---

## ⚙️ Pipeline Flow

1. **Data Source**: Raw CSV file with flight bookings  
2. **PySpark Script**:
   - Reads raw data
   - Cleans & transforms records
   - Writes output as a Delta Lake table
3. **Airflow DAG**:
   - Runs the PySpark script as a task
   - Automates the pipeline on schedule or demand

---

## 🔄 How to Run the Project

### 1. 🐳 Start Airflow (Docker)
```bash
docker compose up airflow-init
docker compose up
'''

###2. 🌐 Access Airflow UI

Open http://localhost:8080
Login (default):
Username: airflow
Password: airflow

###3. ✅ Enable and Trigger DAG

Turn on the flight_etl_pipeline DAG
Trigger it manually or wait for schedule

##📝 Future Enhancements

Add logging & data quality checks
Store processed data in cloud (AWS/GCP/Azure)
Add alerting via email/Slack on DAG failure



