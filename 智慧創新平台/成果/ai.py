import os
import subprocess
import json
from flask import Flask, render_template, request
from dotenv import load_dotenv
from openai import OpenAI

# -----------------------------
# 讀取環境變數
# -----------------------------
load_dotenv()
OPENAI_API_KEY = os.getenv("OPEN_API_KEY")
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

client = OpenAI(api_key=OPENAI_API_KEY)

app = Flask(__name__)


# -----------------------------
# 程式碼模板
# -----------------------------
TEMPLATES = {
    "bfs": """
from collections import deque

def bfs(graph, start):
    visited = set([start])
    queue = deque([start])

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
""",
    "dfs": """
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
""",
    "dijkstra": """
import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        dist, node = heapq.heappop(pq)
        if dist > distances[node]:
            continue
        for neighbor, cost in graph[node]:
            new_dist = dist + cost
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
    return distances
""",
    "merge_sort": """
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
""",
    "sql_select": """
-- 基本 SQL SELECT 模板
SELECT column1, column2
FROM table_name
WHERE condition;
"""
}


# -----------------------------
# 課程分類器
# -----------------------------
def classify(desc):
    text = desc.lower()

    if any(k in text for k in ["bfs", "breadth", "graph", "樹", "圖"]):
        return "bfs"
    if any(k in text for k in ["dfs", "depth"]):
        return "dfs"
    if any(k in text for k in ["dijkstra", "最短路徑"]):
        return "dijkstra"
    if "sort" in text or "排序" in text:
        return "merge_sort"
    if "sql" in text or "資料庫" in text:
        return "sql_select"

    return None


# -----------------------------
# GPT 生成（JSON 格式）
# -----------------------------
def generate_with_gpt(template, user_desc, language):

    prompt = f"""
你是一位資工系程式助教。

⚠️ 請務必輸出「完整 JSON」，格式如下：

{{
  "code": "<整份補齊後的程式碼>",
  "complexity": {{
    "time": "<時間複雜度 Big-O>",
    "space": "<空間複雜度 Big-O>"
  }},
  "explanation": "<簡要解釋（不超過 5 句）>"
}}

不要使用 ```json、``` 或任何 markdown 標記。

以下為模板，必須保留結構：
{template}

使用者需求：
{user_desc}

語言：{language}
"""

    response = client.responses.create(
        model="gpt-4.1",
        input=prompt,
        max_output_tokens=2000
    )

    raw = response.output_text.strip()

    # 去掉可能多的格式
    raw = raw.replace("```json", "").replace("```", "").strip()

    try:
        data = json.loads(raw)
        return data
    except:
        return {
            "code": raw,
            "complexity": {"time": "N/A", "space": "N/A"},
            "explanation": "⚠️ JSON 解析失敗，已顯示原始輸出。"
        }


# -----------------------------
# 語法檢查
# -----------------------------
def lint_code(language, code):

    file_map = {
        "Python": "temp.py",
        "JavaScript": "temp.js",
        "Java": "Temp.java",
        "C": "temp.c"
    }

    filename = file_map.get(language)
    if not filename:
        return "語法檢查不支援此語言。"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(code)

    try:
        if language == "Python":
            result = subprocess.run(["python", "-m", "py_compile", filename], capture_output=True, text=True)
        elif language == "JavaScript":
            result = subprocess.run(["node", filename], capture_output=True, text=True)
        elif language == "Java":
            result = subprocess.run(["javac", filename], capture_output=True, text=True)
        elif language == "C":
            result = subprocess.run(["gcc", filename], capture_output=True, text=True)

        if result.stderr:
            return result.stderr
        return "✔ 未發現語法錯誤。"
    except Exception as e:
        return str(e)


# -----------------------------
# Flask 主頁（前端完全不改）
# -----------------------------
@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    optimization_advice = None
    complexity_text = None
    lint_result = None
    language = None

    if request.method == "POST":
        description = request.form.get("description")
        language = request.form.get("language")

        # 1. 分類 → 模板
        category = classify(description)
        template = TEMPLATES.get(category, "")

        # 2. GPT JSON 生成
        ai_json = generate_with_gpt(template, description, language)

        # 3. 轉成前端需要的格式
        result = ai_json.get("code", "")
        explain = ai_json.get("explanation", "")

        time_c = ai_json.get("complexity", {}).get("time", "")
        space_c = ai_json.get("complexity", {}).get("space", "")

        complexity_text = f"時間：{time_c}\n空間：{space_c}"
        optimization_advice = explain

        # 4. 語法檢查
        lint_result = lint_code(language, result)

    return render_template("index.html",
                           result=result,
                           optimization_advice=optimization_advice,
                           complexity=complexity_text,
                           lint=lint_result,
                           language=language)


if __name__ == "__main__":
    app.run(debug=DEBUG)
