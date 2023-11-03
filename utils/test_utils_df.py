import unittest

import pandas as pd
from utils_df import *
class TestOpener_Dataframe(unittest.TestCase):

    def testOpener_Dataframe_pkl(self):
        PATH_2 = "../Data/binance-ETHUSDT-5m.pkl"
        df = opener_dataframe(PATH_2)
        self.assertEqual(type(df), pd.DataFrame)
        self.assertNotIn("Unnamed: 0",df.columns)



if __name__ == '__main__':
    unittest.main()