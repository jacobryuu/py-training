# py-training

Python3プロジェクト（Poetryで管理）

アルゴリズムとシステムプログラミングの学習・練習用プロジェクト

## プロジェクト構造

```
py_training/
├── algorithm/          # アルゴリズム実装
│   ├── codesignal/    # CodeSignal問題
│   ├── codility/      # Codility問題
│   ├── leetcode/      # LeetCode問題
│   ├── hackerrank/    # HackerRank問題
│   ├── example/       # アルゴリズム例
│   └── tracks/        # その他
└── system/            # システムプログラミング例
    ├── rate_limit.py
    ├── task_distributor.py
    └── task_scheduler.py
```

## セットアップ

```bash
poetry install
```

## 開発ツール

- **black**: コードフォーマッター（行長88）
- **isort**: import文の自動ソート（blackプロファイル）
- **flake8**: コードスタイルチェック（PEP 8準拠）
- **mypy**: 静的型チェック
- **pytest**: テストフレームワーク
- **pytest-cov**: カバレッジレポート

## 使い方

### コード品質チェック

```bash
# すべてのチェックを実行
poetry run black training/ && \
poetry run isort training/ && \
poetry run flake8 training/ && \
poetry run mypy training/

# または個別に実行
poetry run black training/      # フォーマット
poetry run isort training/      # importソート
poetry run flake8 training/     # スタイルチェック
poetry run mypy training/       # 型チェック
```

### テスト実行

```bash
# すべてのテストを実行
poetry run pytest

# カバレッジレポート付き
poetry run pytest --cov=training --cov-report=html

# 特定のテストファイルのみ
poetry run pytest tests/test_example.py
```

## 設定

- **pyproject.toml**: Poetry設定、ツール設定
- **.flake8**: flake8設定（行長88、E203/W503無視）
- **.gitignore**: Git無視ファイル
