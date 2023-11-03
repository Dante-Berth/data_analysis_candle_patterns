from ta.volatility import *
from ta import trend
class fe_volatility:
    @staticmethod
    def boolinger_band(dataframe:pd.DataFrame,signal_name:str,window:int=20,window_dev:int=2):
        indicator_bb = ta.volatility.BollingerBands(close=dataframe[signal_name], window=window, window_dev=window_dev)
        dataframe.loc[:, f'{signal_name}_bbm'] = indicator_bb.bollinger_mavg()
        dataframe.loc[:, f'{signal_name}_bbh'] = indicator_bb.bollinger_hband()
        dataframe.loc[:, f'{signal_name}_bbl'] = indicator_bb.bollinger_lband()

        return None

    @staticmethod
    def average_true_range(dataframe:pd.DataFrame,high_name:str,low_name:str,close_name:str,window:int=14):
        dataframe.loc[:, f'{close_name}_atr'] = ta.volatility.average_true_range(high=dataframe[high_name],
                                                         low=dataframe[low_name],close=dataframe[close_name],
                                                         window=window)
        return None

    @staticmethod
    def keltner_channel(dataframe:pd.DataFrame,high_name:str,low_name:str,close_name:str,window:int=14,window_atr:int=20,multiplier:int=2):
        indicator_kc = ta.volatility.KeltnerChannel(high=dataframe[high_name],low=dataframe[low_name],close=dataframe[close_name],
                                                         window=window, window_atr=window_atr,multiplier=multiplier)
        dataframe.loc[:, f'{close_name}_kcm'] = indicator_kc.keltner_channel_mband()
        dataframe.loc[:, f'{close_name}_kch'] = indicator_kc.keltner_channel_hband()
        dataframe.loc[:, f'{close_name}_kcl'] = indicator_kc.keltner_channel_lband()
        return None

    @staticmethod
    def donchian_channel(dataframe:pd.DataFrame,high_name:str,low_name:str,close_name:str,window:int=14):
        indicator_dc = ta.volatility.DonchianChannel(high=dataframe[high_name],low=dataframe[low_name],close=dataframe[close_name],
                                                         window=window)
        dataframe.loc[:, f'{close_name}_dcm'] = indicator_dc.donchian_channel_mband()
        dataframe.loc[:, f'{close_name}_dch'] = indicator_dc.donchian_channel_hband()
        dataframe.loc[:, f'{close_name}_dcl'] = indicator_dc.donchian_channel_lband()

        return None

    @staticmethod
    def ulcer_index(close_name:str,window:int=14):
        dataframe.loc[:, f'{close_name}_ui'] = ta.volatility.ulcer_index(close=dataframe[close_name],window=window)
        return None


class fe_momentum:
    close_name = "close"
    high_name = "high"
    low_name = "low"
    @staticmethod
    def rsi(dataframe:pd.DataFrame, close_name:str,window: int = 14):
        dataframe[f"{close_name}_rsi"] = ta.momentum.RSIIndicator(dataframe[close_name], window).rsi()
        return None

    @staticmethod
    def tsi(dataframe:pd.DataFrame,close_name:str, window_slow: int = 25, window_fast: int = 13):
        dataframe[f"{close_name}_tsi"] = ta.momentum.TSIIndicator(dataframe[close_name], window_slow, window_fast).tsi()
        return None

    @staticmethod
    def ultimate_oscillator(dataframe:pd.DataFrame,high_name:str,low_name:str,close_name:str,
                            window1: int = 7, window2: int = 14, window3: int = 28,
                            weight1: float = 4.0, weight2: float = 2.0, weight3: float = 1.0):
        dataframe[f"{close_name}_ultimate_oscillator"] = ta.momentum.UltimateOscillator(dataframe[high_name], dataframe[low_name], dataframe[close_name], window1, window2, window3, weight1, weight2, weight3).ultimate_oscillator()
        return None

    @staticmethod
    def stochastic_oscillator(dataframe:pd.DataFrame,high_name:str,low_name:str, close_name:str, window: int = 14,
                              smooth_window: int = 3):
        dataframe[f"{close_name}_stochastic_oscillator"] = ta.momentum.StochasticOscillator(dataframe[high_name], dataframe[low_name], dataframe[close_name], window, smooth_window).stoch()
        return None

    @staticmethod
    def kama(dataframe:pd.DataFrame,close_name:str, window: int = 10, pow1: int = 2, pow2: int = 30):
        dataframe[f"{close_name}_kama_oscillator"] = ta.momentum.KAMAIndicator(dataframe[close_name], window, pow1, pow2).kama()
        return None

    @staticmethod
    def rate_of_change(dataframe:pd.DataFrame,close_name:str, window: int = 12):
        dataframe[f"{close_name}_rate_of_change"] = ta.momentum.ROCIndicator(dataframe[close_name], window).roc()
        return None

    @staticmethod
    def awesome_oscillator(dataframe:pd.DataFrame,high_name:str,low_name:str, window1: int = 5, window2: int = 34):
        dataframe[f"{high_name}_awesome_oscillator_indicator"] = ta.momentum.AwesomeOscillatorIndicator(dataframe[high_name], dataframe[low_name], window1, window2).awesome_oscillator()
        return None

    @staticmethod
    def williams_percent_r(dataframe:pd.DataFrame,high_name:str,low_name:str, close_name: str, lbp: int = 14):
        dataframe[f"{close_name}_williams_percent_r"] = ta.momentum.WilliamsRIndicator(dataframe[high_name], dataframe[low_name], dataframe[close_name], lbp).williams_r()
        return None

    @staticmethod
    def percentage_price_oscillator(dataframe: pd.DataFrame, close_name: str, window_slow: int = 26,
                           window_fast: int = 12, window_sign: int = 9,):
        dataframe[f"{close_name}_percentage_price_oscillator"] = \
            ta.momentum.PercentagePriceOscillator(close=dataframe[close_name],window_slow=window_slow,window_fast=window_fast,
    window_sign=window_sign).ppo_signal()
        return None
class fe_trend:
    @staticmethod
    def ccii(dataframe:pd.DataFrame,high_name:str,low_name:str,window:int = 20):
        dataframe[f"{high_name}_cci"] = ta.trend.CCIIndicator(dataframe[high_name],dataframe[low_name],window).cci()
        return None

    @staticmethod
    def adx(dataframe: pd.DataFrame, high_name: str, low_name: str,close_name:str, window:int = 14):
        dataframe[f"{close_name}_adx"] = ta.trend.ADXIndicator(dataframe[high_name],dataframe[low_name],dataframe[close_name],window).adx()
        return None

    @staticmethod
    def kst(dataframe: pd.DataFrame, close_name: str, roc1: int = 10, roc2: int = 15,\
        roc3: int = 20,  roc4: int = 30,  window1: int = 10,  window2: int = 10,window3: int = 10,\
        window4: int = 15, nsig: int = 9):
        dataframe[f"{close_name}_kst"] = ta.trend.KSTIndicator(dataframe[close_name],roc1, roc2,roc3,roc4,window1,window2,window3,\
        window4,nsig).kst()
        return None

    @staticmethod
    def mass(dataframe: pd.DataFrame, high_name:str, low_name:str, window_fast:int = 9, window_slow: int=25):
        dataframe[f"{high_name}_mass"] = ta.trend.MassIndex(dataframe[high_name],dataframe[low_name], window_fast, window_slow).mass_index()
        return  None

    @staticmethod
    def psar(dataframe: pd.DataFrame, high_name:str, low_name:str,  close_name:str,step: float = 0.02,
        max_step: float = 0.20):
        psar_indicator = ta.trend.PSARIndicator(dataframe[high_name],dataframe[low_name], dataframe[close_name], step, max_step)
        dataframe[f"{high_name}_psar"] = psar_indicator.psar()
        return None









