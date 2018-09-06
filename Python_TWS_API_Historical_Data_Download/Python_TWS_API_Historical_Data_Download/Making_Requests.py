import datetime as dt

class Making_Requests:
    """description of class"""
    @staticmethod
    def Make_Bar_Request(app, contract, trading_date, end_trading_time, time_duration, time_resolution):
        app.reqHistoricalData(1002, contract, dt.datetime.combine(trading_date, end_trading_time).strftime("%Y%m%d %H:%M:%S"), time_duration, time_resolution, "TRADES", 1, 2, False, [])

    @staticmethod
    def Make_Ticks_Request(app, contract):
        app.reqHistoricalTicks(1003, contract,"20180829 09:30:00", "", 1000, "TRADES", 1, True, [])

