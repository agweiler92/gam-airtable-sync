from google.ads import admanager_v1

NETWORK_CODE = "5391017"
ORDER_ID = "4124286128"

client = admanager_v1.LineItemServiceClient()

request = admanager_v1.ListLineItemsRequest(
    parent=f"networks/{NETWORK_CODE}",
    filter=f'order = "networks/{NETWORK_CODE}/orders/{ORDER_ID}"',
)

print(f"Loading line items for Order {ORDER_ID}...\n")

response = client.list_line_items(request=request)

count = 0

for line_item in response:
    count += 1

    print("Line item:", line_item.display_name)
    print("Order:", line_item.order)
    print("Resource:", line_item.name)
    print("Custom fields:", line_item.custom_field_values)
    print("-" * 80)

print(f"\nFound {count} line item(s).")