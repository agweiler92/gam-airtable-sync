from pyairtable import Api
from config import AIRTABLE_PAT, AIRTABLE_BASE_ID, AIRTABLE_TABLE

api = Api(AIRTABLE_PAT)
table = api.table(AIRTABLE_BASE_ID, AIRTABLE_TABLE)


def load_existing_orders():
    """
    Load all existing Airtable records keyed by GAM Order ID.
    """
    existing = {}

    print("Loading existing Airtable records...")

    for record in table.all():
        fields = record.get("fields", {})

        order_id = fields.get("GAM Order ID")

        if order_id:
            existing[str(order_id)] = record

    print(f"Loaded {len(existing)} existing records.")

    return existing


def create_campaign(fields):
    table.create(fields)
    print(f"Created Order {fields['GAM Order ID']}")


def update_campaign(record_id, fields):
    table.update(record_id, fields)
    print(f"Updated Order {fields['GAM Order ID']}")