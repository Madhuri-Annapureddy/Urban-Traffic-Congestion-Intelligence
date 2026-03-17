    **Urban Traffic Congestion Intelligence System**
**Overview**

The Urban Traffic Congestion Intelligence System is an AI-powered dashboard designed to analyze, predict, and visualize traffic congestion across interstates. It leverages historical traffic data, weather, holidays, and time patterns to provide actionable insights and aid urban traffic management.

**Key Features**

Traffic Prediction Panel

Predict congestion for selected time, day, and month.

Input weather conditions (temperature, rain, snow, clouds).

Predict traffic volume with light, moderate, heavy congestion classification.

Daily Traffic Pattern Visualization

Area chart showing average traffic volume by hour.

Identify peak and low-traffic hours.

Traffic Congestion Heatmap

Hourly traffic volume across days of the week.

Color-coded for easy visualization.

Weekday vs Weekend Traffic Comparison

Line chart comparing average traffic patterns.

Highlights behavioral differences in traffic.

Peak Traffic Calendar

Heatmap showing average daily traffic for each month.

Categorizes days as Low, Medium, High congestion.

High-Risk Period Identification

Automatically identifies hours with traffic volume > 5000.

Weather & Holiday Impact Analysis

Understand how weather, holidays, and time patterns affect congestion.

Feature Importance Insights

Shows factors most correlated with congestion using correlation analysis.

**Dataset**

File: data/raw/traffic.csv

Columns used:

date_time – timestamp of traffic measurement

traffic_volume – number of vehicles

temp – temperature in Kelvin

rain_1h – rainfall in the last hour

snow_1h – snowfall in the last hour

clouds_all – cloud coverage (%)

holiday – 0 = no holiday, 1 = holiday

day – day of month

month – month number

hour – hour of day

is_weekend – 0 = weekday, 1 = weekend

**Tech Stack**
Layer	Technology / Library
Frontend / Dashboard	Streamlit
Data Processing	Pandas, NumPy
Visualization	Plotly Express, Plotly Graph Objects
Machine Learning	Scikit-learn (ML model & preprocessing scaler)
Model Storage	Pickle
Python Version	3.10+
Installation

**Clone the repository:**

git clone <your-repo-link>
cd traffic-ai-system

Create a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

**Install required packages:**

pip install -r requirements.txt

Run the Streamlit app:

streamlit run app/app.py
Usage

Open the dashboard in your browser.

Use the Traffic Prediction Panel to input:

Time of day, month, and day

Weather conditions

Holiday/Weekday information

Click Predict Traffic to view predictions:

Gauge for expected traffic volume

Insights for congestion level

Explore visualizations:

Daily traffic pattern

Traffic heatmap

Weekday vs weekend comparison

Peak traffic calendar

Review high-risk periods and feature importance insights for decision-making.

**Presentation Highlights**

Fully interactive dashboard for traffic analysis.

Real-time traffic prediction for any day and time.

Color-coded heatmaps and charts for easy understanding.

Automated identification of high-risk congestion hours.

Weather, holiday, and temporal patterns analysis.

Helps urban planners make data-driven decisions for traffic management.

**Future Enhancements**

Interactive calendar with clickable days to predict traffic.

Real-time traffic updates via live sensors or APIs.

Advanced feature importance visualization with SHAP values for explainable AI.

**Author**
Team NOVARE

Kondala Gnaneswar Reddy

Annapureddy Madhuri

Urban Traffic Congestion Intelligence System
