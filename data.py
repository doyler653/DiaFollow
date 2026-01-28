from supabase_client import supabase

def get_patients():
    resp = supabase.table("users").select("id, role").eq("role", "patient").execute()
    return resp.data

def get_glucose(patient_id, limit=50):
    resp = supabase.table("glucose_readings") \
        .select("value, recorded_at") \
        .eq("patient_id", patient_id) \
        .order("recorded_at", desc=True) \
        .limit(limit) \
        .execute()
    return resp.data

def get_insulin(patient_id, limit=50):
    resp = supabase.table("insulin_doses") \
        .select("dose, time") \
        .eq("patient_id", patient_id) \
        .order("time", desc=True) \
        .limit(limit) \
        .execute()
    return resp.data

def get_carbs(patient_id, limit=50):
    resp = supabase.table("carb_intake") \
        .select("grams, time") \
        .eq("patient_id", patient_id) \
        .order("time", desc=True) \
        .limit(limit) \
        .execute()
    return resp.data
