from pyairtable import Api
from config import AIRTABLE_PAT, AIRTABLE_BASE_ID

api = Api(AIRTABLE_PAT)
base = api.base(AIRTABLE_BASE_ID)

schema = base.schema()

for table in schema.tables:
    print(f"\nTable: {table.name}")
    print("-" * 40)

    for field in table.fields:
        print(field.name)