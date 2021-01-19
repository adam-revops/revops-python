from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
from enum import Enum

class MetricResolution(str, Enum):
    MINUTE = "minute"
    HOUR = "hour"
    DAY = "day"
    MONTH = "month"
    YEAR = "year"

class UsageEventMode(str, Enum):
    INSERT = "insert"
    UPSERT = "upsert"

class EventMetricSchema(BaseModel):
    account_id: str
    sub_account_id: Optional[str]
    metadata: Optional[dict]
    metric_name: str
    metric_value: int
    metric_resolution: MetricResolution = MetricResolution.MONTH
    product:str
    date_submitted: datetime


class UsageEventSchema(BaseModel):
    date_submitted: datetime
    event_metrics: List[EventMetricSchema]
    mode: UsageEventMode = UsageEventMode.UPSERT
    transaction_id: str