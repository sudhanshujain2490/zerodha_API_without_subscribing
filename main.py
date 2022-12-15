# Download the 'kite_trade.py' file
# keep the file in same directory where your code file is stored


from kite_trade import *
import pandas as pd
# # First Way to Login
# # You can use your Kite app in mobile
# # But You can't login anywhere in 'kite.zerodha.com' website else this session will disconnected

# user_id = "XIU527" # Login Id
# password = "Sud@2620226_"      # Login password
# twofa = "355572"         # Login Pin or TOTP
#
# enctoken = get_enctoken(user_id, password, twofa)
# kite = KiteApp(enctoken=enctoken)
#---------------------------------------------------------------------------------------------
# # Second way is provide 'enctoken' manually from 'kite.zerodha.com' website
# # Than you can use login window of 'kite.zerodha.com' website Just don't logout from that window
# # # Process shared on YouTube 'TradeViaPython'

enctoken = "JYhDEHtt65xheXQsnH4Ktl3ZmpoaVH3Qn4m8oPAizSfa4l2Av1tInoNWC1zH7RZqMrPkJTuz8qQaEscJqujjCCW30ENJ0DrtkBWD/wWx3ftCyT1AbmUw3w=="
kite = KiteApp(enctoken=enctoken)

# Basic calls
print(kite.margins())

# print(kite.orders())
# orders_df = pd.DataFrame.from_dict(kite.orders())
# print(orders_df.to_string())
#
# print(kite.positions())
positions_df = pd.DataFrame.from_dict((kite.positions()))
print(positions_df)

print(kite.holdings())
holdings_df = pd.DataFrame.from_dict(kite.holdings())
print(holdings_df)

# # Get instrument or exchange
# print(kite.instruments())
# print(kite.instruments("NSE"))
# print(kite.instruments("NFO"))
#
# # Get Live Data
# print(kite.ltp("NSE:RELIANCE"))
# print(kite.ltp(["NSE:NIFTY 50", "NSE:NIFTY BANK"]))
# print(kite.quote(["NSE:NIFTY BANK", "NSE:ACC", "NFO:NIFTY22SEPFUT"]))
#
# # Get Historical Data
# import datetime
# instrument_token = 738561
# from_datetime = datetime.datetime.now() - datetime.timedelta(days=7)     # From last & days
# to_datetime = datetime.datetime.now()
# interval = "5minute"
# hd = kite.historical_data(instrument_token, from_datetime, to_datetime, interval, continuous=False, oi=False)
# #Convert list of dict to dataframe
# df = pd.DataFrame.from_dict(hd)
# df.to_csv("data.csv")
# print(df)

# Place Order
# order = kite.place_order(variety=kite.VARIETY_AMO,
#                          exchange=kite.EXCHANGE_NSE,
#                          tradingsymbol="ACC",
#                          transaction_type=kite.TRANSACTION_TYPE_BUY,
#                          quantity=1,
#                          product=kite.PRODUCT_MIS,
#                          order_type=kite.ORDER_TYPE_MARKET,
#                          price=None,
#                          validity=None,
#                          disclosed_quantity=None,
#                          trigger_price=None,
#                          squareoff=None,
#                          stoploss=None,
#                          trailing_stoploss=None,
#                          tag="TradeViaPython")
#
# print(order)

# # Modify order
# kite.modify_order(variety=kite.VARIETY_REGULAR,
#                   order_id="order_id",
#                   parent_order_id=None,
#                   quantity=5,
#                   price=200,
#                   order_type=kite.ORDER_TYPE_LIMIT,
#                   trigger_price=None,
#                   validity=kite.VALIDITY_DAY,
#                   disclosed_quantity=None)
#
# # Cancel order
# kite.cancel_order(variety=kite.VARIETY_AMO,
#                   order_id="221215004712377",
#                   parent_order_id=None)


