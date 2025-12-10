<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>機器人圖片展示 + 問題輸入</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" crossorigin="anonymous">
    
    <style>
        body {
            background-color: #f8f9fa;
        }
        .page-title {
            margin-top: 30px;
            margin-bottom: 30px;
            color: #0d6efd;
            font-weight: 700;
        }
        .image-wrapper {
            margin-bottom: 20px;
        }
        .image-wrapper img {
            width: 100%;
            height: auto;
            border-radius: 8px;
            border: 1px solid #dee2e6;
            box-shadow: 0 0.25rem 0.5rem rgba(0,0,0,0.1);
        }
        #display-area {
            margin-top: 20px;
            padding: 15px;
            background-color: #fff3cd;
            border: 1px solid #ffeeba;
            border-radius: 8px;
            color: #856404;
            white-space: pre-wrap; /* 保留換行 */
        }
    </style>
</head>
<body>

<div class="container">
    <h1 class="text-center page-title">🤖 機器人圖片展示</h1>

    <!-- 使用者問題輸入區 -->
    <div class="mb-4">
        <label for="user-input" class="form-label">請輸入你的程式問題描述：</label>
        <textarea id="user-input" class="form-control" rows="4" placeholder="在此輸入問題描述..."></textarea>
        <button id="submit-btn" class="btn btn-primary mt-2">送出</button>
    </div>

    <!-- 顯示使用者輸入內容 -->
    <div id="display-area" style="display:none;"></div>

    <!-- 8 張機器人圖片區塊 -->
    <div class="row">
        <div class="col-md-3 image-wrapper"><img id="img1" alt="機器人 1"></div>
        <div class="col-md-3 image-wrapper"><img id="img2" alt="機器人 2"></div>
        <div class="col-md-3 image-wrapper"><img id="img3" alt="機器人 3"></div>
        <div class="col-md-3 image-wrapper"><img id="img4" alt="機器人 4"></div>
        <div class="col-md-3 image-wrapper"><img id="img5" alt="機器人 5"></div>
        <div class="col-md-3 image-wrapper"><img id="img6" alt="機器人 6"></div>
        <div class="col-md-3 image-wrapper"><img id="img7" alt="機器人 7"></div>
        <div class="col-md-3 image-wrapper"><img id="img8" alt="機器人 8"></div>
    </div>
</div>

<script>
    // 生成 8 張不同亂數的 Robohash GIF
    const used = new Set();
    function getRandomInt(max){
        let num;
        do { num = Math.floor(Math.random()*10000); } while(used.has(num));
        used.add(num);
        return num;
    }

    for(let i=1; i<=8; i++){
        document.getElementById("img"+i).src = "https://robohash.org/"+getRandomInt(10000)+"?set=set1";
    }

    // 按鈕事件，顯示使用者輸入
    document.getElementById("submit-btn").addEventListener("click", function() {
        const userInput = document.getElementById("user-input").value.trim();
        if(userInput){
            const displayArea = document.getElementById("display-area");
            displayArea.style.display = "block";
            displayArea.textContent = "你輸入的程式問題：\n" + userInput;
        }
    });
</script>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" crossorigin="anonymous"></script>
</body>
</html>
