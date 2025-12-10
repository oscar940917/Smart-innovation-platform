<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>影片與圖片並排顯示</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    
    <style>
        /* 提升視覺效果的自定義樣式 */
        .video-card, .image-card {
            padding: 15px;
            background-color: #ffffff;
            border: 1px solid #dee2e6; /* 輕微邊框 */
            border-radius: 10px;
            box-shadow: 0 0.5rem 1rem rgba(0,0,0,0.1); /* 柔和陰影 */
        }
        .page-title {
            margin-bottom: 30px;
            color: #0d6efd; /* Bootstrap Primary 藍色 */
            font-weight: 700;
        }
        .video-wrapper, .image-wrapper {
            margin-bottom: 20px;
        }
        .video-title-main, .image-title-main {
            color: #495057;
            border-bottom: 2px solid #0d6efd;
            padding-bottom: 10px;
            margin-bottom: 30px !important;
        }
        .image-card img {
            width: 100%;
            height: auto;
            border-radius: 8px;
        }
    </style>
</head>
<body>

<div class="container mt-5 mb-5">
    <h1 class="text-center page-title">🎬 影片與圖片並排顯示</h1>

    <!-- 影片區塊 -->
    <div class="row justify-content-center mb-5">
        <div class="col-xl-11 col-lg-11">
            <div class="video-card">
                <h2 class="h4 video-title-main">影片內容區</h2>

                <div class="row">
                    <!-- 第一個影片 -->
                    <div class="col-md-6 video-wrapper">
                        <h3 class="h5 mb-2 text-primary">🎥 第一個影片</h3>
                        <div class="ratio ratio-16x9">
                            <iframe 
                                src="https://www.youtube.com/embed/TNcw-Sod5oo?si=leGzpl1yxZQrJ6jE" 
                                title="YouTube 影片播放器 (第一個影片)" 
                                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                                allowfullscreen>
                            </iframe>
                        </div>
                    </div>

                    <!-- 第二個影片 -->
                    <div class="col-md-6 video-wrapper">
                        <h3 class="h5 mb-2 text-success">🎥 第二個影片</h3>
                        <div class="ratio ratio-16x9">
                            <iframe 
                                src="https://www.youtube.com/embed/TNcw-Sod5oo?si=leGzpl1yxZQrJ6jE" 
                                title="YouTube 影片播放器 (第二個影片)" 
                                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                                allowfullscreen>
                            </iframe>
                        </div>
                    </div>
                </div>
                <p class="mt-4 text-secondary border-top pt-3">
                    **佈局說明：** 頁面使用 Bootstrap 響應式設計，在中等螢幕以上會並排顯示兩個影片，在手機上會自動轉換為上下堆疊。
                </p>
            </div>
        </div>
    </div>

    <!-- 圖片區塊 -->
    <div class="row justify-content-center">
        <div class="col-xl-11 col-lg-11">
            <div class="image-card">
                <h2 class="h4 image-title-main">圖片內容區</h2>

                <div class="row">
                    <!-- 第一張圖片 -->
                    <div class="col-md-3 image-wrapper">
                        <img src="img1.gif" alt="圖片 1">
                    </div>
                    
                    <!-- 第二張圖片 -->
                    <div class="col-md-3 image-wrapper">
                        <img src="img2.gif" alt="圖片 2">
                    </div>
                    
                    <!-- 第三張圖片 -->
                    <div class="col-md-3 image-wrapper">
                        <img src="img3.gif" alt="圖片 3">
                    </div>
                    
                    <!-- 第四張圖片 -->
                    <div class="col-md-3 image-wrapper">
                        <img src="img4.gif" alt="圖片 4">
                    </div>
                </div>

                <p class="mt-4 text-secondary border-top pt-3">
                    **佈局說明：** 頁面使用 Bootstrap 響應式設計，在大螢幕顯示四張圖片，在中型螢幕會顯示兩張圖片，並在手機上顯示單張圖片。
                </p>
            </div>
        </div>
    </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
</body>
</html>
