import os
from typing import Type, List

import chainlit as cl
from tabulate import tabulate

from langchain.tools import BaseTool

import pandas as pd
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI

from src.tools.table_qa_tool.schema import TableQASchema


class TableQATool(BaseTool):
    name = "table_qa"
    description = "Ask questions about dataframes, tables and CSVs."
    args_schema: Type[TableQASchema] = TableQASchema

    def _run(
        self,
        question: str,
        tables: List[str],
        new_table_name: str,
    ) -> str:
        pass

    async def _arun(
        self,
        question: str,
        tables: List[str],
        new_table_name: str,
    ) -> str:
        llm = OpenAI(api_token=os.environ.get("OPENAI_API_KEY"))

        pandas_ai = PandasAI(llm)

        dfs = []
        for df in tables:
            dfs.append(cl.user_session.get(df))

        response = pandas_ai(dfs, prompt=question)

        if isinstance(response, (pd.DataFrame, pd.Series)):
            await cl.Text(
                display="inline",
                language="json",
                name=f"{new_table_name}_show",
                content=tabulate(
                    response,
                    headers="keys",
                    tablefmt="rounded_outline",
                ),
            ).send()

            cl.user_session.set(new_table_name, response)

            response = f"Escreva para o usuário que a tabela foi criada e está salva em: '{new_table_name}'. Mostre a tabela escrevendo: '{new_table_name}_show.'"

        return response
