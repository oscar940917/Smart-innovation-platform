#推理跟行動的合作-專案:去搜尋今天台股的TSMC開盤/收盤價，給明天TSMC的最佳賣點價
#6.1複習ReAct框架
#6.2LangChain中的ReAct Agent的實現
#6.3LangChain的工具和工具包
#6.4creat_react_agent建立股票定價Agent

#匯入環境變數
from dotenv import load_dotenv #pip install python-dotenv
load_dotenv()

import os

#取得環境變數(金鑰放在.env)，不會揭露API code
serpapi_key = os.getenv("SERP_API_KEY")  #pip install google-search-results
print(serpapi_key)

#pip install numexpr
#初始化大模型:控制Agent
#from langchain_openai import ChatOpenAI #pip install langchain-openai 新版寫法不適合當下環境
from langchain.chat_models import ChatOpenAI
llm = ChatOpenAI(model='gpt-4o-mini', temperature=0.5)

#設定工具:兩個工具，1:SerpApi: google; 2:llm-math: 數學
from langchain.agents import initialize_agent, AgentType, load_tools
#from langchain_community.agent_toolkits.load_tools import load_tools
tools = load_tools(["serpapi","llm-math"],llm=llm,serpapi_api_key=serpapi_key)

#第一個練習
#from langchain.agents import initialize_agent, AgentType

agent = initialize_agent(
    tools = tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=True #新增項目
)

#agent.run("今天虎尾天氣、濕度、空氣品質如何?")
agent.run("去搜尋今天台股的TSMC開盤/收盤價，給明天TSMC的最佳賣點價?")



