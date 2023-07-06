import pandas as pd

import chainlit as cl
from tabulate import tabulate

from src.utils.alpha_vantage.base import AlphaVantageBase

intervals_enum = {
    "1min": "Time Series (1min)",
    "5min": "Time Series (5min)",
    "15min": "Time Series (15min)",
    "30min": "Time Series (30min)",
    "60min": "Time Series (60min)",
    # "daily": "Time Series (Daily)",
    "weekly": "Weekly Time Series",
    "monthly": "Monthly Time Series",
}


class AssetPriceFunction:
    @classmethod
    async def run(self, symbol="", interval="", table_name=""):
        params = {"symbol": symbol}

        if "min" in interval:
            params.update({"slug": "intraday", "interval": interval, "adjusted": False})
        else:
            params.update({"slug": interval})

        api_response = AlphaVantageBase.run(**params)

        time_series_df = api_response.get(intervals_enum[interval])

        df = pd.DataFrame(time_series_df).transpose()

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

    @classmethod
    def get_infos(self):
        infos = {
            "name": "asset_price",
            "description": "The API returns current and 20+ years of historical time series (date, open, high, low, close, volume) of the equity specified.",
            "parameters": {
                "type": "object",
                "properties": {
                    "symbol": {
                        "type": "string",
                        "description": "The name of the equity of your choice. For example: symbol=IBM",
                    },
                    "interval": {
                        "type": "string",
                        "enum": list(intervals_enum.keys()),
                        "description": "Time interval between two consecutive data points in the time series.",
                    },
                    "table_name": {
                        "type": "string",
                        "description": "Give a unique name to the table generated from this request.",
                    },
                },
                "required": ["symbol", "interval", "table_name"],
            },
        }

        return infos
