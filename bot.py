# import needed libraries
from trader_lib import *
from logger import *
import sys

# initialize the logger
initialize_logger()

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

# define asset ()
    # IN: keyboard
    # OUT: string

# execute trading bot
    # IN: string (ticker)
    # OUT: Boolean (True => success / False => falied)
