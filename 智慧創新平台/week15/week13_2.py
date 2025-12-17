import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.agent_toolkits.load_tools import load_tools

# 避開損壞的 __init__.py，直接從底層路徑匯入
from langchain.agents.agent import AgentExecutor
from langchain.agents.initialize import initialize_agent
from langchain.agents.agent_types import AgentType

# 1. 載入金鑰
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPEN_API_KEY")

# 2. 初始化模型 (6.2 ReAct Agent 核心)
llm = ChatOpenAI(model='gpt-4o-mini', temperature=0)

# 3. 準備工具 (6.3 工具包應用)
tools = load_tools(["serpapi", "llm-math"], llm=llm, serpapi_api_key=os.getenv("SERP_API_KEY"))

# 4. 建立 Agent (6.4 整合大腦與工具)
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=True
)

# 5. 執行專案任務
query = "搜尋今日台股台積電(2330)的收盤價，並計算若要獲利 3% 賣出，目標價位是多少？"

print("--- 啟動 TSMC ReAct 推理任務 ---")
agent.run(query)