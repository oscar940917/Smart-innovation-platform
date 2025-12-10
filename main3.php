<?php
// ==============================
// PHP：處理使用者輸入並呼叫 OpenAI API
// ==============================

$answer = "";
if ($_SERVER["REQUEST_METHOD"] === "POST") {

    $userQuestion = $_POST["question"] ?? "";

    if (!empty($userQuestion)) {

        $apiKey = "";

        $payload = [
            "model" => "gpt-4o-mini",
            "messages" => [
                ["role" => "user", "content" => $userQuestion]
            ]
        ];

        $ch = curl_init("https://api.openai.com/v1/chat/completions");
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_HTTPHEADER, [
            "Content-Type: application/json",
            "Authorization: Bearer $apiKey"
        ]);
        curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($payload));

        $response = curl_exec($ch);
        curl_close($ch);

        $json = json_decode($response, true);

        $answer = $json["choices"][0]["message"]["content"] ?? "⚠ 無法取得 AI 回應";
    }
}
?>

<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI 問答 + 機器人圖片展示</title>

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    
    <style>
        .image-card img {
            width: 100%;
            border-radius: 8px;
        }
    </style>
</head>

<body class="bg-light">

<div class="container mt-5 mb-5">

    <h1 class="text-center text-primary fw-bold mb-4">🤖 AI 程式問題問答 + 機器人圖片展示</h1>

    <!-- 使用者輸入區 -->
    <div class="card p-4 mb-5">
        <h3 class="mb-3">請輸入你的程式問題：</h3>

        <form method="POST">

            <textarea class="form-control mb-3" name="question" rows="4"
                      placeholder="在此輸入你的程式問題..."><?php
                        if ($_SERVER["REQUEST_METHOD"] === "POST") echo htmlspecialchars($userQuestion);
                      ?></textarea>

            <button class="btn btn-primary">送出問題</button>
        </form>

        <?php if (!empty($answer)): ?>
            <div class="alert alert-success mt-4">
                <h5 class="fw-bold">AI 回答：</h5>
                <p><?php echo nl2br(htmlspecialchars($answer)); ?></p>
            </div>
        <?php endif; ?>
    </div>

    <!-- 8 張 RoboHash 圖片 -->
    <div class="card p-4">
        <h3 class="mb-3">🤖 8 張隨機機器人圖片</h3>

        <div class="row">
            <?php
            for ($i = 0; $i < 8; $i++) {
                $seed = rand(1, 999999); // 隨機種子
                $url = "https://robohash.org/$seed?set=set1";
                echo "
                <div class='col-md-3 mb-4'>
                    <img src='$url' class='img-fluid rounded shadow'>
                </div>
                ";
            }
            ?>
        </div>
    </div>

</div>

</body>
</html>
