from openai import OpenAI

# 直接在程式中設定 API Key
API_KEY = "OPENAI_API_KEY"

# 初始化 OpenAI client
client = OpenAI(api_key=API_KEY)

def translate_to_english(text):
    """
    使用 OpenAI GPT 模型，將輸入文字翻譯成英文
    """
    system_prompt = "將輸入的中文翻譯成英文。"

    response = client.chat.completions.create(
        model="gpt-4o-mini",  # 可改成其他模型，例如 gpt-4o
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": text}
        ]
    )

    return response.choices[0].message.content.strip()

# 測試用
if __name__ == "__main__":
    source_text = "今天天氣很好，我想去散步。"
    result = translate_to_english(source_text)
    print("翻譯結果：", result)
