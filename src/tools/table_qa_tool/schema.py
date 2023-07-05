from pydantic import BaseModel, Field
from typing import List


class TableQASchema(BaseModel):
    tables: List[str] = Field(
        description="List table names you want to ask questions about. Example: ['ibm_intraday']. Required."
    )
    question: str = Field(description="Question you want to ask to tables. Required.")
    new_table_name: str = Field(
        description="Return a unique name for new table. Required."
    )
