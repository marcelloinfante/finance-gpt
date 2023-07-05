from pydantic import BaseModel, Field
from typing import List


class ChartCreationSchema(BaseModel):
    tables: List[str] = Field(
        description="List table names you want to create charts from. Example: ['ibm_intraday']. Required."
    )
    description: str = Field(
        description="Describe the chart you want to create. Required."
    )
    chart_name: str = Field(description="Give a unique name to the chart. Required.")
