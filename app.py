import streamlit as st
import pandas as pd
from data import get_patients, get_glucose, get_insulin, get_carbs
from models import df_from_records
from auth import login

st.set_page_config(page_title="DiaCare Connect", layout="wide")
st.title("DiaCare Connect Dashboard")

# --- Authentication ---
viewer_id = login()
if not viewer_id:
    st.stop()

# --- Patient selection ---
patients = get_patients()
if not patients:
    st.warning("No patients found in the database.")
    st.stop()

patient_options = [(p['id'], p['id']) for p in patients]
selected_patient = st.selectbox("Select Patient", patient_options, format_func=lambda x: x[1])

# --- Glucose readings ---
glucose_data = get_glucose(selected_patient)
df_glucose = df_from_records(glucose_data, time_col="recorded_at")

if not df_glucose.empty:
    st.subheader("Glucose Readings")
    st.line_chart(df_glucose.set_index('recorded_at')['value'])
else:
    st.info("No glucose data available.")

# --- Insulin doses ---
insulin_data = get_insulin(selected_patient)
df_insulin = df_from_records(insulin_data, time_col="time")

if not df_insulin.empty:
    st.subheader("Insulin Doses")
    st.line_chart(df_insulin.set_index('time')['dose'])
else:
    st.info("No insulin data available.")

# --- Carb intake ---
carb_data = get_carbs(selected_patient)
df_carbs = df_from_records(carb_data, time_col="time")

if not df_carbs.empty:
    st.subheader("Carbohydrate Intake")
    st.line_chart(df_carbs.set_index('time')['grams'])
else:
    st.info("No carb data available.")

# --- Alerts (example) ---
if not df_glucose.empty and (df_glucose['value'].iloc[-1] < 4.0 or df_glucose['value'].iloc[-1] > 10.0):
    st.warning(f"Critical glucose reading: {df_glucose['value'].iloc[-1]} mmol/L")
