# 匯入環境變數
from dotenv import load_dotenv
load_dotenv()

import os
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, AgentType, load_tools

# 1. 初始化大模型
llm = ChatOpenAI(model='gpt-4o-mini', temperature=0.3)

# 2. 設定工具：將 serpapi 換成 arxiv
# 我們保留 llm-math，這樣 Agent 搜尋到論文數據後還能做計算
tools = load_tools(["arxiv", "llm-math"], llm=llm)

# 3. 建立 ReAct Agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True, # 讓你看到 ReAct 的思考過程
    handle_parsing_errors=True
)

# 4. 執行查詢
# 範例：搜尋關於 "Large Language Models" 的最新進展
query = "幫我搜尋 ArXiv 上關於 ' normal distribution'的相關論文並翻譯成中文統整一下重點"
agent.run(query)