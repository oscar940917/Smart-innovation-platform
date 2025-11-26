from flask import Flask, render_template, request
from openai import OpenAI

# 直接寫 API Key（自己用沒問題）
OPENAI_API_KEY = "OPENAI_API_KEY"

# 初始化 OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        text_to_translate = request.form.get("text")
        if text_to_translate:
            result = translate_to_english(text_to_translate)
    return render_template("query.html", result=result)

def translate_to_english(text):
    system_prompt = "將輸入的中文翻譯成英文。"
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    app.run(debug=True)
