# 🚀 Superstore Data Engineering Pipeline (Spark + HDFS)

## 📌 Project Overview
This project implements a complete Data Engineering pipeline using Apache Spark and Hadoop HDFS following the Medallion Architecture (Bronze → Silver → Gold).

---

## 🏗️ Architecture

### 🟤 Bronze Layer
- Raw data ingestion (CSV → HDFS)
- No transformations applied

### ⚪ Silver Layer
- Data cleaning and type casting
- Date parsing (Order Date, Ship Date)
- Stored as Parquet in HDFS

### 🟡 Gold Layer
- Aggregated business metrics
- Example: Total Sales by Region

---

## ⚙️ Technologies Used
- Apache Spark 3.5.0
- Hadoop HDFS
- Python (PySpark)
- Docker & Docker Compose
- Linux (WSL2)

---

## 📊 Example Output (Gold Layer)

| Region  | Total Sales |
|---------|-------------|
| West    | 713471      |
| East    | 672194      |
| Central | 497800      |
| South   | 388983      |

---

## 🧪 How to Run

### 1. Start cluster
```bash
docker compose up -d# superstore-data-engineering
