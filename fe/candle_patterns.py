import pandas as pd
class idle_patterns:
    def __init__(self, dataframe, ohlc=None):
        super(idle_patterns, self).__init__()
        if ohlc is None:
            ohlc = {"close_name": "close",
                    "open_name": "open_price",
                    "high_name": "high",
                    "low_name": "low"}
        self.ohlc = ohlc
        self.dataframe = dataframe
        self.close = self.dataframe[self.ohlc["close_name"]]
        self.open = self.dataframe[self.ohlc["open_name"]]
        self.high = self.dataframe[self.ohlc["high_name"]]
        self.low = self.dataframe[self.ohlc["low_name"]]


    def bearich_breakaway(self,shift:int=1):
        # First candle a tall white candle
        prev_prev_prev_prev_open = self.open.shift(4 * shift)
        prev_prev_prev_prev_close = self.close.shift(4 * shift)
        # Second candle a white candle and candle opens above the previous opening price
        prev_prev_prev_open = self.open.shift(3 * shift)
        prev_prev_prev_close = self.close.shift(3 * shift)


    def bearich_engulfing(self,shift:int=1):

        prev_close = self.close.shift(shift)
        prev_open = self.open.shift(shift)

        self.dataframe[self.ohlc["close_name"] + "_bearich_engulfing"] = (self.open.ge(prev_close) & prev_close.gt(prev_open) &
                    self.open.gt(self.close) & prev_open.ge(self.close) & (self.open - self.close).gt(prev_close - prev_open))
        return None


    def bearich_harami(self,shift:int=1):
        prev_close = self.close.shift(shift)
        prev_open = self.open.shift(shift)


        self.dataframe[self.ohlc["close_name"] + "_bearich_harami"] = ( prev_close.gt(prev_open) &
                                                                        prev_close.ge(self.open) &
                                                                        self.open.gt(self.close) &
                                                                        self.close.ge(prev_open) &
                                                                        (prev_close-prev_open).gt(self.open-self.close)
                                                                        )
        return None

    def bullish_engulfing(self,shift:int=1):

        prev_close = self.close.shift(shift)
        prev_open = self.open.shift(shift)

        self.dataframe[self.ohlc["close_name"] + "_bullish_engulfing"] = (self.close.ge(prev_open) & prev_open.gt(prev_close) &
                    self.close.gt(self.open) & prev_close.ge(self.open) & (self.close - self.open).gt(prev_open - prev_close))
        return None


    def bullish_harami(self,shift:int=1):
        prev_close = self.close.shift(shift)
        prev_open = self.open.shift(shift)

        self.dataframe[self.ohlc["close_name"] + "_bullish_harami"] = ( prev_open.gt(prev_close) &
                                                                        prev_open.ge(self.close) &
                                                                        self.close.gt(self.open) &
                                                                        self.open.ge(prev_close) &
                                                                        (prev_open - prev_close).gt(self.close-self.open)
                                                                        )
        return None
    def dark_cloud_cover(self,shift:int=1):
        prev_close = self.close.shift(shift)
        prev_open = self.open.shift(shift)

        self.dataframe[self.ohlc["close_name"] + '_dark_cloud_cover'] = (prev_close.gt(prev_open) &
                                                                         ((prev_close + prev_open) / 2).gt(self.close) &
                                                                         self.open.gt(self.close) &
                                                                         self.open.gt(prev_close) &
                                                                         self.close.gt(prev_open) &
                                                                         ((self.open - self.close)/(0.001+ (self.high-self.low))).gt(0.6)
                                                                        )
        return None
    def doji(self):
        abs_close_minus_open = (self.close - self.open).abs()
        self.dataframe[self.ohlc["close_name"] + '_doji'] = ( (abs_close_minus_open/(self.high-self.low)).lt(0.1) &
                                                              (self.high-self.open.combine(self.close, max)).gt(3*abs_close_minus_open) &
                                                              (self.open.combine(self.close, min)-self.low).gt(3*abs_close_minus_open))


        return None

    def doji_star(self,shift:int=1):

        prev_close = self.close.shift(shift)
        prev_open = self.open.shift(shift)
        prev_high = self.high.shift(shift)
        prev_low = self.low.shift(shift)
        abs_close_minus_open = (self.close - self.open).abs()
        self.dataframe[self.ohlc["close_name"] + '_doji_star'] = (prev_close.gt(prev_open) &
                                                                  ((prev_close - prev_open).abs() / (prev_high - prev_low)).ge(0.7) &
                                                                  (abs_close_minus_open/(self.high-self.low)).lt(0.1) &
                                                                  prev_close.lt(self.close) &
                                                                  prev_close.lt(self.open) &
                                                                  (self.high-self.close.combine(self.open,max)).gt(3*abs_close_minus_open) &
                                                                  (self.close.combine(self.open, min)-self.low ).gt(
                                                                      3 * abs_close_minus_open)
                                                                  )
        return None
    def dragonfly_doji(self):

        abs_close_minus_open = abs(self.close - self.open)

        self.dataframe[self.ohlc["close_name"]+"_dragonfly_doji"] = (
            (abs_close_minus_open / (self.high - self.low)).lt(0.1) &
            ((self.close.combine(self.open, min) - self.low).gt(3 * abs_close_minus_open)) &
            ((self.high - self.close.combine(self.open, max)).lt(abs_close_minus_open))
        )
        return None

    def evening_star(self,shift:int=1):

        prev_close = self.close.shift(shift)
        prev_open = self.open.shift(shift)


        prev_prev_close = prev_close.shift(shift)
        prev_prev_open = prev_open.shift(shift)


        self.dataframe[self.ohlc["close_name"] + "_evening_star"] = (
            prev_open.combine(prev_close,min).gt(prev_prev_close) &
            prev_prev_close.gt(prev_prev_open) &
            self.close.lt(self.open) &
            self.open.lt(prev_open.combine(prev_close,min))
        )
        return None

    def evening_star_doji(self, shift: int = 1):

        prev_close = self.close.shift(shift)
        prev_open = self.open.shift(shift)
        prev_high = self.high.shift(shift)
        prev_low = self.low.shift(shift)



        prev_prev_close = prev_close.shift(shift)
        prev_prev_open = prev_open.shift(shift)
        prev_prev_high = prev_high.shift(shift)
        prev_prev_low = prev_low.shift(shift)

        abs_close_minus_open = (self.close - self.open).abs()
        abs_prev_close_minus_open = (prev_close - prev_open).abs()
        abs_prev_prev_close_minus_open = (prev_prev_close - prev_prev_open).abs()

        self.dataframe[self.ohlc["close_name"] + "_evening_star_doji"] = (
                prev_prev_close.gt(prev_prev_open) &
                (abs_prev_prev_close_minus_open / (prev_prev_high - prev_prev_low)).ge(0.7) &
                (abs_prev_close_minus_open / (prev_high - prev_low)).lt(0.1) &
                self.close.lt(self.open) &
                (abs_close_minus_open / (self.high - self.low)).ge(0.7) &
                prev_prev_close.lt(prev_close) &
                prev_prev_close.lt(prev_open) &
                prev_close.gt(self.open) &
                prev_open.gt(self.open) &
                self.close.lt(prev_prev_close) &
                (prev_high - prev_close.combine(prev_open,max)).gt(3 * abs_prev_close_minus_open) &
                (prev_close.combine(prev_open,min) - prev_low).gt(3 * abs_prev_close_minus_open)
        )
        return None

    def gravestone_doji(self):
        abs_close_minus_open = (self.close-self.open).abs()
        self.dataframe[self.ohlc["close_name"] + "_gravestone_doji"] = ((abs_close_minus_open/(self.high-self.low)).lt(0.1) &
                                                                         (self.high-self.close.combine(self.open,max)).gt(3*abs_close_minus_open) &
                                                                         (self.close.combine(self.open,min)-self.low).le(abs_close_minus_open)
        )
        return None
    def hammer(self):
        high_minus_low = self.high-self.low
        self.dataframe[self.ohlc["close_name"] + "_hammer"] = ( high_minus_low.gt(3*(self.open-self.close)) &
                                                                ((self.close-self.low)/(0.001+high_minus_low)).gt(0.6) &
                                                                ((self.open - self.low) / (0.001 + high_minus_low)).gt(
                                                                    0.6)
        )
        return None
    def hanging_man(self, shift: int = 1):
        prev_high = self.high.shift(shift)
        prev_prev_high = prev_high.shift(shift)
        high_minus_low = self.high - self.low
        self.dataframe[self.ohlc["close_name"] + "_hanging_man"] = (high_minus_low.gt(4*(self.open-self.close)) &
                                                                ((self.close-self.low)/(0.001+high_minus_low)).ge(0.75) &
                                                                ((self.open - self.low) / (0.001 + high_minus_low)).ge(
                                                                    0.75) &
                                                                self.open.gt(prev_high) &
                                                                self.open.gt(prev_prev_high)
                                                                       )
        return None

    def inverted_hammer(self):
        high_minus_low = self.high - self.low
        self.dataframe[self.ohlc["close_name"] + "_inverted_hammer"] = (high_minus_low.gt(3 * (self.open - self.close)) &
                                                               ((self.high - self.close) / (0.001 + high_minus_low)).gt(
                                                                   0.6) &
                                                               ((self.high - self.open) / (0.001 + high_minus_low)).gt(
                                                                   0.6)
                                                               )
        return None
    def morning_star(self,shift:int=1):

        prev_close = self.close.shift(shift)
        prev_open = self.open.shift(shift)


        prev_prev_close = prev_close.shift(shift)
        prev_prev_open = prev_open.shift(shift)


        self.dataframe[self.ohlc["close_name"] + "_morning_star"] = (
            prev_open.combine(prev_close,max).lt(prev_prev_close) &
            prev_prev_close.lt(prev_prev_open) &
            self.close.gt(self.open) &
            self.open.gt(prev_open.combine(prev_close,max))
        )
        return None

    def morning_star_doji(self, shift: int = 1):

        prev_close = self.close.shift(shift)
        prev_open = self.open.shift(shift)
        prev_high = self.high.shift(shift)
        prev_low = self.low.shift(shift)

        prev_prev_close = prev_close.shift(shift)
        prev_prev_open = prev_open.shift(shift)
        prev_prev_high = prev_high.shift(shift)
        prev_prev_low = prev_low.shift(shift)

        abs_close_minus_open = (self.close - self.open).abs()
        abs_prev_close_minus_open = (prev_close - prev_open).abs()
        abs_prev_prev_close_minus_open = (prev_prev_close - prev_prev_open).abs()

        self.dataframe[self.ohlc["close_name"] + "_morning_star_doji"] = (
                prev_prev_close.lt(prev_prev_open) &
                (abs_prev_prev_close_minus_open / (prev_prev_high - prev_prev_low)).ge(0.7) &
                (abs_prev_close_minus_open / (prev_high - prev_low)).lt(0.1) &
                self.close.gt(self.open) &
                (abs_close_minus_open / (self.high - self.low)).ge(0.7) &
                prev_prev_close.gt(prev_close) &
                prev_prev_close.gt(prev_open) &
                prev_close.lt(self.open) &
                prev_open.lt(self.open) &
                self.close.gt(prev_prev_close) &
                (prev_high - prev_close.combine(prev_open,max)).gt(3 * abs_prev_close_minus_open) &
                (prev_close.combine(prev_open,min) - prev_low).gt(3 * abs_prev_close_minus_open)
        )
        return None

    def piercing_pattern(self,shift:int=1):
        prev_close = self.close.shift(shift)
        prev_open = self.open.shift(shift)
        prev_low = self.low.shift(shift)

        self.dataframe[self.ohlc["close_name"] + "_piercing_pattern"] = (prev_close.lt(prev_open) &
                                                                        self.open.lt(prev_low) &
                                                                         prev_open.gt(self.close) &
                                                                          self.close.gt( (prev_close+((prev_open - prev_close) / 2))
                                                                         )  )
        return None
    def rain_drop(self,shift:int=1):
        prev_close = self.close.shift(shift)
        prev_open = self.open.shift(shift)
        prev_low = self.low.shift(shift)
        prev_high = self.high.shift(shift)
        self.dataframe[self.ohlc["close_name"] + "_rain_drop"] = (prev_close.lt(prev_open) &
                                                                  (abs(prev_close - prev_open) / (prev_high - prev_low)).ge(0.7) &
                                                                  (abs(self.close - self.open) / (self.high - self.low)).lt(0.3) &
                                                                  (abs(self.close - self.open) / (self.high - self.low)).ge(0.1) &
                                                                  prev_close.gt(self.close) &
                                                                  prev_close.gt(self.open)

                                                                  )
        return None

    def rain_drop_doji(self, shift: int = 1):
        prev_close = self.close.shift(shift)
        prev_open = self.open.shift(shift)
        prev_high = self.high.shift(shift)
        prev_low = self.low.shift(shift)

        abs_close_minus_open = abs(self.close - self.open)
        abs_prev_close_minus_open = abs(prev_close - prev_open)

        self.dataframe[self.ohlc["close_name"] + "_rain_drop_doji"] = (
                prev_close.lt(prev_open) &
                (abs_prev_close_minus_open / (prev_high - prev_low)).ge(0.7) &
                (abs_close_minus_open / (self.high - self.low)).lt(0.1) &
                prev_close.gt(self.close) &
                prev_close.gt(self.open) &
                (self.high - self.close.combine(self.open,max)).gt(3 * abs_close_minus_open) &
                (self.close.combine(self.open,min) - self.low).gt(3 * abs_close_minus_open)
        )
        return None

    def shooting_star(self, shift: int = 1):
        prev_close = self.close.shift(shift)
        prev_open = self.open.shift(shift)

        abs_close_minus_open = abs(self.close - self.open)

        self.dataframe[self.ohlc["close_name"] + "_shooting_star"] = (
                (prev_open.lt(prev_close) & prev_close.lt(self.open)) &
                (self.high - self.open.combine(self.close,max)).ge(abs_close_minus_open * 3) &
                ( self.close.combine(self.open,min) - self.low).le(abs_close_minus_open)
        )
        return None

    def star(self, shift: int = 1):
        prev_close = self.close.shift(shift)
        prev_open = self.open.shift(shift)
        prev_high = self.high.shift(shift)
        prev_low = self.low.shift(shift)

        abs_close_minus_open = abs(self.close - self.open)
        abs_prev_close_minus_open = abs(prev_close - prev_open)

        self.dataframe[self.ohlc["close_name"] + "_star"] = (
                prev_close.gt(prev_open) &
                (abs_prev_close_minus_open / (prev_high - prev_low)).ge(0.7) &
                (abs_close_minus_open / (self.high - self.low)).lt(0.3) &
                (abs_close_minus_open / (self.high - self.low)).ge(0.1) &
                prev_close.lt(self.close) &
                prev_close.lt(self.open)
        )
        return None