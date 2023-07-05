from dotenv import load_dotenv
import chainlit as cl

from langchain.agents import AgentType
from langchain.memory import ConversationBufferMemory
from langchain.agents import initialize_agent, Tool
from langchain.chat_models import ChatOpenAI

from src.tools.chart_creation_tool.index import ChartCreationTool
from src.tools.intraday_tool.index import IntradayTool
from src.tools.table_qa_tool.index import TableQATool

from langchain.prompts import MessagesPlaceholder

load_dotenv()


@cl.langchain_factory(use_async=True)
def load():
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo", streaming=True)

    chat_history = MessagesPlaceholder(variable_name="chat_history")
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    tools = [IntradayTool(), TableQATool()]

    agent_chain = initialize_agent(
        tools,
        llm,
        agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        memory=memory,
        agent_kwargs={
            "memory_prompts": [chat_history],
            "input_variables": ["input", "agent_scratchpad", "chat_history"],
        },
    )

    return agent_chain
