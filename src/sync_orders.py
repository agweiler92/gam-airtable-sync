from datetime import datetime, timezone

from orders import list_orders
from airtable_client import (
    load_existing_orders,
    create_campaign,
    update_campaign,
)

CUTOFF_DATE = datetime(2026, 1, 1, tzinfo=timezone.utc)


def sync_orders():

    orders = list_orders()
    existing = load_existing_orders()

    print(f"Found {len(orders)} Google Ad Manager orders.")

    for order in orders:

        # Skip archived orders
        if order.archived:
            continue

        # Skip campaigns that started before 2026
        if order.start_time < CUTOFF_DATE:
            continue

        print(f"Syncing Order {order.order_id}: {order.display_name}")

        order_id = str(order.order_id)

        record = {
    "Advertiser": order.display_name,   # Temporary (we'll replace this with the real advertiser name later)
    "Order Name": order.display_name,
    "GAM Order ID": order_id,
    "Date": order.start_time.strftime("%Y-%m-%d"),
    "End date": order.end_time.strftime("%Y-%m-%d"),
    "Campaign Link": f"https://admanager.google.com/5391017#delivery/orders/{order_id}",
}

        if order_id in existing:
            update_campaign(existing[order_id]["id"], record)
        else:
            create_campaign(record)

    print("Sync complete.")