# FinanceGPT
The FinanceGPT is a chatbot application for financial analysis using real time data and OpenAI fuctions.

## Quick Start
 1. Create a python virtual environment.
```
python -m venv venv
```

 2. Activate the virtual environment.
```
# Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

 3. Install the dependencies
```
pip install -r requirements.txt
```

 4. Add a .env file and add your OpenAI api key and your alpha vantage api key
```
# .env
OPENAI_API_KEY=
ALPHA_VANTAGE_API_KEY=
ALPHA_VANTAGE_BASE_URL=https://www.alphavantage.co
```

 5. Run the chatbot
```
chainlit run app.py
```
