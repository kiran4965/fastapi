from fastapi import FastAPI, Query
from Schema import Trade
from Data import TRADES
import datetime as dt
from typing import Optional
from fastapi_pagination import Page, add_pagination, paginate

app = FastAPI()

# pagination
DEFUALT_OFFSET = 0
DEFUALT_LIMIT = 10



@app.get("/", status_code=200)
async def Home():
    return {"msg" : "server running"}


# Listing Trades and Advanced filtering
@app.get("/AllTrades/", status_code=200, response_model=Page[Trade])
async def AllTrades(sort: str = Query(None, description="sorting criteria"),
                    sort_order: Optional[bool] = False,
                    assetClass: Optional[str] = None, 
                    end: Optional[dt.datetime] = None, 
                    maxPrice: Optional[float]= None, 
                    minPrice: Optional[float] = None, 
                    start: Optional[dt.datetime] = None, 
                    tradeType: Optional[str] = None,
                    offset: Optional[int] = DEFUALT_OFFSET,
                    limit: Optional[int] = DEFUALT_LIMIT):
    
    # just sorting and pagination
    opt_par = not(assetClass or end or maxPrice or minPrice or start or tradeType)
    if opt_par:
        if sort=="assetClass" or sort=="counterparty":                      # handling Optional
            result = sorted(TRADES, key=lambda x: x[sort] or '', reverse=sort_order)
        elif sort=="price" or sort=="quantity":                             # handling nested
            result = sorted(TRADES, key=lambda x: x["tradeDetails"][sort] or '', reverse=sort_order)
        elif sort:
            result = sorted(TRADES, key=lambda x: x[sort], reverse=sort_order)
        else:
            result = TRADES
        
        if offset<len(result):
            count_trade = min(limit, len(result)-offset)
            if count_trade > 0:
                return paginate(result[offset : offset+count_trade])
        return paginate(result)
    
    # filtering
    result = []
    if assetClass:
        result1 = list(filter(lambda trade: assetClass.lower() in trade["assetClass"].lower(), TRADES))
        result = result1
    if end:
        result1 = [trade for trade in TRADES if trade["tradeDateTime"] <= end]
        result = result + result1
    if maxPrice:
        result1 = [trade for trade in TRADES if trade["tradeDetails"]["price"] <= maxPrice]
        result = result + result1
    if minPrice:
        result1 = [trade for trade in TRADES if trade["tradeDetails"]["price"] >= minPrice]
        result = result + result1
    if start:
        result1 = [trade for trade in TRADES if trade["tradeDateTime"] >= start]
        result = result + result1
    if tradeType:
        result1 = [trade for trade in TRADES if trade["tradeDetails"]["buySellIndicator"] == tradeType]
        result = result + result1


    # sorting
    if sort=="assetClass" or sort=="counterparty":
        result = sorted(result, key=lambda x: x[sort] or '', reverse=sort_order)
    elif sort=="price" or sort=="quantity":
        result = sorted(TRADES, key=lambda x: x["tradeDetails"][sort] or '', reverse=sort_order)
    elif sort:
        result = sorted(result, key=lambda x: x[sort], reverse=sort_order)
    
    # pagination
    if offset<len(result):
        count_trade = min(limit, len(result)-offset)
        if count_trade > 0:
            return paginate(result[offset : offset+count_trade])
        
    return paginate(result)


# Single trade
@app.get("/Trade/{trade_id}", status_code=200, response_model=Trade)
async def retrieveTrade(trade_id):
    result = [trade for trade in TRADES if trade["tradeId"] == trade_id]
    if result:
        return result[0]
    

# Searching trades, not case-sensitive
@app.get("/search/", status_code=200, response_model=Page[Trade])
async def searchTrade(search):
    result = list(filter(lambda trade: search.lower() in trade["instrumentId"].lower() + trade["instrumentName"].lower() + trade["trader"].lower(), TRADES))
    temp = [trade for trade in TRADES if isinstance(trade["counterparty"], str) and search.lower() in trade["counterparty"].lower()]
    result = result + temp
    return paginate(result)


add_pagination(app)