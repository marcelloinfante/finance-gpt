from typing import Type

import pandas as pd
import chainlit as cl
from tabulate import tabulate

from langchain.tools import BaseTool

from src.utils.alpha_vantage.base import AlphaVantageBase
from src.tools.intraday_tool.schema import IntradaySchema


class IntradayTool(BaseTool):
    name = "intraday"
    description = "This API returns current and 20+ years of historical intraday OHLCV time series of the equity specified, covering extended trading hours where applicable (e.g., 4:00am to 8:00pm Eastern Time for the US market). You can query both raw (as-traded) and split/dividend-adjusted intraday data from this endpoint."
    args_schema: Type[IntradaySchema] = IntradaySchema

    def _run(
        self,
        symbol: str,
        interval: str,
        table_name: str,
    ) -> str:
        pass

    async def _arun(
        self,
        symbol: str,
        interval: str,
        table_name: str,
    ) -> str:
        api_response = AlphaVantageBase.run(
            "intraday", symbol=symbol, interval=interval
        )

        for time in ["1min", "5min", "15min", "30min", "60min"]:
            time_series = api_response.get(f"Time Series ({time})")

            if time_series:
                break

        df = pd.DataFrame(time_series).transpose()

        cl.user_session.set(table_name, df)

        await cl.Text(
            language="json",
            name=f"{table_name}_show",
            display="inline",
            content=tabulate(
                df.head(5),
                headers="keys",
                tablefmt="rounded_outline",
            ),
        ).send()

        response = f"Escreva para o usuário que a tabela foi criada e está salva em: '{table_name}'. Mostre a tabela escrevendo: '{table_name}_show.'"

        return response
