# 🚀 Data Radar

**Data Radar** is an end-to-end data engineering project that collects, processes, and visualizes real-time job market data. It automates the pipeline from data extraction to insight generation, helping users explore hiring trends across companies and roles.

---

## 📌 Overview

The project scrapes job postings from multiple company career pages, cleans and transforms the data, and presents it through an interactive dashboard. It demonstrates a complete data pipeline using modern data engineering tools.

---

## ⚙️ Tech Stack

- Python – Core programming  
- Selenium – Web scraping  
- Pandas – Data cleaning & transformation  
- SQL (MySQL) – Data storage  
- Apache Airflow – Workflow orchestration  
- Streamlit – Dashboard visualization  

---

## 🔄 Data Pipeline Architecture

1. **Data Ingestion**
   - Scrapes job listings from company websites using Selenium  

2. **Data Processing**
   - Cleans, formats, and standardizes raw data using Pandas  

3. **Data Storage**
   - Stores processed data in a structured database  

4. **Workflow Automation**
   - Uses Airflow DAGs to schedule and manage pipelines  

5. **Data Visualization**
   - Interactive dashboard built with Streamlit  

---

## 📊 Features

- 🔍 Filter jobs by company, role, and keywords  
- 📈 Explore job market trends  
- ⏱️ Automated daily data updates using Airflow  
- 🧹 Clean and structured dataset for analysis  

---

## 📁 Project Structure

```
DataRadar/
│── dags/                # Airflow DAGs
│── scraper/             # Web scraping scripts
│── utils/               # Helper functions (DB, cleaning)
│── dashboard/           # Streamlit app
│── data/                # Stored datasets
│── requirements.txt
│── README.md
```

---

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/Avashpro/DataRadar.git
cd DataRadar
```

### 2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run scraper
```bash
python scraper/main.py
```

### 5. Run dashboard
```bash
streamlit run dashboard/app.py
```

---

## 📌 Future Improvements

- Add more company data sources  
- Deploy dashboard online (Streamlit Cloud / AWS)  
- Add real-time alerts for new job postings  
- Use APIs instead of scraping where possible  

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork and improve the project.

---

## 📬 Contact

**Avash Pradhan**  
- GitHub: https://github.com/Avashpro  

---

## ⭐ Why This Project Matters

This project demonstrates:
- End-to-end data pipeline development  
- Easier Job searching. 
- Automation and scheduling with Airflow  

