# Code Archive by Topic

`2025/` 以下の日付ごとのコードを、テーマ別に整理したアーカイブです。  
2025年8〜11月に学習した内容を、後から再利用しやすい形にまとめています。

## ディレクトリ構成

- `basic_python/`  
  変数、ループ、関数、クラス、ファイル操作、例外処理などの基礎的な Python コード。
  - 例: `08_monte/`（モンテカルロ法）, `10_sort/`（ソート）, `15_file_handling/`（ファイル操作）

- `csv_json_handling/`  
  CSV / JSON / Base64 などのデータフォーマットの入出力・変換。
  - 例: `11_pandas_csv/`, `13_csv/`, `20_json/`, `21_base64/`

- `api_http/`  
  HTTP 通信・API 呼び出し関連。
  - 例: `12_api/`（GET/POST での API 通信 + レスポンス保存）

- `algorithms_data_structures/`  
  木構造・ヒープなどアルゴリズム寄りのコード。
  - 例: `16_tree_algorithms/`

- `data_engineering/`  
  スクレイピング・SQLite・データ前処理など「データを集めて整える」処理。
  - 例: `02_scrape_books/`, `03_sqlite_min/`, `01_analyze_sqlite/`, `05_cleaned_data_plot/`, `25~30_scraping/`

- `data_science_ml/`  
  機械学習・前処理・特徴量エンジニアリング・モデル評価。
  - 例:  
    - `01_k-means/`（クラスタリング）  
    - `04_nlp/`, `05_nlp_jan/`, `06_nlp_posinega/`（NLP 系）  
    - `02~04_data_cleaning/`, `06~09_missing_values/`, `10~15_outlier_detection/`  
    - `24~27_feature_engineering/`, `28~30_correlation/`  
    - `31_evaluating_regression_models/`, `01~08_evaluating_classification_models/`  
    - `07~20_app.py/`（ML デモアプリ）

- `visualization_matplotlib/`  
  折れ線・散布図・棒グラフ・箱ひげ・ヒストグラムなど、主に matplotlib / seaborn による可視化。
  - 例: `17_matplotlib/`, `18_scatter_plot/`, `23_scatter_plot/`,  
    `26_pie_chart/`, `27_histgram/`, `30_boxplot/`, `31_heatmap/`

- `visualization_geospatial/`  
  地図・地理情報・時系列ヒートマップなどの可視化。
  - 例:  
    - `09_temp_heatmap/`, `11_temp_heatmap_expand/`  
    - `10_choropleth_animation/`  
    - `12~13_temp_japan/`（日本地図 + GeoJSON + Plotly）  
    - `15~16_temp_data/`, `17~18_temp_plot/`（都道府県別気温の時系列）

---

## 運用ルール（メモ）

- 生のタイムラインは `2025/` 以下にそのまま保存しておく
- 学んだ内容は、必要に応じて `sorted/` 以下にコピーして再利用する
- 新しいコードを書くときは最初からテーマ別ディレクトリに置くことも検討する
