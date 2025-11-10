from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
import requests

app = FastAPI()

# Slack Webhook URL（実際のURLに置き換えてください）
SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/XXX/YYY/ZZZ"

@app.post("/slack/events")
async def slack_events(request: Request):
    body = await request.json()

    # SlackのURL検証（初回設定時に必要）
    if body.get("type") == "url_verification":
        return PlainTextResponse(content=body.get("challenge"))

    # 通常のイベント処理（例：メッセージ受信）
    event = body.get("event", {})
    user = event.get("user", "unknown")
    text = event.get("text", "No message received")

    # Slack通知メッセージの構築
    message = f"Slackイベント受信：{user} が「{text}」と発言しました。"

    # Slack Webhookに送信
    response = requests.post(SLACK_WEBHOOK_URL, json={"text": message})

    # レスポンス確認（任意でログ出力などに拡張可能）
    if response.status_code != 200:
        return {"status": "error", "detail": response.text}

    return {"status": "sent"}
Slack通知テスト by Masaru
SlackTes
SlackTEST12
