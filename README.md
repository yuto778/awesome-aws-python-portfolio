# awesome-aws-python-portfolio

# awesome-aws-python-portfolio

> **Portfolio: Python × AWS (Lambda, S3, CSV→JSON, Text Processing)**

## 📝 プロジェクト概要

このリポジトリは、Python と AWS サーバーレスサービスを組み合わせたさまざまな自動化ワークフローをまとめたポートフォリオです。以下の機能を含み、実際の副業案件で使えるレベルの実装例を提供します。

- S3 バケット一覧取得スクリプト
- S3 へのファイルアップロード／ダウンロード
- S3 トリガー → Lambda でファイル取得・加工 → 別バケットに保存
- CSV → JSON 変換ワークフロー
- テキストファイル加工（行番号・文字数・単語数付与）

## 📂 ディレクトリ構成

```text
lambda-functions/
  ├── s3-triggered-processor/
  │   ├── lambda_function.py       # S3→Lambda→加工→別S3保存
  │   ├── requirements.txt         # Python パッケージ一覧
  │   └── event-sample.json        # テスト用サンプルイベント
  └── csv-to-json-converter/
      ├── lambda_function.py       # CSV→JSON変換
      ├── requirements.txt
      └── event-sample.json

scripts/
  ├── list_buckets.py             # S3 バケット一覧取得
  ├── upload_file.py              # ファイルアップロード
  └── download_and_read.py        # ファイルダウンロード・読み込みテスト

diagrams/
  └── architecture.drawio         # アーキテクチャ図（draw.io ファイル）

docs/
  └── deployment_guide.md         # デプロイ手順／IAM 設定例
```

## 🚀 機能一覧

1. **S3 バケット一覧取得**

   ```bash
   python scripts/list_buckets.py
   ```

2. **ファイルアップロード**

   ```bash
   python scripts/upload_file.py --bucket my-bucket --file sample.txt
   ```

3. **S3 トリガー → Lambda 自動処理**

   - `lambda-functions/s3-triggered-processor/lambda_function.py` を AWS Lambda にデプロイ

4. **CSV → JSON 変換**

   - 同ディレクトリ内の `csv-to-json-converter` を利用

5. **テキスト加工 (行番号・文字数・単語数)**

   - `lambda-functions/s3-triggered-processor` の加工ロジックを参考

## ⚙️ 動作環境・前提条件

- Python 3.12
- AWS CLI 設定済み (`aws configure`)
- IAM ポリシー例（S3, Lambda, CloudWatch Logs）:

  ```json
  {
    "Effect": "Allow",
    "Action": [
      "s3:GetObject",
      "s3:PutObject",
      "logs:CreateLogGroup",
      "logs:CreateLogStream",
      "logs:PutLogEvents"
    ],
    "Resource": "*"
  }
  ```

## 📦 デプロイ手順

1. リポジトリをクローン

   ```bash
   git clone https://github.com/yuto778/awesome-aws-python-portfolio.git
   cd awesome-aws-python-portfolio
   ```

2. 各ディレクトリで依存パッケージをインストール

   ```bash
   pip install -r lambda-functions/s3-triggered-processor/requirements.txt
   ```

3. AWS コンソール or SAM CLI で Lambda をデプロイ

## 🎬 実行例

- Lambda テストイベント:

  ```bash
  sam local invoke MyFunction --event lambda-functions/s3-triggered-processor/event-sample.json
  ```

## 📈 今後の拡張案

- Slack 通知連携
- 複数ファイル一括処理
- DynamoDB 保存

## 📄 ライセンス

MIT License
