import os
import requests

from alpha_vantage.enums import SLUG_ENUM


class Provider:
    def query_data(self, slug, **params):
        ALPHA_VANTAGE_BASE_URL = os.getenv('ALPHA_VANTAGE_BASE_URL')
        ALPHA_VANTAGFE_API_KEY = os.getenv('ALPHA_VANTAGFE_API_KEY')

        endpoint = f"{ALPHA_VANTAGE_BASE_URL}/query"

        params = {
            'apikey': ALPHA_VANTAGFE_API_KEY,
            'function': SLUG_ENUM[slug],
            **params
        }

        response = requests.get(endpoint, params=params).json()

        return response
