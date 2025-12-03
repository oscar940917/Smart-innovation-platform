# 匯入環境變數
from dotenv import load_dotenv
import time
from openai import OpenAI

import matplotlib.pyplot as plt  #pip install matplotlib



# 載入 .env
load_dotenv()

client = OpenAI()

THREAD_ID = "thread_aaIGkP6a9Wj0jNt2S0N9S512"  # 用你先前建立的 thread.id
RUN_ID = "run_msf1PaVVB9pSou09DoaG5jrs"     # 用你先前執行後印出的 run.id


print(f" 正在檢查 Run 狀態...\nThread: {THREAD_ID}\nRun: {RUN_ID}\n")

# 等待 run 完成
while True:
    run = client.beta.threads.runs.retrieve(thread_id=THREAD_ID, run_id=RUN_ID)
    print(f"當前狀態: {run.status}")

    if run.status in ["completed", "failed", "cancelled"]:
        break
    time.sleep(10)

# === 狀態檢查完成 ===
if run.status == "completed":
    print("\n任務完成，正在取得回覆...\n")

    # 取得所有訊息
    messages = client.beta.threads.messages.list(thread_id=THREAD_ID)

    for msg in reversed(messages.data):  # 最新訊息在最前
        role = msg.role
        print(f"🗣️ {role.upper()}:")
        for content in msg.content:
            if content.type == "text":
                print(content.text.value)
            elif content.type == "image_file":
                image_id = getattr(content.image_file, "file_id", None)
                if image_id:  # 確保 image_id 不是空
                    print(f"圖片輸出（file_id）: {image_id}")

                

                    # 在檢測到圖片時，下載圖片
                    image_content  = client.files.content(image_id).read() #需要先 .read() 取出 bytes 才能寫入檔案
                    with open("output_chart.png", "wb") as f:
                        f.write(image_content )
                    print("圖片已下載：output_chart.png")
                else:
                    print("找不到圖片 ID，跳過下載")
        print("-" * 50)

elif run.status == "failed":
    print("Run 執行失敗。")
    print(run)
elif run.status == "cancelled":
    print("Run 被取消。")