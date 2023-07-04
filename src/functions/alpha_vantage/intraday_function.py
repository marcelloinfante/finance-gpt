import json

import pandas as pd

import chainlit as cl

from src.functions.alpha_vantage.base import AlphaVantageBase


class IntradayFunction:
    @classmethod
    def run(self, symbol="", interval="", table_name=""):
        params = {"symbol": symbol, "interval": interval}

        response = AlphaVantageBase.run("intraday", **params)

        for time in ["1min", "5min", "15min", "30min", "60min"]:
            time_series = response.get(f"Time Series ({time})")

            if time_series:
                break

        response_df = pd.DataFrame(time_series).transpose()

        cl.user_session.set(table_name, response_df)

        response = {
            "content": json.dumps(
                {"success": True, "table_name": table_name},
            ),
            "is_dataframe": False,
        }

        return response

    @classmethod
    def get_infos(self):
        infos = {
            "name": "intraday",
            "description": "This API returns current and 20+ years of historical intraday OHLCV time series of the equity specified, covering extended trading hours where applicable (e.g., 4:00am to 8:00pm Eastern Time for the US market). You can query both raw (as-traded) and split/dividend-adjusted intraday data from this endpoint.",
            "parameters": {
                "type": "object",
                "properties": {
                    "symbol": {
                        "type": "string",
                        "description": "The name of the equity of your choice. For example: symbol=IBM",
                    },
                    "interval": {
                        "type": "string",
                        "description": "Time interval between two consecutive data points in the time series. The following values are supported: 1min, 5min, 15min, 30min, 60min",
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
