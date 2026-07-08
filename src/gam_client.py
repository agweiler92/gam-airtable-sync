from google.ads import admanager_v1
from config import NETWORK_CODE


def get_network():
    client = admanager_v1.NetworkServiceClient()

    request = admanager_v1.GetNetworkRequest(
        name=f"networks/{NETWORK_CODE}"
    )

    response = client.get_network(request=request)

    return response