import unittest
from datetime import datetime


#check if stock symbol is valid
def valid_symbol(symbol):
    return (
        isinstance(symbol, str)
        and 1 <= len(symbol) <= 7
        and symbol.isalpha()
        and symbol.isupper()
    )


#check if chart type is valid
def valid_chart_type(chart_type):
    return chart_type in ["1", "2"]


#check if time series is valid
def valid_time_series(time_series):
    return time_series in ["1", "2", "3", "4"]


#check if start date is valid
def valid_start_date(start_date):
    try:
        datetime.strptime(start_date, "%Y-%m-%d")
        return (
            len(start_date) == 10
            and start_date == datetime.strptime(
                start_date, "%Y-%m-%d"
            ).strftime("%Y-%m-%d")
        )
    except (ValueError, TypeError):
        return False


#check if end date is valid
def valid_end_date(end_date):
    try:
        datetime.strptime(end_date, "%Y-%m-%d")
        return (
            len(end_date) == 10
            and end_date == datetime.strptime(
                end_date, "%Y-%m-%d"
            ).strftime("%Y-%m-%d")
        )
    except (ValueError, TypeError):
        return False


#unit tests
class TestStockVisualizer(unittest.TestCase):

    #test stock symbols
    def test_symbol(self):
        self.assertTrue(valid_symbol("AAPL"))
        self.assertTrue(valid_symbol("GOOGL"))
        self.assertFalse(valid_symbol("apple"))
        self.assertFalse(valid_symbol("123"))
        self.assertFalse(valid_symbol("TOOLONGSYMBOL"))
        self.assertFalse(valid_symbol(""))

    #test chart types
    def test_chart_type(self):
        self.assertTrue(valid_chart_type("1"))
        self.assertTrue(valid_chart_type("2"))
        self.assertFalse(valid_chart_type("3"))
        self.assertFalse(valid_chart_type("bar"))
        self.assertFalse(valid_chart_type(""))

    #test time series
    def test_time_series(self):
        self.assertTrue(valid_time_series("1"))
        self.assertTrue(valid_time_series("2"))
        self.assertTrue(valid_time_series("3"))
        self.assertTrue(valid_time_series("4"))
        self.assertFalse(valid_time_series("5"))
        self.assertFalse(valid_time_series("0"))
        self.assertFalse(valid_time_series("daily"))

    #test start dates
    def test_start_date(self):
        self.assertTrue(valid_start_date("2026-11-18"))
        self.assertTrue(valid_start_date("2020-01-01"))
        self.assertFalse(valid_start_date("11-18-2026"))
        self.assertFalse(valid_start_date("2026-13-18"))
        self.assertFalse(valid_start_date("2026-02-30"))
        self.assertFalse(valid_start_date(""))

    #test end dates
    def test_end_date(self):
        self.assertTrue(valid_end_date("2026-11-18"))
        self.assertTrue(valid_end_date("2020-01-01"))
        self.assertFalse(valid_end_date("11-18-2026"))
        self.assertFalse(valid_end_date("2026-13-18"))
        self.assertFalse(valid_end_date("2026-02-30"))
        self.assertFalse(valid_end_date(""))


#run the unit tests
if __name__ == "__main__":
    unittest.main()
