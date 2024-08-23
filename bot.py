# import needed libraries
from trader_lib import *
from logger import *
import sys


# check our trading account (blocked?, total amount?)
def check_account_ok():
    try:
        # get account info
        print("trying...")
    except Exception as e:
        lg.error("Could not get account info")
        lg.info(str(e))
        sys.exit()


# close current orders
def clean_open_orders():
    # get list of open orders
    open_orders = ''
    lg.info("List of open orders")
    lg.info(str(open_orders))

    for order in open_orders:
        # close order
        lg.info("Order %s closed" % str(order.id))

    lg.info("Closing orders complete")


# execute trading bot
def main():

    # initialize the logger
    initialize_logger()

    # check our trading account
    check_account_ok()

    # close current orders
    clean_open_orders()

    # define asset
    ticker = input("Write the ticker you want to operate with: ")
    
    # run trading bot
        # IN: string (ticker)
        # OUT: Boolean (True => success / False => falied)


if __name__ == '__main__':
    main()
