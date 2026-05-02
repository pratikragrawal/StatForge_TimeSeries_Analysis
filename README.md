# 📊 StatForge: Time-Series Analysis of Temperature & AQI Trends

## 📌 Overview
StatForge is a data analysis project that explores environmental patterns using statistical and time-series techniques.  
The project focuses on analyzing **Temperature**, **Air Quality Index (AQI)**, and **Humidity** data for Delhi over a 90-day period.

The goal is to extract meaningful insights such as trends, relationships, and anomalies using data-driven methods.

---

## 🎯 Objectives
- Analyze temperature and AQI data using statistical techniques  
- Identify trends using time-series analysis  
- Apply moving averages for smoothing fluctuations  
- Examine correlation between temperature and AQI  
- Detect anomalies using statistical methods  
- Visualize data for better interpretation  

---

## 🛠️ Technologies Used
- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  
- Statsmodels  

---

## 📂 Project Structure
StatForge_TimeSeries_Analysis/
│
├── CODE/
│ └── statforge_final.py
│
├── DATA/
│ └── delhi_climate.csv
│
├── OUTPUTS/
│ ├── temperature_trend.png
│ ├── moving_average.png
│ ├── heatmap.png
│ └── decomposition.png
│
├── REPORT/
│ └── StatForge_Report.pdf
│
├── PRESENTATION/
│ └── StatForge_Presentation.pptx
│
└── README.md

---

## 📊 Key Features
- Time-Series Analysis of environmental data  
- Moving Average for trend smoothing  
- Correlation Analysis (Temperature vs AQI)  
- Outlier Detection using Z-score  
- Rolling statistics and variability analysis  
- Data visualization using multiple graph types  
- Trend detection using regression  

---

## 📈 Results & Insights
- Temperature shows a gradual increasing trend over time  
- AQI decreases as temperature increases (inverse relationship)  
- Moving averages effectively smooth short-term fluctuations  
- Correlation analysis reveals a negative relationship between temperature and AQI  
- Outliers highlight unusual environmental conditions  

---

## ▶️ How to Run

### 1. Clone Repository
```bash
git clone https://github.com/your-username/StatForge_TimeSeries_Analysis.git
cd StatForge_TimeSeries_Analysis

2. Install Dependencies
pip install pandas numpy matplotlib seaborn statsmodels
3. Run the Script
python CODE/statforge_final.py
4. View Outputs

Graphs will be saved inside the OUTPUTS/ folder.

📌 Dataset
Contains 90 days of environmental data for Delhi
Includes:
Temperature (°C)
AQI
Humidity (%)
🔮 Future Enhancements
Extend dataset for long-term analysis
Implement machine learning models for prediction
Include additional environmental factors (wind, rainfall)
Perform multi-city comparison

👨‍💻 Author
Pratik Agrawal
