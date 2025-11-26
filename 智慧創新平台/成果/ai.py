import os
from flask import Flask, render_template, request
from openai import OpenAI
from dotenv import load_dotenv

# 讀取 .env 檔案
load_dotenv()

# 取得環境變數
OPENAI_API_KEY = os.getenv("OPEN_API_KEY")
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

# 初始化 OpenAI 客戶端
client = OpenAI(api_key=OPENAI_API_KEY)

# Flask app
template_path = os.path.join(os.path.dirname(__file__), "templates")
app = Flask(__name__, template_folder=template_path)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        description = request.form.get("description")
        if description:
            try:
                result = generate_code(description)
            except Exception as e:
                result = f"生成失敗: {str(e)}"
    return render_template("index.html", result=result)

def generate_code(description):
   
    system_prompt = f"根據以下描述生成程式碼：{description}"
    
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "你是一個程式碼生成助手。"},
            {"role": "user", "content": system_prompt}
        ]
    )
    
    # Debug: 印出完整回傳內容
    print(response)
    
    try:
        return response.choices[0].message.content.strip()
    except (IndexError, AttributeError):
        return "生成程式碼時發生錯誤"

if __name__ == "__main__":
    app.run(debug=DEBUG)
