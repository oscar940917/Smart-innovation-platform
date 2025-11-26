from flask import Flask, render_template, request
from openai import OpenAI

# 你的 OpenAI API 密鑰
OPENAI_API_KEY = "your-openai-api-key"

# 初始化 OpenAI 客戶端
client = OpenAI(api_key=OPENAI_API_KEY)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        text_to_generate_code = request.form.get("text")
        if text_to_generate_code:
            result = generate_code(text_to_generate_code)
    return render_template("index.html", result=result)

def generate_code(description):
    """
    根據用戶描述生成程式碼
    """
    system_prompt = f"根據以下描述生成程式碼：{description}"
    
    # 使用 GPT 模型來生成程式碼
    response = client.chat.completions.create(
        model="gpt-4",  # 你可以根據需求選擇不同模型
        messages=[
            {"role": "system", "content": "你是一個程式碼生成助手。"},
            {"role": "user", "content": system_prompt}
        ]
    )
    # 返回生成的程式碼
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    app.run(debug=True)
