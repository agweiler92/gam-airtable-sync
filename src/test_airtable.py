from pyairtable import Api
from config import AIRTABLE_PAT, AIRTABLE_BASE_ID, AIRTABLE_TABLE

print("Connecting to Airtable...")

api = Api(AIRTABLE_PAT)
table = api.table(AIRTABLE_BASE_ID, AIRTABLE_TABLE)

records = table.all(max_records=1)

print("✅ Connected successfully!")
print(f"Found {len(records)} existing record(s).")

if records:
    print(records[0]["fields"])