from google.ads import admanager_v1


def list_orders():

    client = admanager_v1.OrderServiceClient()

    request = admanager_v1.ListOrdersRequest(
        parent="networks/5391017"
    )

    response = client.list_orders(request=request)

    return list(response)