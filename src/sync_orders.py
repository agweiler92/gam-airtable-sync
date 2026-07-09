from datetime import datetime, timezone

from orders import list_orders
from companies import get_advertiser_name
from reporting import get_order_reporting

from airtable_client import (
    load_existing_orders,
    create_campaign,
    update_campaign,
)


CUTOFF_DATE = datetime(
    2026,
    1,
    1,
    tzinfo=timezone.utc,
)


def sync_orders():

    # Load records that already have a GAM Order ID.
    # On the first sync, this may correctly return zero.

    existing = load_existing_orders()

    print(
        "Loading Google Ad Manager "
        "reporting data..."
    )

    reporting = get_order_reporting()

    print(
        f"Loaded reporting data for "
        f"{len(reporting)} orders."
    )

    orders = list_orders()

    print(
        f"Found {len(orders)} "
        f"Google Ad Manager orders."
    )

    for order in orders:

        # Skip archived GAM orders.

        if order.archived:
            continue

        # Skip GAM orders beginning before
        # January 1, 2026.

        if order.start_time < CUTOFF_DATE:
            continue

        print(
            f"Syncing Order "
            f"{order.order_id}: "
            f"{order.display_name}"
        )

        order_id = str(
            order.order_id
        )

        # Look up the actual advertiser
        # company name in GAM.

        advertiser_name = (
            get_advertiser_name(
                order.advertiser
            )
        )

        # Use blank/zero values when an order
        # has not yet recorded delivery.

        report_data = reporting.get(
            order_id,
            {
                "Site": [],
                "Impressions": 0,
                "Clicks": 0,
            },
        )

        record = {

    "Advertiser": (
        advertiser_name
    ),

    "Order Name": (
        order.display_name
    ),

    "Placement": ["Rotational Media"],

    "GAM Order ID": (
        order_id
    ),

            "Date": (
                order.start_time.strftime(
                    "%Y-%m-%d"
                )
            ),

            "End date": (
                order.end_time.strftime(
                    "%Y-%m-%d"
                )
            ),

            "Campaign Link": (
                "https://"
                "admanager.google.com/"
                "5391017"
                "#delivery/orders/"
                f"{order_id}"
            ),

            # Site is a list because the Airtable
            # Site field is a multiple-select field.

            "Site": (
                report_data["Site"]
            ),

            "Impressions": (
                report_data[
                    "Impressions"
                ]
            ),

            "Total Clicks": (
                report_data[
                    "Clicks"
                ]
            ),
        }

        # Update a GAM-synced record if its
        # GAM Order ID already exists.
        # Otherwise, create a new record.

        if order_id in existing:

            update_campaign(
                existing[
                    order_id
                ]["id"],
                record,
            )

        else:

            create_campaign(
                record
            )

    print(
        "\nSync complete."
    )