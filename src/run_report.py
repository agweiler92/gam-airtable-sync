import time

from google.ads import admanager_v1


REPORT_NAME = "networks/5391017/reports/7931651252"

client = admanager_v1.ReportServiceClient()

print("Starting report...")

operation = client.run_report(
    request={
        "name": REPORT_NAME
    }
)

print("Waiting for report to finish...")

result = operation.result(timeout=300)

print("\nReport finished!")
print(result)
