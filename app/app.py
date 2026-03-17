import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import pickle
import numpy as np

from ui.theme import load_theme

st.set_page_config(page_title="Traffic Intelligence System", layout="wide")
load_theme()

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------
st.markdown("""
<div class='title'>Urban Traffic Congestion Intelligence</div>
<div class='subtitle'>AI Powered Smart City Traffic Dashboard</div>
""", unsafe_allow_html=True)

st.markdown("""
This system analyzes historical interstate traffic data to understand how traffic congestion evolves throughout the day.
The model studies weather conditions, calendar patterns and holidays to estimate expected traffic volume.
""")

# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------
df = pd.read_csv("data/raw/traffic.csv")
df["date_time"] = pd.to_datetime(df["date_time"])
df["hour"] = df["date_time"].dt.hour
df["day_name"] = df["date_time"].dt.day_name()
df["day"] = df["date_time"].dt.day       # <-- add this
df["month"] = df["date_time"].dt.month   # <-- add this
df["is_weekend"] = df["day_name"].isin(["Saturday","Sunday"]).astype(int)
# Convert holiday to numeric (0 = no holiday, 1 = holiday)
df['holiday'] = df['holiday'].apply(lambda x: 0 if pd.isna(x) or x==0 else 1)
# ---------------------------------------------------
# LOAD MODEL
# ---------------------------------------------------
model = pickle.load(open("models/traffic_model.pkl","rb"))
scaler = pickle.load(open("models/scaler.pkl","rb"))

# ---------------------------------------------------
# INPUT PANEL
# ---------------------------------------------------
st.markdown("<div class='section'>Traffic Prediction Panel</div>", unsafe_allow_html=True)
st.markdown("<div class='card'>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

time_options = {
"12 AM":0,"1 AM":1,"2 AM":2,"3 AM":3,"4 AM":4,"5 AM":5,
"6 AM":6,"7 AM":7,"8 AM":8,"9 AM":9,"10 AM":10,"11 AM":11,
"12 PM":12,"1 PM":13,"2 PM":14,"3 PM":15,"4 PM":16,
"5 PM":17,"6 PM":18,"7 PM":19,"8 PM":20,"9 PM":21,
"10 PM":22,"11 PM":23
}

month_map = {
"January":1,"February":2,"March":3,"April":4,
"May":5,"June":6,"July":7,"August":8,
"September":9,"October":10,"November":11,"December":12
}

with col1:
    time_label = st.selectbox("Time of Day", list(time_options.keys()))
    hour = time_options[time_label]
    temp = st.number_input("Temperature (Kelvin)",250,330,290)
    holiday = st.selectbox("Holiday",[0,1])

with col2:
    rain = st.number_input("Rain in last hour",0.0)
    snow = st.number_input("Snow in last hour",0.0)
    clouds = st.slider("Cloud Coverage %",0,100,40)

with col3:
    selected_month = st.selectbox("Month", list(month_map.keys()))
    month = month_map[selected_month]
    day = st.slider("Day of Month",1,31,15)
    weekend = st.selectbox("Day Type",["Weekday","Weekend"])
    is_weekend = 1 if weekend == "Weekend" else 0

weather_main_options = {
"Clear":0,"Clouds":1,"Rain":2,"Snow":3,"Mist":4,"Fog":5,"Haze":6,"Thunderstorm":7,"Drizzle":8
}

weather_desc_options = {
"clear sky":0,"few clouds":1,"scattered clouds":2,"broken clouds":3,"overcast clouds":4,
"light rain":5,"moderate rain":6,"heavy rain":7,"snow":8,"mist":9
}

selected_weather_main = st.selectbox("Weather Condition", list(weather_main_options.keys()))
selected_weather_desc = st.selectbox("Weather Description", list(weather_desc_options.keys()))

predict = st.button("🚀 Predict Traffic")
st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------
# PREDICTION
# ---------------------------------------------------
if predict:
    input_data = pd.DataFrame({
        "temp":[temp],
        "rain_1h":[rain],
        "snow_1h":[snow],
        "clouds_all":[clouds],
        "hour":[hour],
        "holiday":[holiday],
        "weather_main":[weather_main_options[selected_weather_main]],
        "weather_description":[weather_desc_options[selected_weather_desc]],
        "day":[day],
        "month":[month],
        "is_weekend":[is_weekend]
    })

    input_data = input_data[scaler.feature_names_in_]
    scaled = scaler.transform(input_data)
    prediction = model.predict(scaled)[0]
    predicted_vehicles = int(prediction)

    col1, col2 = st.columns(2)

    # SPEEDOMETER
    with col1:
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=predicted_vehicles,
            title={'text':"Traffic Congestion Meter"},
            gauge={'axis':{'range':[0,8000]},
                   'steps':[{'range':[0,2500],'color':"green"},
                            {'range':[2500,5000],'color':"yellow"},
                            {'range':[5000,8000],'color':"red"}]}
        ))
        st.plotly_chart(fig,use_container_width=True)

    # INSIGHT
    with col2:
        st.subheader("Traffic Prediction Insight")
        st.write(f"Expected vehicles on road: **{predicted_vehicles} vehicles**")
        if predicted_vehicles < 2500:
            st.success("Traffic is light with smooth flow.")
        elif predicted_vehicles < 5000:
            st.warning("Moderate traffic congestion expected.")
        else:
            st.error("High traffic congestion predicted.")

# ---------------------------------------------------
# DAILY TRAFFIC PATTERN
# ---------------------------------------------------
st.markdown("<div class='section'>Daily Traffic Pattern</div>", unsafe_allow_html=True)
hourly = df.groupby("hour")["traffic_volume"].mean().reset_index()
fig = px.area(hourly,x="hour",y="traffic_volume",
title="Traffic Volume Variation Throughout the Day")
st.plotly_chart(fig,use_container_width=True)

# ---------------------------------------------------
# HEATMAP
# ---------------------------------------------------
st.markdown("<div class='section'>Traffic Congestion Heatmap</div>", unsafe_allow_html=True)
heat = df.pivot_table(
values="traffic_volume",
index="hour",
columns="day_name",
aggfunc="mean"
)
fig = px.imshow(
heat,
color_continuous_scale="Turbo",
labels=dict(x="Day",y="Hour",color="Traffic"),
aspect="auto"
)
st.plotly_chart(fig,use_container_width=True)

# ---------------------------------------------------
# WEEKDAY VS WEEKEND COMPARISON
# ---------------------------------------------------
st.markdown("<div class='section'>Weekday vs Weekend Traffic Patterns</div>", unsafe_allow_html=True)
weekday = df[df['is_weekend']==0].groupby('hour')['traffic_volume'].mean().reset_index()
weekend = df[df['is_weekend']==1].groupby('hour')['traffic_volume'].mean().reset_index()
fig = go.Figure()
fig.add_trace(go.Scatter(x=weekday['hour'], y=weekday['traffic_volume'], mode='lines+markers', name='Weekday'))
fig.add_trace(go.Scatter(x=weekend['hour'], y=weekend['traffic_volume'], mode='lines+markers', name='Weekend'))
fig.update_layout(title='Weekday vs Weekend Traffic Comparison', xaxis_title='Hour', yaxis_title='Traffic Volume')
st.plotly_chart(fig,use_container_width=True)

# ---------------------------------------------------
# PEAK TRAFFIC CALENDAR
# ---------------------------------------------------
st.markdown("<div class='section'>Peak Traffic Calendar</div>", unsafe_allow_html=True)
calendar_peak = df.groupby(['month','day'])['traffic_volume'].mean().reset_index()
calendar_peak['congestion_level'] = pd.cut(calendar_peak['traffic_volume'], bins=[0,2500,5000,10000], labels=['Low','Medium','High'])
fig = px.density_heatmap(calendar_peak, x='day', y='month', z='traffic_volume', color_continuous_scale='Turbo', labels={'x':'Day','y':'Month','z':'Avg Traffic'})
st.plotly_chart(fig,use_container_width=True)
calendar_peak = df.groupby(['month','day'])['traffic_volume'].mean().reset_index()
correlations = df[['traffic_volume','temp','rain_1h','snow_1h','clouds_all','hour','holiday','month','is_weekend']].corr()
# ---------------------------------------------------
# AUTOMATED HIGH-RISK PERIODS
# ---------------------------------------------------
st.markdown("<div class='section'>High-Risk Congestion Periods</div>", unsafe_allow_html=True)
hourly_avg = df.groupby('hour')['traffic_volume'].mean()
high_risk_hours = hourly_avg[hourly_avg>5000].index.tolist()
st.write(f"High-risk congestion hours (avg traffic > 5000 vehicles): {high_risk_hours}")

# ---------------------------------------------------
# FEATURE IMPORTANCE INSIGHT (approx using correlation)
# ---------------------------------------------------
st.markdown("<div class='section'>Factors Contributing Most to Congestion</div>", unsafe_allow_html=True)
correlations = df[['traffic_volume','temp','rain_1h','snow_1h','clouds_all','hour','holiday','month','is_weekend']].corr()
feature_corr = correlations['traffic_volume'].drop('traffic_volume').sort_values(key=abs, ascending=False)
st.write(feature_corr)