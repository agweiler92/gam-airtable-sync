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
    Load Airtable records that contain
    a GAM Order ID.

    Records are keyed by GAM Order ID
    so the sync can update existing
    records instead of creating duplicates.
    """

    existing = {}

    print(
        "Loading existing "
        "Airtable records..."
    )

    records = table.all()

    print(
        f"Airtable returned "
        f"{len(records)} total records."
    )

    for record in records:

        fields = record.get(
            "fields",
            {},
        )

        order_id = fields.get(
            "GAM Order ID"
        )

        if order_id:

            existing[
                str(order_id)
            ] = record

    print(
        f"Loaded {len(existing)} "
        f"records with a GAM Order ID."
    )

    return existing


def create_campaign(fields):

    table.create(fields)

    print(
        f"Created Order "
        f"{fields['GAM Order ID']}"
    )


def update_campaign(
    record_id,
    fields,
):

    table.update(
        record_id,
        fields,
    )

    print(
        f"Updated Order "
        f"{fields['GAM Order ID']}"
    )