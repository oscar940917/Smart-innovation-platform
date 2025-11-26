from dotenv import load_dotenv
import os

# 載入 .env 檔案
load_dotenv()

# 取得環境變數
debug_mode = os.getenv("DEBUG")

if debug_mode:
    print("Debug mode is ON")
else:
    print("Debug mode is OFF")

# 取得環境變數
open_api_key = os.getenv("OPEN_API_KEY")
serp_api_key = os.getenv("SERP_API_KEY")

# 確保 API 金鑰被正確加載
if not open_api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file")

if not serp_api_key:
    raise ValueError("SERP_API_KEY not found in .env file")

# 匯入 OpenAI
from langchain_openai import OpenAI

# 初始化 OpenAI 模型，並傳遞 API 金鑰
llm = OpenAI(temperature=0, openai_api_key=open_api_key)

# 使用手動設置的提示字
prompt = "請告訴我周子瑜是誰。"

# 執行查詢
response = llm(prompt)
print(response)

# 匯入 SerpAPIWrapper
from langchain_community.utilities import SerpAPIWrapper
from langchain.tools import Tool

# 建立 SerpAPIWrapper
search = SerpAPIWrapper(serp_api_key=serp_api_key)

# 準備工具清單
tools = [
    Tool(
        name="Search",
        func=search.run,
        description="當 LLM 沒有相關知識時，用於搜尋知識"
    )
]

# 匯入代理功能
from langchain.agents import create_react_agent
from langchain.agents import AgentExecutor

# 建立 React agent
agent = create_react_agent(llm, tools=tools)

# 建構 AgentExecutor
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# 執行代理
print("執行結果")
agent_executor.invoke({"input": "周子瑜是誰啊?"})
