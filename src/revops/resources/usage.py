from typing import List, Optional
from revops.resources import APIResource
from revops.schema import EventMetricSchema, MetricResolution, UsageEventMode, UsageEventSchema
from revops.exceptions import RequestSchemaException

from marshmallow import Schema, fields
from datetime import datetime, timezone

class UsageEvent(APIResource):
    _resource = "v1/usage/events"
    _metrics = []
       
    id = None
    date_submitted = None
    event_metrics = []
    mode = None
    usage_event_id = None
    transaction_id = None

    def add_metric(self, 
        account_id: str, 
        metric_name: str, 
        metric_value: int, 
        product: str, 
        metric_resolution: Optional[MetricResolution] = MetricResolution.MONTH, 
        date_submitted: Optional[datetime] = None,
        sub_account_id: Optional[str] = "",
        metadata: Optional[dict] = {}
        ):

        if date_submitted is None:
            date_submitted = datetime.now()

        self.event_metrics.append(
            EventMetricSchema(
                account_id=account_id, 
                sub_account_id=sub_account_id,
                metric_name=metric_name, 
                metric_value=metric_value, 
                metric_resolution=metric_resolution,
                product=product, 
                date_submitted=date_submitted,
                metadata=metadata
            )
        )

    def create(self, 
            transaction_id: str,
            event_metrics: Optional[List[EventMetricSchema]] = None,
            date_submitted: Optional[datetime] = None,
            mode: Optional[UsageEventMode]= UsageEventMode.UPSERT
        ):

        if date_submitted is None:
            date_submitted = datetime.now()

        if event_metrics is not None:
            self.event_metrics.extend(
                event_metrics
            )
 

        event = UsageEventSchema(
            date_submitted=datetime.now(), 
            event_metrics=self.event_metrics, 
            transaction_id=transaction_id,
            mode=mode,
        )

        return self.request(
            data=event.json(),
            http_method = "POST"
        )

"""
Defines the records module
revops.usage.records.<action>
"""
class __api_module__(object):

    def __init__(self, api):
        self._api = api

    @property
    def events(self):
        return UsageEvent(self._api)
