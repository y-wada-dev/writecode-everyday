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
- やったことは`docs/daily-log.md`に残す

### 2. フォルダ構成
- ルート直下は **テーマ別（言語・技術）ディレクトリ**
- サブディレクトリは `theme/YYYYMMDD_slug` 形式（スラッグは簡潔に）

例：
```markdown
write_code_everyday/
├── career.md
├── docs/
│   └── daily-log.md
├── python/
│   ├── library/                       # テーマ別に整理したコード
│   │   ├── algorithms_data_structures/
│   │   ├── api_http/
│   │   ├── basic_python/
│   │   ├── csv_json_handling/
│   │   ├── data_engineering/
│   │   ├── data_science_ml/
│   │   ├── visualization_geospatial/
│   │   └── visualization_matplotlib/
│   ├── raw_logs/                      # (旧)日別の“生コード”置き場
│   └── first_commit.py
└── README.md
```

### 3. コミットメッセージ形式
feat:     新機能
fix:      バグ修正
docs:     ドキュメント
chore:    雑務・設定
leetcode: LeetCode（自分ルール）
30days-py:   30-Days-Of-Python（自分ルール）

### 4. Daily Log
- `docs/daily-log.md` に日ごとの記録を表形式で保存

例：
```markdown
--
## YYYY/MM/DD

### What I Did
-

### Learnings
-

### Next Action
-
# Archive: Auto-Generated File Logs（旧ログ保管庫）
| Date       | What                | Path                                      | Tags         |
|------------|---------------------|-------------------------------------------|--------------|
| 2025-08-08 | PythonでFizzBuzz実装 | Python/20250808_fizzbuzz/main.py          | python, kata |
| 2025-08-09 | 日付処理の練習        | Python/20250809_datetime_practice/main.py | datetime     |
```

## この取り組みのポイント
- 毎日の積み重ねでコード力を向上
- 新しい言語・技術の実験場として活用
- Git/GitHub の運用スキル強化
- 学習ログとして振り返り可能

参考
John Resig: ["Write Code Every Day"](https://johnresig.com/blog/write-code-every-day/) 
