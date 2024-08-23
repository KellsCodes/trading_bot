
# LOOP until timeout reached (ex. 2h)
# POINT ECHO: INITIAL CHECK
# check the position: ask the broker API if we have an open position with "asset"
    # IN: asset (string)
    # OUT: True (exists) / False (does not exists)
    
# check if tradable: ask the broker API if "asset" is tradable
    # IN: string
    # OUT: True (exists) / False (does not exists)
    
# GENERAL TREND
# load 30 min candles: demand the API for 30 min candles
    # IN: asset (or whatever the API needs), time range*, candle size*
    # OUT: 30 min candles (OHLC for every candle)

# Perform general trend analysis: detect interesting trend (UP / DOWN / NO CLEAR TREND)
    # IN: 30 min candles data (close data)
    # OUT: UP / DOWN / NO TREND (strings)
    # if no trend defined, go back to POINT ECHO
    
    # LOOP until timeout reached (ex. 30 min)
    # POINT DELTA
    # STEP 1: load 5 min candles
        # IN: asset (or whatever the API needs), time range*, candle size*
        # OUT: 5 min candles (OHLC for every candle)
        # if failed go back to POINT DELTA
        
    # STEP 2: perform instant trend analysis: confirm the trend detected by GT analysis
        # IN: 5 min candles data (close data), output of the GT analysis (UP / DOWN string)
        # OUT: True (confirmed) / False (not confirmed)
        # if failed go back to POINT DELTA
    
    # STEP 3: perform RSI analysis
        # IN: 5 min candles data (close data), output of the GT analysis (UP / DOWN string)
        # OUT: True (confirmed) / False (not confirmed)
        # if failed go back to POINT DELTA
    
    # STEP 4: perform stochastic analysis
        # IN: 5 min candles data (OHLC data), output of the GT analysis (UP / DOWN string)
        # OUT: True (confirmed) / False (not confirmed)
        # if failed go back to POINT DELTA
        
# SUBMIT ORDER
# submit order (limit order): interact with broker API
    # IN: number of shares to buy/sell, asset, desired price
    # OUT: True (confirmed) / False (not confirmed), position ID
    # if False, log error and abort ==> Go back POINT ECHO

# check position: see if position exists
    # IN: position ID
    # OUT: True (confirmed) / False (not confirmed)
    # if False, log error and abort ==> Go back POINT ECHO

# LOOP until timeout reached (ex. ~8h)
# Enter POSITION MODE: check the filter conditions in parallel
# IF check take profit: If True -> close position
    # IN: current gains (earning)
    # OUT: True / False

# ELIF check stop loss: If True ->  close position
    # IN: current gains (loosing)
    # OUT: True / False

# ELIF check stochastic crossing: If True ->  close position
    # STEP 1: pull 5 min OHLC data
        # IN: asset
        # OUT: OHLC data (5 min candles)

    # STEP 2: check whether stochastic curves are crossing
        # IN: OHLC data (5 min candles)
        # OUT: True / False
        

# GET OUT
# SUBMIT ORDER
# submit order (market order): interact with broker API
    # IN: number of shares to buy/sell, asset, position ID
    # OUT: True (confirmed) / False (not confirmed)
    # if False, keep retrying until successful

# check positionse: check if position exists
    # IN: position ID
    # OUT: True (still exists) / False (does not exists)
    # if False ==> Go back Submit order

# wait 15 min

# End

