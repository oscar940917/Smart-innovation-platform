# =========================================
# ReAct + Tools 股價分析 Agent（TSMC）
# LangChain 1.2.0 穩定可跑版本
# =========================================

# --------- 載入環境變數 ---------
from dotenv import load_dotenv
import os

load_dotenv()

serpapi_key = os.getenv("SERP_API_KEY")
print("SERP API KEY Loaded:", bool(serpapi_key))

# --------- 初始化 LLM ---------
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.5
)

# --------- 載入工具（Tools）---------
from langchain_community.agent_toolkits.load_tools import load_tools

tools = load_tools(
    ["serpapi", "llm-math"],
    llm=llm,
    serpapi_api_key=serpapi_key
)

# --------- 建立 ReAct Agent（官方穩定版）---------
from langchain.agents import initialize_agent, AgentType

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# --------- 執行任務 ---------
query = """
請搜尋今天台股 TSMC（2330）的開盤價與收盤價，
計算今日漲跌幅，
並根據價格變化推算明天較佳的賣出價格建議。
"""

result = agent.invoke(query)

print("\n========== 最終結果 ==========")
print(result)
