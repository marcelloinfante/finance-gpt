import json

from src.utils.alpha_vantage.base import AlphaVantageBase


class MarketNewsSentimentFunction:
    @classmethod
    async def run(self, ticker="", topics=""):
        api_response = AlphaVantageBase.run(
            slug="news-sentiment",
            ticker=ticker,
            topics=topics,
        )

        response = {
            "sentiment_score_definition": api_response["sentiment_score_definition"],
            "relevance_score_definition": api_response["relevance_score_definition"],
            "feed": api_response["feed"][:3],
        }

        response = json.dumps(response)

        return response

    @classmethod
    def get_infos(self):
        infos = {
            "name": "market_news_sentiment",
            "description": "The API returns current and 20+ years of historical time series (date, open, high, low, close, volume) of the equity specified.",
            "parameters": {
                "type": "object",
                "properties": {
                    "ticker": {
                        "type": "string",
                        "description": "The stock/crypto/forex symbols of your choice. For example: tickers=IBM will filter for articles that mention the IBM ticker; tickers=COIN,CRYPTO:BTC,FOREX:USD will filter for articles that simultaneously mention Coinbase (COIN), Bitcoin (CRYPTO:BTC), and US Dollar (FOREX:USD) in their content.",
                    },
                    "topics": {
                        "type": "string",
                        "enum": [
                            "mergers_and_acquisitions",
                            "energy_transportation",
                            "financial_markets",
                            "retail_wholesale",
                            "economy_monetary",
                            "economy_fiscal",
                            "manufacturing",
                            "economy_macro",
                            "life_sciences",
                            "real_estate",
                            "technology",
                            "blockchain",
                            "earnings",
                            "finance",
                            "ipo",
                        ],
                        "description": "The news topics of your choice. For example: topics=technology will filter for articles that write about the technology sector; topics=technology,ipo will filter for articles that simultaneously cover technology and IPO in their content.",
                    },
                },
                "required": [],
            },
        }

        return infos
