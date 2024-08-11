# Algorithmic Trading Bot in Python
This is a learning/pet project to develop an automated trading bot in python with the intent of executing trades for the user with no prior knowledge of trading by the user
The bot trades and records/logs activities/actions it takes to enable fine tuning the bot for optimal performance
Inorder to enter a position, the bot runs through 4 filters to find an optimal entry signal, the filters are:
1. Obtaining the general trend of the market in 30Min timeframe(this can be changed depending on user preference)
2. Obtaining the Instant trend of the market in 5Min timeframe(this can be changed depending on user preference)
3. Check for the stochastic crossing for entry confirmation
4. check for Exponential Moving Average crossing between the slow and fast moving averages
When all filters return true, the trade is executed else the cycle is repeated until a favorable entry is obtained

