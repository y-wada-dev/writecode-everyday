# Write Code Everyday

## 概要
このリポジトリは、jQuery の作者 **John Resig** 氏によるブログ記事  
["Write Code Every Day"](https://johnresig.com/blog/write-code-every-day/) に触発されて開始しました。

目的は、**毎日コードを書く習慣を身につけ、エンジニアとしてのスキルアップを図ること**です。

---

## 運用方法

### 1. ルール
- 毎日コードを書きコミットする
- 小さなコードでもOK。ただしできる限り有益なコードを目指すこと
- GitHubで管理すること
- このリポジトリ以外でもOK
- 何をやったかはコミット履歴で振り返る

### 2. フォルダ構成
- ルート直下は **テーマ別（言語・技術）ディレクトリ**
- 整理済みコードは `python/library/<theme>/` にテーマ別で置く
- 日別の生コードは `python/raw_logs/YYYY/MM/DD_slug/` 形式で残す

例：
```markdown
writecode-everyday/
├── README.md
├── career.md                          # 個人メモ（.gitignore 済み）
├── leetcode/                          # LeetCode の回答
│   └── easy/                          #   難易度別（001_Two-Sum.py など）
├── python/
│   ├── first_commit.py
│   ├── auto_sort.py                   # raw_logs をテーマ別に整理する補助スクリプト
│   ├── library/                       # テーマ別に整理したコード（README.md あり）
│   │   ├── algorithms_data_structures/
│   │   ├── api_http/
│   │   ├── basic_python/
│   │   ├── csv_json_handling/
│   │   ├── data_engineering/
│   │   ├── data_science_ml/
│   │   ├── streamlit_dashboard/
│   │   ├── visualization_geospatial/
│   │   └── visualization_matplotlib/
│   └── raw_logs/                      # 日別の“生コード”置き場
│       └── 2025/MM/DD_slug/           #   例: 2025/08/08_monte/monte.py
└── python30days/                      # 「30 Days Of Python」教材の写経・演習
```

### 3. コミットメッセージ形式
feat:     新機能
fix:      バグ修正
docs:     ドキュメント
chore:    雑務・設定
leetcode: LeetCode（自分ルール）
30days-py:   30-Days-Of-Python（自分ルール）

## この取り組みのポイント
- 毎日の積み重ねでコード力を向上
- 新しい言語・技術の実験場として活用
- Git/GitHub の運用スキル強化
- 振り返りはコミット履歴で行う

参考
John Resig: ["Write Code Every Day"](https://johnresig.com/blog/write-code-every-day/) 
