from google.ads import admanager_v1


client = admanager_v1.CompanyServiceClient()


def get_advertiser_name(advertiser_resource):
    """
    Converts:
    networks/5391017/companies/11825617

    into:
    Actual Advertiser Name
    """

    if not advertiser_resource:
        return ""

    company = client.get_company(
        request={
            "name": advertiser_resource
        }
    )

    return company.display_name