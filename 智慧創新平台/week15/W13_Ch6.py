import os
from dotenv import load_dotenv

# 1. 載入金鑰
load_dotenv()
serpapi_key = os.getenv("SERP_API_KEY")

# 2. 核心元件匯入 (改用絕對路徑，避開 __init__.py 的錯誤)
from langchain_openai import ChatOpenAI
from langchain_community.agent_toolkits.load_tools import load_tools
import langchainhub as hub

# 關鍵修正：直接從底層路徑抓取 AgentExecutor 和 create_react_agent
from langchain.agents.agent import AgentExecutor
from langchain.agents.react.agent import create_react_agent

# 3. 初始化模型 (GPT-4o mini)
llm = ChatOpenAI(model='gpt-4o-mini', temperature=0.5)

# 4. 準備工具
tools = load_tools(["serpapi", "llm-math"], llm=llm, serpapi_api_key=serpapi_key)

# 5. 取得思考模板 (ReAct Prompt)
prompt = hub.pull("hwchase17/react")

# 6. 建立 Agent 與執行器
agent = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor(
    agent=agent, 
    tools=tools, 
    verbose=True, 
    handle_parsing_errors=True
)

# 7. 執行任務
print("--- 啟動 TSMC ReAct 推理任務 ---")
query = "搜尋今日台股台積電(2330)的開盤與收盤價，並計算若要獲利 3% 賣出，目標價位是多少？"

# 使用 invoke 執行
agent_executor.invoke({"input": query})