import os
import json

from pandasai import PandasAI
from pandasai.llm.openai import OpenAI

import chainlit as cl

class PandasAIFunction:
    @classmethod
    def run(self, dataframes=[], question=""):
        llm = OpenAI(api_token=os.environ.get("OPENAI_API_KEY"))
        pandas_ai = PandasAI(llm)
        
        dfs = []
        for df in dataframes:
            dfs.append(cl.user_session.get(df))
        
        response = pandas_ai(dfs, prompt=question)
        
        if hasattr(response, "to_json"):
            response = response.to_json()
        else:
            response = json.dumps(response)
        
        return response
        
    
    @classmethod
    def get_infos(self):
        infos = {
            "name": "pandas_ai",
            "description": "Ask questions about dataframes, tables and CSVs.",
            "parameters": {
                "type": "object",
                "properties": {
                    "dataframes": {
                        "type": "array",
                        "items": {
                            "type": "string",
                            "description": "Dataframe name.",
                        }
                    },
                    "question": {"type": "string", "description": "Question you want to ask to dataframe"},
                },
                "required": ["dataframes", "question"],
            },
        }
        
        
        return infos