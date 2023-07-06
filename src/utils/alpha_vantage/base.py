import os
import requests

from src.utils.alpha_vantage.enum import SLUG_ENUM


class AlphaVantageBase:
    @classmethod
    def run(self, slug="", **params):
        ALPHA_VANTAGE_BASE_URL = os.getenv("ALPHA_VANTAGE_BASE_URL")
        ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")

        endpoint = f"{ALPHA_VANTAGE_BASE_URL}/query"

        params = {
            "apikey": ALPHA_VANTAGE_API_KEY,
            "function": SLUG_ENUM[slug],
            **params,
        }

        response = requests.get(endpoint, params=params).json()

        return response
