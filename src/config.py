from dotenv import load_dotenv
import os

load_dotenv()

# Google Ad Manager
NETWORK_CODE = os.getenv("GAM_NETWORK_CODE")

# Airtable
AIRTABLE_PAT = os.getenv("AIRTABLE_PAT")
AIRTABLE_BASE_ID = os.getenv("AIRTABLE_BASE_ID")
AIRTABLE_TABLE = os.getenv("AIRTABLE_TABLE")