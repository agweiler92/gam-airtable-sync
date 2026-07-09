from google.ads import admanager_v1

NETWORK_CODE = "5391017"

client = admanager_v1.ReportServiceClient()

Dimension = admanager_v1.ReportDefinition.Dimension
Metric = admanager_v1.ReportDefinition.Metric
ReportType = admanager_v1.ReportDefinition.ReportType

report = admanager_v1.Report(
    display_name="GAM Airtable Test Report",
    report_definition=admanager_v1.ReportDefinition(
        dimensions=[
            Dimension.ORDER_ID,
            Dimension.ORDER_NAME,
            Dimension.PLACEMENT_NAME,
            Dimension.AD_UNIT_NAME_TOP_LEVEL,
        ],
        metrics=[
            Metric.IMPRESSIONS,
            Metric.CLICKS,
        ],
        date_range={
            "fixed": {
                "start_date": {
                    "year": 2026,
                    "month": 1,
                    "day": 1,
                },
                "end_date": {
                    "year": 2026,
                    "month": 12,
                    "day": 31,
                },
            }
        },
        report_type=ReportType.HISTORICAL,
    ),
)

request = admanager_v1.CreateReportRequest(
    parent=f"networks/{NETWORK_CODE}",
    report=report,
)

created_report = client.create_report(request=request)

print("Report created successfully!")
print("Report resource:", created_report.name)
print(created_report)
