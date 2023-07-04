import os
import json

import pandas as pd
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI

import chainlit as cl


class TableQAFunction:
    @classmethod
    def run(self, dataframes=[], question=""):
        llm = OpenAI(api_token=os.environ.get("OPENAI_API_KEY"))

        pandas_ai = PandasAI(llm)

        dfs = []
        for df in dataframes:
            dfs.append(cl.user_session.get(df))

        response = pandas_ai(dfs, prompt=question)

        if isinstance(response, (pd.DataFrame, pd.Series)):
            response = {"content": response, "is_dataframe": True}
        else:
            if hasattr(response, "tolist"):
                response = response.tolist()

            response = json.dumps(response)

            response = {"content": response, "is_dataframe": False}

        return response

    @classmethod
    def get_infos(self):
        infos = {
            "name": "table_qa",
            "description": "Ask questions about dataframes, tables and CSVs.",
            "parameters": {
                "type": "object",
                "properties": {
                    "dataframes": {
                        "type": "array",
                        "items": {
                            "type": "string",
                            "description": "Dataframe name.",
                        },
                    },
                    "question": {
                        "type": "string",
                        "description": "Question you want to ask to dataframe",
                    },
                },
                "required": ["dataframes", "question"],
            },
        }

        return infos
