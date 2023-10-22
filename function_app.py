# 必要なライブラリをインポートする
import azure.functions as func
import os
import logging
import tweepy

# Azure Functionsの設定を行う。認証レベルはFUNCTIONに設定。
app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

# Twitter Developer Portalから取得したキーを環境変数から読み込む
client = tweepy.Client(
    consumer_key = os.environ["CONSUMER_KEY"],
    consumer_secret = os.environ["CONSUMER_SECRET"],
    access_token = os.environ["ACCESS_TOKEN"],
    access_token_secret = os.environ["ACCESS_TOKEN_SECRET"]
)

# http_triggerという名前のエンドポイントを設定し、POSTメソッドを受け付けるようにする
@app.route(route="http_trigger", methods=["POST"])
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    # リクエストが処理されたことをログに記録
    logging.info('Python HTTP trigger function processed a request.')

    # リクエストからJSONを取得しようとする。失敗した場合はエラーメッセージを返す。
    try:
        req_body = req.get_json()
    except ValueError:
        return func.HttpResponse(
            "Invalid JSON format",
            status_code=400
        )

    # JSONからメッセージを取得
    message = req_body.get('message')

    # メッセージが存在する場合、ツイートを投稿しようとする
    if message:
        try:
            tweet_response = client.create_tweet(text=message)
            return func.HttpResponse(f"Post: {message}")
        # ツイートの投稿に失敗した場合はエラーメッセージを返す
        except tweepy.TweepError as e:
            return func.HttpResponse(f"Failed to Post: {e.response.text}", status_code=400)
    # メッセージが存在しない場合、エラーメッセージを返す
    else:
        return func.HttpResponse(
            "Please provide a message in the request body for a personalized tweet.",
            status_code=400
        )
