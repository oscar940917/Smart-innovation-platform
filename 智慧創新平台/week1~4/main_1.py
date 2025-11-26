import os
from openai import OpenAI
from dotenv import load_dotenv
import requests
from PIL import Image
from io import BytesIO

load_dotenv()

open_api_key = os.getenv("OPEN_API_KEY")

client = OpenAI(api_key=open_api_key)

response = client.images.generate(
    model="dall-e-3",
    prompt="在動漫一拳超人裡有一位S級第二名的英雄，名字叫做顫慄的龍捲，外表是一位穿著黑色連衣裙的傲嬌蘿莉的感覺，頭髮是一頭綠色的長髮尾部捲捲的，請你生成他的圖片，或是直接給我你搜尋到的圖片也可以",
    size="1024x1024",
    quality="standard",
    n=1
)

#取得圖片 URL
image_url =response.data[0].url
print(f"圖片生成成功:{image_url}")

#下載圖片內容
image_data = requests.get(image_url).content

#儲存圖片
image_path = "output.png"
with open(image_path,"wb") as f:
    f.write(image_data)

#顯示圖片
img = Image.open(BytesIO(image_data))
img.show()
