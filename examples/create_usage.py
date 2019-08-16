
from revops.api import RevOpsAPI

api = RevOpsAPI()

record_request = api.usage.events.create(
    transaction_id = "batch-1",
    mode = "insert",
)

record_request.add_metric(
    account_id = "test123",
    product = "my-product",
    metric_name = "nam",
    metric_value = 102,
    metric_resolution = "hour",
)

record_request.add_metric(
    account_id = "test456",
    product = "my-product",
    metric_name = "nam1",
    metric_value = 100,
    metric_resolution = "hour",
)

usage_record = record_request.commit()
print(usage_record.transaction_id)
print("Created {}: {}".format(usage_record.id, usage_record.date_submitted))
print("\tMode: {}".format(usage_record.mode))
response = usage_record.delete()
