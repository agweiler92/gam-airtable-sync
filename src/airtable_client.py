from pyairtable import Api

from config import (
    AIRTABLE_PAT,
    AIRTABLE_BASE_ID,
    AIRTABLE_TABLE,
)

api = Api(AIRTABLE_PAT)

table = api.table(
    AIRTABLE_BASE_ID,
    AIRTABLE_TABLE,
)


def load_existing_orders():
    """
    Load all existing Airtable records keyed by GAM Order ID.
    """

    existing = {}

    print("Loading existing Airtable records...")

    records = table.all()

    print(f"Airtable returned {len(records)} total records.")

    for record in records:

        fields = record.get("fields", {})

        order_id = fields.get("GAM Order ID")

        if order_id:
            existing[str(order_id)] = record

    print(f"Loaded {len(existing)} records with a GAM Order ID.")

    return existing


def create_campaign(fields):
    """
    Create a new Airtable campaign.
    """

    table.create(fields)

    print(f"Created Order {fields['GAM Order ID']}")


def update_campaign(record_id, fields):
    """
    Update an existing Airtable campaign.
    """

    table.update(record_id, fields)

    print(f"Updated Order {fields['GAM Order ID']}")