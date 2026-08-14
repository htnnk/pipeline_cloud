An end-to-end Python data Pipeline that automatically collects hourly stock market prices, stores it in a cloud infrastructure, and presents it through an interactive dashboard on Power BI. The process to collect the data automatically uses GitHub Actions workflow

This is a simple project that takes the data provided by the Yahoo Finance API ('yfinance') and uses that data to analyze the stocks (ITUB3.SA, PETR3.SA, VALE3.SA and ^BVSP) hourly.

## Build With
* **Python 3** (Pandas, yfinance, sqlalchemy, psycopg2-binary)
* **Supabase** (Cloud infrasruture to store the filtered data)
* **GitHub Actions** (Automation: automate the fetching data)
* **Power BI** (BI Visualization & Reporting)

## How to clone the repository:
git clone https://github.com/htnnk/pipeline_cloud.git

## Install dependencies:
pip install -r requirements.txt

## Run the Data Pipeline:

python part1.py

## Disclaimer:

This project was created only for educational purposes, without any profit purpose
* The financial data was collected by the Yahoo Finance API
* This software should not be used as a real investment operation
* The developer doesnt have any ties with the data source and doesn't guarantee the accuracy or continue availability of the data returned by the API
