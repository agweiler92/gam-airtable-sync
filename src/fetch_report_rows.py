from google.ads import admanager_v1


REPORT_RESULT = (
    "networks/5391017/reports/7931651252/results/10233585709"
)

client = admanager_v1.ReportServiceClient()

request = admanager_v1.FetchReportResultRowsRequest(
    name=REPORT_RESULT,
)

print("Fetching report rows...\n")

response = client.fetch_report_result_rows(request=request)

print(response)