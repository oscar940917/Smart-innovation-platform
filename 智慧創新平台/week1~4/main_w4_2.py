import os
from openai import OpenAI
from dotenv import load_dotenv
import requests
from PIL import Image
from io import BytesIO

# 載入環境變數
load_dotenv()

# 取得 API 金鑰
open_api_key = os.getenv("OPEN_API_KEY")  # 從 .env 文件中讀取 API 金鑰

# 檢查是否成功讀取 API 金鑰
if open_api_key is None:
    raise ValueError("API key not found in environment variables")

# 建立 OpenAI 客戶端，傳遞 api_key 進來
client = OpenAI(api_key=open_api_key)

# 優化後的英文 prompt
prompt = (
    "A full-body anime-style female character with pale white skin and long twin-tailed silver hair "
    "with pink highlights. She has red eyes and a gentle, slightly mischievous smile. Her hair is partially braided "
    "and decorated with flowers. She wears a modern Japanese fantasy outfit – a short, off-shoulder black and red kimono "
    "with gold accents, floral patterns, ribbons, tassels, and rope details. She has two swords crossed on her back and "
    "traditional platform sandals with straps tied around her legs. Blue flame-like spirits float around her, giving off "
    "a mystical and spiritual aura. The background is transparent or light-themed, and the art style is highly detailed, "
    "Japanese anime illustration, vivid and colorful."
)

# 生成圖片
response = client.images.generate(
    model="dall-e-3",
    prompt=prompt,
    size="1024x1024",
    quality="standard",
    n=1
)

# 取得圖片 URL
image_url = response.data[0].url
print(f"圖片生成成功: {image_url}")

# 下載圖片內容
image_data = requests.get(image_url).content

# 儲存圖片
image_path = "output.png"
with open(image_path, "wb") as f:
    f.write(image_data)

# 顯示圖片
img = Image.open(BytesIO(image_data))
img.show()
