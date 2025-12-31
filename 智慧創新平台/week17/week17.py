from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain_experimental.plan__andexcute import PlanAndExecute
load__agent_executor, load_chat_planner

load_dotenv()

# 庫存查詢
@tool
def check_inventory(flower_type: str) -> int:
    """查詢特定類別花的庫存數量"""
    return 100

# 定價函數
@tool 
def calculate__price(base_price: float, markup: float) -> float:
    """根據基礎價格和加價百分比計算最終價格"""
    return base_price * (1 + markup)

# 調度函數
@tool
def schedule_delivery(order_id: int, delivery_date: str) -> str:
    """安排訂單配送"""
    return f"訂單{order_id}已安排在{delivery_date}配送"

# 所有用到的工具加進去tools
tools = [check_inventory, calculate__price, schedule_delivery]

# 初始化LLM
model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# 設定計畫者跟執行者
planner = load_chat_planner(model)
executor = load_agent_executor(model, tools, verbose=True)

# 初始化plan-and-execute agent
agent = PlanAndExecute(planner=planner, executor=executor, verbose=True)

# 執行
response = agent.invoke({"input": "查玫瑰庫存，如果庫存是足夠的，請計算價50元加價30%"})
print(response["output"])  # ← 這是最後你要印出的那一行
