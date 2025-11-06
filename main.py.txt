from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.post("/slack/events")
async def slack_events(request: Request):
    body = await request.json()
    
    # Slackの検証リクエストに対応
    if body.get("type") == "url_verification":
        return PlainTextResponse(content=body.get("challenge"))

    # 通常のイベント処理（今は空でOK）
    return {"status": "ok"}