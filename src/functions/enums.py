from enum import Enum
from src.functions.chart_function import ChartFunction
from src.functions.table_qa_function import TableQAFunction
from src.functions.alpha_vantage.intraday_function import IntradayFunction


class FunctionsEnum(Enum):
    chart = ChartFunction
    table_qa = TableQAFunction
    intraday = IntradayFunction
