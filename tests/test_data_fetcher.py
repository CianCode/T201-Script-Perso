import unittest
from unittest.mock import patch, mock_open
from src.data_manager import CustomFetcher

class TestCustomFetcher(unittest.TestCase):
    def setUp(self):
        self.fetcher = CustomFetcher()

    @patch("os.listdir", return_value=["file_1.csv"])
    @patch("builtins.open", new_callable=mock_open, read_data="Product ID,Company,Origin,Category,Stock,Unit Price\n1,ABC,USA,Tech,100,10.5")
    def test_get_data(self, mock_open_file, mock_listdir):
        data = self.fetcher.get_data()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["Company"], "ABC")

    def test_match_filters(self):
        row = {"Stock": "50"}
        filters = [("Stock", ">", "40")]
        result = self.fetcher.match_filters(row, filters)
        self.assertTrue(result)

    def test_generate_summary(self):
        data = [{"Stock": "50", "Unit Price": "10.5"}, {"Stock": "100", "Unit Price": "20.5"}]
        summary = self.fetcher.generate_summary(data)
        self.assertEqual(summary["Stock"]["sum"], 150)
        self.assertEqual(summary["Unit Price"]["average"], 15.5)

if __name__ == "__main__":
    unittest.main()
