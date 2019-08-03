import unittest
from revops.resources import (
    usage
)
from revops.exceptions import RequestSchemaException

class TestUsage(unittest.TestCase):
    def test_create_usage(self):
        dummy_api = object()
        metric = usage.UsageEvent(dummy_api)
        result = metric.create(
            transaction_id="test-transaction-id",
            event_metrics=[],
            mode="insert",
            date_submitted="2019-07-31T23:47:17.205481+00:00"
        )
        self.assertEqual(result.transaction_id, "test-transaction-id")
        self.assertEqual(result.id, None)
        self.assertEqual(result.event_metrics, [])
        self.assertEqual(result.mode, "insert")
        self.assertEqual(result.date_submitted, "2019-07-31T23:47:17.205481+00:00")

    def test_create_usage_invalid(self):
        dummy_api = object()
        metric = usage.UsageEvent(dummy_api)
        with self.assertRaises(RequestSchemaException):
            result = metric.create(
                transaction_id="test-transaction-id",
                event_metrics=[],
                mode="invalid-mode",
                date_submitted="2019-07-31T23:47:17.205481+00:00"
            )
