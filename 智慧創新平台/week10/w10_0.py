import os
from dotenv import load_dotenv
from openai import OpenAI
import pandas as pd

# 切換到 CSV 所在資料夾（保險起見）
os.chdir(r"C:\Users\user\Desktop\智慧創新平台\week10")

# 載入 .env
load_dotenv()

# 讀取環境變數
OPENAI_API_KEY = os.getenv("OPEN_API_KEY")
SERP_API_KEY = os.getenv("SERP_API_KEY")
DEBUG = os.getenv("DEBUG")

# 檢查 API KEY
if not OPENAI_API_KEY:
    raise ValueError("請在 .env 設定 OPEN_API_KEY")

# DEBUG 模式
if DEBUG == "True":
    print("DEBUG 模式開啟")
    print(f"OPENAI_API_KEY: {OPENAI_API_KEY}")
    print(f"SERP_API_KEY: {SERP_API_KEY}")

# 建立 OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

# 讀取 CSV
file_path = 'sales_data_1.csv'
try:
    sale_data = pd.read_csv(file_path, encoding='big5')
    if DEBUG == "True":
        print("CSV 讀取成功，前五列資料：")
        print(sale_data.head())
except FileNotFoundError:
    print(f"找不到 CSV 檔案，請確認 {file_path} 是否存在於資料夾中。")
