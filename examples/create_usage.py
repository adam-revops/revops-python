
from revops.api import RevOpsAPI

api = RevOpsAPI()

# Add metrics you want to track for billing purposes
api.usage.events.add_metric(
    account_id='revops-io', 
    metric_name='active-dolls', # The second part to a product metric "dolly-platform.active-dolls"
    metric_value=100, 
    metric_resolution = "hour", # Track and aggregate the usage every hour, month, day, year.
    product='dolly-platform', # The product name from "dolly-platform.active-dolls"
)
response = api.usage.events.create(
    transaction_id='1234', # idempotency key
    mode="insert" # insert or upsert the data in the usage database
)

try:
    print(response)
except Exception as e:
    print("Unable to persist usage event.")
    print(e)
