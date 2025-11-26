from flask import Flask, request

app = Flask(__name__)

# 範例帳密
VALID_USER = "test"
VALID_PASS = "1234"

@app.route("/")
def hello_world():
    return "<p>Hello, Flask!!!</p><p><a href='/login'>前往登入</a></p>"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form.get("username", "")
        pwd = request.form.get("password", "")
        if user == VALID_USER and pwd == VALID_PASS:
            return f"<h1>歡迎，{user}！</h1><p>登入成功。</p>"
        else:
            # 登入失敗就回同一頁並顯示訊息
            return """
                <h1>登入</h1>
                <p style='color:red;'>帳號或密碼錯誤，請再試一次。</p>
                <form method='post'>
                  <label>帳號：<input name='username' required></label><br>
                  <label>密碼：<input name='password' type='password' required></label><br>
                  <button type='submit'>登入</button>
                </form>
                <p>提示帳密：test / 1234</p>
            """, 401

    # GET 顯示表單
    return """
        <h1>登入</h1>
        <form method='post'>
          <label>帳號：<input name='username' required></label><br>
          <label>密碼：<input name='password' type='password' required></label><br>
          <button type='submit'>登入</button>
        </form>
        <p>提示帳密：test / 1234</p>
    """

if __name__ == "__main__":
    app.run(debug=True)