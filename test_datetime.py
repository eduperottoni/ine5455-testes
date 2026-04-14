import unittest
import datetime


class TestDatetime(unittest.TestCase):

    def test_datetime_creation_with_valid_params(self):
        # Fixture setup
        # Exercise SUT
        dt = datetime.datetime(2023, 10, 1, 12, 0, 0)
        # Result verification
        self.assertEqual(dt.year, 2023)
        self.assertEqual(dt.month, 10)
        self.assertEqual(dt.day, 1)
        self.assertEqual(dt.hour, 12)
        self.assertEqual(dt.minute, 0)
        self.assertEqual(dt.second, 0)
        # Teardown

    def test_datetime_creation_with_invalid_month(self):
        # Fixture setup
        # Exercise SUT and Result verification
        with self.assertRaises(ValueError):
            datetime.datetime(2023, 13, 1, 12, 0, 0)
        # Teardown

    def test_datetime_creation_with_invalid_day(self):
        # Fixture setup
        # Exercise SUT and Result verification
        with self.assertRaises(ValueError):
            datetime.datetime(2023, 10, 32, 12, 0, 0)
        # Teardown

    def test_datetime_creation_with_invalid_hour(self):
        # Fixture setup
        # Exercise SUT and Result verification
        with self.assertRaises(ValueError):
            datetime.datetime(2023, 10, 1, 24, 0, 0)
        # Teardown

    def test_datetime_creation_with_invalid_minute(self):
        # Fixture setup
        # Exercise SUT and Result verification
        with self.assertRaises(ValueError):
            datetime.datetime(2023, 10, 1, 12, 60, 0)
        # Teardown

    def test_datetime_creation_with_invalid_second(self):
        # Fixture setup
        # Exercise SUT and Result verification
        with self.assertRaises(ValueError):
            datetime.datetime(2023, 10, 1, 12, 0, 60)
        # Teardown

    def test_datetime_creation_with_date_and_without_time(self):
        # Fixture setup
        # Exercise SUT
        dt = datetime.datetime(2023, 10, 1)
        # Result verification
        self.assertEqual(dt.year, 2023)
        self.assertEqual(dt.month, 10)
        self.assertEqual(dt.day, 1)
        self.assertEqual(dt.hour, 0)
        self.assertEqual(dt.minute, 0)
        self.assertEqual(dt.second, 0)
        # Teardown

    def test_datetime_less_than_comparison_with_different_dates(self):
        # Fixture setup
        dt1 = datetime.datetime(2023, 10, 1, 12, 0, 0)
        dt2 = datetime.datetime(2023, 10, 2, 12, 0, 0)
        # Exercise SUT
        result = dt1 < dt2
        # Result verification
        self.assertTrue(result)
        # Teardown

    def test_datetime_greater_than_comparison_with_different_dates(self):
        # Fixture setup
        dt1 = datetime.datetime(2023, 10, 1, 12, 0, 0)
        dt2 = datetime.datetime(2023, 10, 2, 12, 0, 0)
        # Exercise SUT
        result = dt1 > dt2
        # Result verification
        self.assertFalse(result)
        # Teardown

    def test_datetime_equality_comparison_with_different_dates(self):
        # Fixture setup
        dt1 = datetime.datetime(2023, 10, 1, 12, 0, 0)
        dt2 = datetime.datetime(2023, 10, 2, 12, 0, 0)
        # Exercise SUT
        result = dt1 == dt2
        # Result verification
        self.assertFalse(result)
        # Teardown

    def test_datetime_inequality_comparison_with_different_dates(self):
        # Fixture setup
        dt1 = datetime.datetime(2023, 10, 1, 12, 0, 0)
        dt2 = datetime.datetime(2023, 10, 2, 12, 0, 0)
        # Exercise SUT
        result = dt1 != dt2
        # Result verification
        self.assertTrue(result)
        # Teardown

    def test_datetime_less_than_comparison_with_same_dates(self):
        # Fixture setup
        dt1 = datetime.datetime(2023, 10, 1, 12, 0, 0)
        dt2 = datetime.datetime(2023, 10, 1, 12, 0, 0)
        # Exercise SUT
        result = dt1 < dt2
        # Result verification
        self.assertFalse(result)
        # Teardown

    def test_datetime_greater_than_comparison_with_same_dates(self):
        # Fixture setup
        dt1 = datetime.datetime(2023, 10, 1, 12, 0, 0)
        dt2 = datetime.datetime(2023, 10, 1, 12, 0, 0)
        # Exercise SUT
        result = dt1 > dt2
        # Result verification
        self.assertFalse(result)
        # Teardown

    def test_datetime_equality_comparison_with_same_dates(self):
        # Fixture setup
        dt1 = datetime.datetime(2023, 10, 1, 12, 0, 0)
        dt2 = datetime.datetime(2023, 10, 1, 12, 0, 0)
        # Exercise SUT
        result = dt1 == dt2
        # Result verification
        self.assertTrue(result)
        # Teardown

    def test_datetime_inequality_comparison_with_same_dates(self):
        # Fixture setup
        dt1 = datetime.datetime(2023, 10, 1, 12, 0, 0)
        dt2 = datetime.datetime(2023, 10, 1, 12, 0, 0)
        # Exercise SUT
        result = dt1 != dt2
        # Result verification
        self.assertFalse(result)
        # Teardown

    def test_datetime_arithmetic_hours(self):
        # Fixture setup
        dt = datetime.datetime(2023, 10, 1, 12, 0, 0)
        delta = datetime.timedelta(hours=1)
        # Exercise SUT
        new_dt = dt + delta
        # Result verification
        self.assertEqual(new_dt.year, 2023)
        self.assertEqual(new_dt.month, 10)
        self.assertEqual(new_dt.day, 1)
        self.assertEqual(new_dt.hour, 13)
        self.assertEqual(new_dt.minute, 0)
        self.assertEqual(new_dt.second, 0)
        # Teardown

    def test_datetime_arithmetic_days(self):
        # Fixture setup
        dt = datetime.datetime(2023, 10, 1, 12, 0, 0)
        delta = datetime.timedelta(days=1)
        # Exercise SUT
        new_dt = dt + delta
        # Result verification
        self.assertEqual(new_dt.year, 2023)
        self.assertEqual(new_dt.month, 10)
        self.assertEqual(new_dt.day, 2)
        self.assertEqual(new_dt.hour, 12)
        self.assertEqual(new_dt.minute, 0)
        self.assertEqual(new_dt.second, 0)
        # Teardown

    def test_datetime_arithmetic_days_and_hours(self):
        # Fixture setup
        dt = datetime.datetime(2023, 10, 1, 12, 0, 0)
        delta = datetime.timedelta(days=1, hours=2)
        # Exercise SUT
        new_dt = dt + delta
        # Result verification
        self.assertEqual(new_dt.year, 2023)
        self.assertEqual(new_dt.month, 10)
        self.assertEqual(new_dt.day, 2)
        self.assertEqual(new_dt.hour, 14)
        self.assertEqual(new_dt.minute, 0)
        self.assertEqual(new_dt.second, 0)
        # Teardown

    def test_datetime_arithmetic_negative_hours(self):
        # Fixture setup
        dt = datetime.datetime(2023, 10, 1, 12, 0, 0)
        delta = datetime.timedelta(hours=-1)
        # Exercise SUT
        new_dt = dt + delta
        # Result verification
        self.assertEqual(new_dt.year, 2023)
        self.assertEqual(new_dt.month, 10)
        self.assertEqual(new_dt.day, 1)
        self.assertEqual(new_dt.hour, 11)
        self.assertEqual(new_dt.minute, 0)
        self.assertEqual(new_dt.second, 0)
        # Teardown

    def test_datetime_arithmetic_negative_days_and_hours(self):
        # Fixture setup
        dt = datetime.datetime(2023, 10, 1, 12, 0, 0)
        delta = datetime.timedelta(days=-1, hours=-2)
        # Exercise SUT
        new_dt = dt + delta
        # Result verification
        self.assertEqual(new_dt.year, 2023)
        self.assertEqual(new_dt.month, 9)
        self.assertEqual(new_dt.day, 30)
        self.assertEqual(new_dt.hour, 10)
        self.assertEqual(new_dt.minute, 0)
        self.assertEqual(new_dt.second, 0)
        # Teardown

    def test_datetime_arithmetic_changes_day_when_removing_hours(self):
        # Fixture setup
        dt = datetime.datetime(2023, 10, 1, 12, 0, 0)
        delta = datetime.timedelta(days=-1, hours=-13)
        # Exercise SUT
        new_dt = dt + delta
        # Result verification
        self.assertEqual(new_dt.year, 2023)
        self.assertEqual(new_dt.month, 9)
        self.assertEqual(new_dt.day, 29)
        self.assertEqual(new_dt.hour, 23)
        self.assertEqual(new_dt.minute, 0)
        self.assertEqual(new_dt.second, 0)
        # Teardown

    def test_time_creation(self):
        # Fixture setup
        # Exercise SUT
        t = datetime.time(hour=1, minute=2, second=3, microsecond=4)
        # Result verification
        self.assertEqual(t.hour, 1)
        self.assertEqual(t.minute, 2)
        self.assertEqual(t.second, 3)
        self.assertEqual(t.microsecond, 4)
        # Teardown

    def test_time_creation_with_invalid_hour(self):
        # Fixture setup
        # Exercise SUT
        with self.assertRaises(ValueError):
            datetime.time(hour=24, minute=2, second=3, microsecond=4)
        # Result verification
        # Teardown

    def test_datetime_combine_datetime_and_time(self):
        # Fixture setup
        dt = datetime.datetime(2023, 10, 1, 12, 0, 0)
        t = datetime.time(hour=2, minute=2, second=1)
        # Exercise SUT
        new_dt = datetime.datetime.combine(dt, t)
        # Result verification
        self.assertEqual(new_dt.year, 2023)
        self.assertEqual(new_dt.month, 10)
        self.assertEqual(new_dt.day, 1)
        self.assertEqual(new_dt.hour, 2)
        self.assertEqual(new_dt.minute, 2)
        self.assertEqual(new_dt.second, 1)
        # Teardown

    def test_datetime_replace_hour_on_datetime(self):
        # Fixture setup
        dt = datetime.datetime(2023, 10, 1, 12, 0, 0)
        # Exercise SUT
        new_dt = dt.replace(hour=2)
        # Result verification
        self.assertEqual(new_dt.year, 2023)
        self.assertEqual(new_dt.month, 10)
        self.assertEqual(new_dt.day, 1)
        self.assertEqual(new_dt.hour, 2)
        self.assertEqual(new_dt.minute, 0)
        self.assertEqual(new_dt.second, 0)
        # Teardown

    def test_datetime_replace_with_invalid_hour(self):
        # Fixture setup
        dt = datetime.datetime(2023, 10, 1, 12, 0, 0)
        # Exercise SUT
        with self.assertRaises(ValueError):
            dt.replace(hour=24)
        # Result verification
        # Teardown

    def test_datetime_tz(self):
        # Fixture setup
        delta = datetime.timedelta(hours=12)
        # Exercise SUT
        dt = datetime.timezone(delta, "algum tz")
        # Result verification
        self.assertEqual(dt.tzname(None), "algum tz")
        self.assertEqual(dt.utcoffset(None), delta)
        # Teardown

    def test_transform_datetime_to_timestamp(self):
        # Fixture setup
        dt = datetime.datetime(2023, 10, 1, 12, 0, 0)
        # Exercise SUT
        timestamp = dt.timestamp()
        # Result verification
        self.assertEqual(timestamp, 1696172400.0)
        # Teardown

    def test_convert_datetime_to_string(self):
        # Fixture setup
        dt = datetime.datetime(2023, 10, 1, 12, 0, 0)
        # Exercise SUT
        dt_str = dt.isoformat()
        # Result verification
        self.assertEqual(dt_str, "2023-10-01T12:00:00")
        # Teardown

    def test_convert_string_to_datetime(self):
        # Fixture setup
        dt_str = "2023-10-01T12:00:00"
        # Exercise SUT
        dt = datetime.datetime.fromisoformat(dt_str)
        # Result verification
        self.assertEqual(dt.year, 2023)
        self.assertEqual(dt.month, 10)
        self.assertEqual(dt.day, 1)
        self.assertEqual(dt.hour, 12)
        self.assertEqual(dt.minute, 0)
        self.assertEqual(dt.second, 0)
        # Teardown

    def test_datetime_strftime(self):
        # Fixture setup
        dt = datetime.datetime(2023, 10, 1, 12, 0, 0)
        # Exercise SUT
        dt_str = dt.strftime("%Y-%m-%d %H:%M:%S")
        # Result verification
        self.assertEqual(dt_str, "2023-10-01 12:00:00")
        # Teardown


if __name__ == "__main__":
    unittest.main()
