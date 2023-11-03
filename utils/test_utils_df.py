import unittest

import pandas as pd
from utils_df import *
class TestOpener_Dataframe(unittest.TestCase):
    def testOpener_Dataframe_zip(self):

        PATH = "../Data/ETHUSDT-5m.zip"
        df = opener_dataframe(PATH)
        self.assertEqual(type(df), pd.DataFrame)  # Check if the output is a Dataframe
        self.assertNotIn("Unnamed: 0", df.columns) # Check if Unnamed: 0 column was dropped

    def testOpener_Dataframe_pkl(self):
        PATH_2 = "../Data/binance-ETHUSDT-5m.pkl"
        df = opener_dataframe(PATH_2)
        self.assertEqual(type(df), pd.DataFrame)
        self.assertNotIn("Unnamed: 0",df.columns)

    def testOpener_Dataframe_csvzip(self):
        PATH_3 = "../Data/HARMONIA_V20.1-82-BACKTESTS_COMPLETE_2022-04-01--2023-05-05.csv.zip"
        df = opener_dataframe(PATH_3)
        self.assertEqual(type(df), pd.DataFrame)
        self.assertNotIn("Unnamed: 0", df.columns)
class TestFilter_Dataframe_By_Date_Range(unittest.TestCase):
    def testFilter_Dataframe(self):
        PATH_3 = "../Data/HARMONIA_V20.1-82-BACKTESTS_COMPLETE_2022-04-01--2023-05-05.csv.zip"
        df = opener_dataframe(PATH_3)
        new_df = filter_dataframe_by_date_range(df,begin_date="2022-08-02",end_date="2023-04-01")
        self.assertEqual(type(new_df), pd.DataFrame)



if __name__ == '__main__':
    unittest.main()