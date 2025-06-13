import json
import csv
import boto3
from io import StringIO

# CSVを読み込み、JSONに変換して別バケットに保存するLambda関数
s3 = boto3.client('s3')

def lambda_handler(event, context):
    # 1. トリガー元バケット・キーの取得
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    source_key    = event['Records'][0]['s3']['object']['key']

    # 2. CSVファイル取得
    response = s3.get_object(Bucket=source_bucket, Key=source_key)
    body     = response['Body'].read().decode('utf-8')

    # 3. CSVパース
    csv_reader = csv.DictReader(StringIO(body))
    rows       = [row for row in csv_reader]

    # 4. JSON文字列化
    json_data = json.dumps(rows, ensure_ascii=False)

    # 5. 保存先バケットとキーを設定
    dest_bucket = 'your-destination-bucket'  # ← 実際のバケット名に変更してください
    output_key  = 'json/' + source_key.rsplit('.', 1)[0] + '.json'

    # 6. 別バケットにJSONを保存
    s3.put_object(
        Bucket=dest_bucket,
        Key=output_key,
        Body=json_data.encode('utf-8'),
        ContentType='application/json'
    )

    # 7. ログ出力
    print(f'JSON file saved to {dest_bucket}/{output_key}')

    return {
        'statusCode': 200,
        'body': json.dumps('CSV→JSON変換完了')
    }
