import os
from typing import Type, List

import chainlit as cl

from langchain.tools import BaseTool

from pandasai import PandasAI
from pandasai.llm.openai import OpenAI

from src.tools.chart_creation_tool.schema import ChartCreationSchema


class ChartCreationTool(BaseTool):
    name = "chart_creation"
    description = (
        "You can create charts from dataframes, tables and CSVs if the user want."
    )
    args_schema: Type[ChartCreationSchema] = ChartCreationSchema

    def _run(
        self,
        tables: List[str],
        description: str,
        chart_name: str,
    ) -> str:
        pass

    async def _arun(
        self,
        tables: List[str],
        description: str,
        chart_name: str,
    ) -> str:
        dfs = []
        for df in tables:
            dfs.append(cl.user_session.get(df))

        await self._create_table(dfs, description)

        created_chart_path = self._get_latest_created_chart_path(os.getcwd())

        await cl.Image(
            path=created_chart_path, name=chart_name, display="inline"
        ).send()

        response = f"Escreava para o usuário que o gráfico foi criado e mostre ele para o usuário escrevendo: '{chart_name}'."

        return response

    async def _create_table(self, dfs, description):
        llm = OpenAI(api_token=os.environ.get("OPENAI_API_KEY"))
        charts_path = os.getcwd()
        pandas_ai = PandasAI(llm, save_charts=True, save_charts_path=charts_path)

        return pandas_ai(dfs, prompt=description)

    def _get_latest_created_chart_path(self, charts_path):
        charts_dir = os.path.join(charts_path, "exports", "charts")

        subdirectories = [
            subd
            for subd in os.listdir(charts_dir)
            if os.path.isdir(os.path.join(charts_dir, subd))
        ]

        sorted_subdirectories = sorted(
            subdirectories,
            key=lambda subdir: os.path.getmtime(os.path.join(charts_dir, subdir)),
            reverse=True,
        )

        latest_dir = sorted_subdirectories[0] if sorted_subdirectories else None

        chart_path = os.path.join(charts_dir, latest_dir, "chart.png")

        return chart_path
