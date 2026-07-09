from collections import defaultdict

from google.ads import admanager_v1


# Saved GAM report definition
REPORT_NAME = (
    "networks/5391017/reports/7931651252"
)


def get_order_reporting():

    client = (
        admanager_v1.ReportServiceClient()
    )

    print(
        "Running fresh Google Ad Manager "
        "delivery report..."
    )

    # Run the saved report again so impressions
    # and clicks are current.

    operation = client.run_report(
        request={
            "name": REPORT_NAME
        }
    )

    print(
        "Waiting for GAM report "
        "to finish..."
    )

    # Wait up to five minutes.

    result = operation.result(
        timeout=300
    )

    # GAM returns a new report-result resource
    # each time the saved report is run.

    report_result = (
        result.report_result
    )

    print(
        "GAM report finished."
    )

    print(
        "Loading report rows..."
    )

    order_data = defaultdict(
        lambda: {
            "sites": set(),
            "impressions": 0,
            "clicks": 0,
        }
    )

    page_token = ""

    while True:

        request = (
            admanager_v1
            .FetchReportResultRowsRequest(
                name=report_result,
                page_token=page_token,
                page_size=1000,
            )
        )

        response = (
            client.fetch_report_result_rows(
                request=request
            )
        )

        for row in response.rows:

            # Dimensions:
            #
            # 0 = Order ID
            # 1 = Order Name
            # 2 = Placement Name
            # 3 = Top-Level Ad Unit

            order_id = str(
                row.dimension_values[
                    0
                ].int_value
            )

            placement_name = (
                row.dimension_values[
                    2
                ].string_value
            )

            # Metrics:
            #
            # 0 = Impressions
            # 1 = Clicks

            impressions = (
                row
                .metric_value_groups[0]
                .primary_values[0]
                .int_value
            )

            clicks = (
                row
                .metric_value_groups[0]
                .primary_values[1]
                .int_value
            )

            # Save only the three Cityside
            # publication placement names.

            if placement_name in {
                "Berkeleyside",
                "The Oaklandside",
                "Richmondside",
            }:

                order_data[
                    order_id
                ]["sites"].add(
                    placement_name
                )

            # Count delivery from every report
            # row, including rows with blank
            # placement names.

            order_data[
                order_id
            ]["impressions"] += (
                impressions
            )

            order_data[
                order_id
            ]["clicks"] += (
                clicks
            )

        page_token = (
            response.next_page_token
        )

        if not page_token:
            break

    results = {}

    for order_id, data in (
        order_data.items()
    ):

        results[order_id] = {

            # Airtable Site is a
            # multiple-select field.

            "Site": sorted(
                data["sites"]
            ),

            "Impressions": (
                data["impressions"]
            ),

            "Clicks": (
                data["clicks"]
            ),
        }

    print(
        f"Aggregated reporting data "
        f"for {len(results)} orders."
    )

    return results