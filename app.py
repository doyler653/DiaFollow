import streamlit as st
import pandas as pd
from supabase_client import supabase

st.set_page_config(page_title="DiaCare Connect", layout="wide")

st.title("DiaCare Connect Dashboard")

# Select a patient (example)
patients = supabase.table("users").select("id, role").eq("role", "patient").execute()
patient_list = [(p['id'], p['id']) for p in patients.data]

selected_patient = st.selectbox("Select Patient", patient_list, format_func=lambda x: x[1])

if selected_patient:
    # Fetch glucose readings
    data = supabase.table("glucose_readings") \
        .select("*") \
        .eq("patient_id", selected_patient) \
        .order("recorded_at", desc=True) \
        .limit(50) \
        .execute()

    if data.data:
        df = pd.DataFrame(data.data)
        df['recorded_at'] = pd.to_datetime(df['recorded_at'])
        st.subheader("Latest Glucose Readings")
        st.line_chart(df.set_index('recorded_at')['value'])
    else:
        st.info("No glucose data available.")
