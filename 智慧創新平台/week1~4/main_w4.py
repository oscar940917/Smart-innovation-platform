import os
from dotenv import load_dotenv
from openai import OpenAI

# 載入 .env
load_dotenv()

# 抓取 API 金鑰
open_api_key = os.getenv("OPEN_API_KEY")



# 建立 Client
client = OpenAI(api_key=open_api_key)

# 呼叫 Chat API
response = client.chat.completions.create(
    model="gpt-4-turbo-preview",
    response_format={"type": "json_object"},
    messages=[
        {"role": "system", "content": "你是一個幫助使用者了解老人常照顧的智慧助理，$奢車JSON格式內容"},
        {"role": "user", "content": "失智老人怎麼照顧最好"},
        {"role": "assistant", "content": "在身上安裝追蹤器是個不錯的選擇。"},
        {"role": "user", "content": "追蹤器送貨需要多少時間?"}
    ]
)

print("Assistant 回覆內容：")
print(response.choices[0].message.content)
