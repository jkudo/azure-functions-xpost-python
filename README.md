# Azure Function for Posting to X (Former Twitter) using Tweepy

This Azure Function provides a REST endpoint that allows you to post to X (Former Twitter) using the Tweepy library. 

## Prerequisites

1. Azure account with the necessary permissions to create and manage Azure Functions.
2. An account on X (Former Twitter) with the necessary permissions to post content. 

## Configuration

1. From your platform's developer or API portal, you will need the following credentials:
   - CONSUMER_KEY
   - CONSUMER_SECRET
   - ACCESS_TOKEN
   - ACCESS_TOKEN_SECRET

2. Set these credentials as environment variables in your Azure Function App settings.

## Usage 

- Send a POST request to the function endpoint with the following JSON payload:

```json
{
    "message": "Your content for X here"
}
```

- If the post is successfully made to X, you will receive a response with the content of the post. 
- If there's an error or an invalid JSON format, appropriate error messages will be returned.

## Error Handling

- If you provide an invalid JSON format, you will get a response with the message "Invalid JSON format".
  
- If the `message` field is missing from your request, the response will indicate that you should provide a message.

- Any Tweepy-specific errors (like rate limiting or invalid credentials) will be returned in the response.

## Development Notes

- The function uses the Tweepy library to interact with the X platform's API. The code handles authentication and content posting.

- Logging is implemented to provide insights on function execution.

## Final Thoughts

Make sure your credentials are kept secure. Do not expose them in your code. Always use environment variables or other secure methods to store and retrieve sensitive data.


---
Japanese Support

# Azure Functionを使用してTweepyライブラリを使用してX (旧Twitter) に投稿する

このAzure Functionは、Tweepyライブラリを使用してX (旧Twitter) に投稿するためのRESTエンドポイントを提供します。

## 前提条件

1. Azure Functionsの作成と管理に必要な権限を持つAzureアカウント。
2. コンテンツを投稿するための必要な権限を持つX (旧Twitter) のアカウント。

## 設定

1. あなたのプラットフォームの開発者またはAPIポータルから、次の資格情報が必要です：
   - CONSUMER_KEY
   - CONSUMER_SECRET
   - ACCESS_TOKEN
   - ACCESS_TOKEN_SECRET

2. これらの資格情報をAzure Function Appの設定の環境変数として設定します。

## 使用方法 

- 以下のJSONペイロードを持つPOSTリクエストを機能エンドポイントに送信します：

```json
{
    "message": "Xへのあなたのコンテンツはこちら"
}
```

- Xへの投稿が成功した場合、投稿の内容を含むレスポンスが返されます。
- エラーまたは無効なJSON形式がある場合、適切なエラーメッセージが返されます。

## エラーハンドリング

- 無効なJSON形式を提供した場合、"Invalid JSON format"というメッセージのレスポンスが返されます。
  
- リクエストから`message`フィールドが欠落している場合、メッセージを提供するようにというレスポンスが示されます。

- Tweepy固有のエラー（レート制限や無効な資格情報など）は、レスポンスに返されます。

## 開発ノート

- 機能はTweepyライブラリを使用してXプラットフォームのAPIとやりとりします。コードは認証とコンテンツの投稿を処理します。

- ロギングは、機能の実行に関する洞察を提供するために実装されています。

## 最後に

資格情報を安全に保管してください。コード内でそれらを公開しないでください。常に環境変数や他の安全な方法を使用して、機密データを保存および取得してください。