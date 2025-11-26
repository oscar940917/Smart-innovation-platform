# 引入套件
from openai import OpenAI

# 直接設置你的 OpenAI API 金鑰
client = OpenAI(
    api_key="OPENAI_API_KEY"
)

# 建立助理 assistant
assistant = client.beta.assistants.create(
    name="小愛同學",
    instructions="你是數據分析助理。當收到指令時，可以讀上傳的CSV檔案，計算銷售、畫圖、生成PPT，並提供洞察與標題",
    tools=[{"type": "code_interpreter"}],
    model="gpt-4-turbo-preview"
)

# 顯示建立的 assistant
print(assistant)
