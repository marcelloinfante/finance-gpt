from enum import Enum
from src.functions.chart_function import ChartFunction
from src.functions.table_qa_function import TableQAFunction
from src.functions.asset_price_function import AssetPriceFunction
from src.functions.asset_price_ajusted_function import AssetPriceAjustedFunction
from src.functions.market_news_sentiment_function import MarketNewsSentimentFunction


class FunctionsEnum(Enum):
    chart = ChartFunction
    table_qa = TableQAFunction
    asset_price = AssetPriceFunction
    asset_price_ajusted = AssetPriceAjustedFunction
    market_news_sentiment = MarketNewsSentimentFunction
