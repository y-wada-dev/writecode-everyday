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

### 2. フォルダ構成
- ルート直下は **テーマ別（言語・技術）ディレクトリ**
- サブディレクトリは `YYYYMMDD_slug` 形式（スラッグは簡潔に）

例：
```markdown
write_code_everyday/
├── Python/
│ ├── 20250808_fizzbuzz/
│ │ └── main.py
│ ├── 20250809_datetime_practice/
│ │ └── main.py
├── JavaScript/
│ └── 20250809_dom_practice/
│ └── index.js
├── docs/
│ └── daily-log.md
└── README.md
```

### 3. コミットメッセージ形式
- `YYYYMMDD_やったこと`
- 例：
20250808_PythonでFizzBuzz実装
20250809_日付処理の練習

### 4. Daily Log
- `docs/daily-log.md` に日ごとの記録を表形式で保存
- commit-msg フックで自動追記

例：
```markdown
| Date       | What                | Path                                      | Tags         |
|------------|---------------------|-------------------------------------------|--------------|
| 2025-08-08 | PythonでFizzBuzz実装 | Python/20250808_fizzbuzz/main.py          | python, kata |
| 2025-08-09 | 日付処理の練習        | Python/20250809_datetime_practice/main.py | datetime     |
```

### 5. commit-msg フック
コミット時に自動で日付を付与し、Daily Logに記録します

コマンド例：`
git commit -m "PythonでFizzBuzz"
`

実際のコミットメッセージ：`
20250808_PythonでFizzBuzz
`

## この取り組みのポイント
- 毎日の積み重ねでコード力を向上
- 新しい言語・技術の実験場として活用
- Git/GitHub の運用スキル強化
- 学習ログとして振り返り可能

参考
John Resig: ["Write Code Every Day"](https://johnresig.com/blog/write-code-every-day/) 