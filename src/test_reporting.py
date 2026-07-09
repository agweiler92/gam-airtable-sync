from reporting import get_order_reporting


print("Loading GAM reporting data...\n")

reporting = get_order_reporting()

print(
    f"Loaded reporting data for "
    f"{len(reporting)} orders.\n"
)

for order_id, data in list(
    reporting.items()
)[:10]:

    print("Order ID:", order_id)
    print("Site:", data["Site"])
    print(
        "Impressions:",
        data["Impressions"],
    )
    print("Clicks:", data["Clicks"])
    print("-" * 60)