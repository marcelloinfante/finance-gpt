from pydantic import BaseModel, Field


class IntradaySchema(BaseModel):
    symbol: str = Field(
        description="The name of the equity of your choice. For example: symbol=IBM. Required."
    )
    interval: str = Field(
        description="Time interval between two consecutive data points in the time series. The following values are supported: 1min, 5min, 15min, 30min, 60min. Required."
    )
    table_name: str = Field(
        description="Give a unique name to the table generated from this request. Required."
    )
