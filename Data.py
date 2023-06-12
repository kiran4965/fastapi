import datetime as dt

TRADES = [
    {
        "assetClass": "Equity",
        "counterparty": "XYZ Corporation",
        "instrumentId": "AAPL",
        "instrumentName": "Apple Inc",
        "tradeDateTime": dt.datetime(2023, 5, 15, 10, 30, 53),
        "tradeDetails": {
            "buySellIndicator": "BUY",
            "price": 150.5,
            "quantity": 100
        },
        "tradeId": "KM01",
        "trader": "Kiranprava Maharana"
    },
    { 
        "assetClass" : "FX",
        "counterparty": "ABC Bank", 
        "instrumentId": "EURUSD",
        "instrumentName": "Euro/US Dollar",
        "tradeDateTime": dt.datetime(2023, 6, 10, 14, 45, 3),
        "tradeDetails":
        {
            "buySellIndicator" : "SELL",
            "price": 20.50,
            "quantity": 200
        },
        "tradeId": "PG02",
        "trader": "Pragati Gupta"
    }, 
    {
        "assetClass": "Equity",
        "counterparty": "XYZ Corporation",
        "instrumentId": "TSLA",
        "instrumentName": "Tesla",
        "tradeDateTime": dt.datetime(2023, 6, 1, 11, 30, 16),
        "tradeDetails": {
            "buySellIndicator": "BUY",
            "price": 1000.0,
            "quantity": 10
        },
        "tradeId": "ML03",
        "trader": "Mrunal Lalwani"
    },
    {
        "assetClass": "Bond",
        "counterparty": "PQR Company",
        "instrumentId": "MSFT",
        "instrumentName": "Microsoft Corporation",
        "tradeDateTime": dt.datetime(2023, 6, 10, 4, 0, 0),
        "tradeDetails": {
            "buySellIndicator": "BUY",
            "price": 56.4,
            "quantity": 13
        },
        "tradeId": "UN04",
        "trader": "Unnati Markam"
    },
    {
        "assetClass": "Equity",
        "counterparty": "DEF Company",
        "instrumentId": "GOOGL",
        "instrumentName": "Alphabet Inc.",
        "tradeDateTime": dt.datetime(2023, 6, 9, 9, 21, 42),
        "tradeDetails": {
            "buySellIndicator": "SELL",
            "price": 11.4,
            "quantity": 50
        },
        "tradeId": "PK05",
        "trader": "Pragya Kiran",
    },
    {
        "assetClass": "Equity",
        "counterparty": None,
        "instrumentId": "AMZN",
        "instrumentName": "Amazon.com, Inc.",
        "tradeDateTime": dt.datetime(2023, 5, 21, 12, 6, 20),
        "tradeDetails": {
            "buySellIndicator": "BUY",
            "price": 5.4,
            "quantity": 150
        },
        "tradeId": "TG06",
        "trader": "Tejaswini Gupta",
    },
    {
        "assetClass": "Bond",
        "counterparty": "GHI Company",
        "instrumentId": "NFLX",
        "instrumentName": "Netflix,Inc.",
        "tradeDateTime": dt.datetime(2023, 6, 5, 16, 52, 0),
        "tradeDetails": {
            "buySellIndicator": "SELL",
            "price": 2.94,
            "quantity": 80
        },
        "tradeId": "SK07",
        "trader": "Sanika Kanade",
    },
    {
        "assetClass": "FX",
        "counterparty": "UK Bank",
        "instrumentId": "EUR",
        "instrumentName": "Euro",
        "tradeDateTime": dt.datetime(2023, 4, 9, 8, 4, 6),
        "tradeDetails": {
            "buySellIndicator": "SELL",
            "price": 6.3,
            "quantity": 50000
        },
        "tradeId": "KK08",
        "trader": "Kiran Kumar"
    },
    {
        "assetClass": "Equity",
        "counterparty": "XYZ Corporation",
        "instrumentId": "AMZN",
        "instrumentName": "Amazon.com,Inc.",
        "tradeDateTime": dt.datetime(2023, 5, 15, 10, 46, 3),
        "tradeDetails": {
            "buySellIndicator": "SELL",
            "price": 150.5,
            "quantity": 100
        },
        "tradeId": "KM09",
        "trader": "Kiranprava Maharana"
    },
    {
        "assetClass": None,
        "counterparty": None,
        "instrumentId": "NFLX",
        "instrumentName": "Netflix,Inc.",
        "tradeDateTime": dt.datetime(2023, 5, 30, 6, 52, 3),
        "tradeDetails": {
            "buySellIndicator": "BUY",
            "price": 67.8,
            "quantity": 40
        },
        "tradeId": "ML10",
        "trader": "Mrunal Lalwani",
    },
    {
        "assetClass": "Equity",
        "counterparty": "DEF Company",
        "instrumentId": "GOOGL",
        "instrumentName": "Alphabet Inc.",
        "tradeDateTime": dt.datetime(2023, 6, 3, 13, 42, 20),
        "tradeDetails": {
            "buySellIndicator": "BUY",
            "price": 3.5,
            "quantity": 50
        },
        "tradeId": "SK11",
        "trader": "Sanika Kanade",
    }
]