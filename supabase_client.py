import os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("https://zrvgyamfvblqgyecbtmg.supabase.co")
SUPABASE_KEY = os.getenv("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inpydmd5YW1mdmJscWd5ZWNidG1nIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjE3Mjc1MjYsImV4cCI6MjA3NzMwMzUyNn0.w77xGc5-lHSfjcshPaRw2n9-GUCO-4OjyGAvRCC-joc")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
