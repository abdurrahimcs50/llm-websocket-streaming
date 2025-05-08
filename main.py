from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from helpers import LLMStreamer, gemini_streamer, claude_streamer
import asyncio

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    streamers = [
        LLMStreamer("Gemini", gemini_streamer),
        LLMStreamer("Claude", claude_streamer),
    ]

    try:
        while True:
            message = await websocket.receive_text()
            await websocket.send_text(f"🟢 Received: {message}")

            tasks = [s.stream_to_websocket(message, websocket) for s in streamers]
            await asyncio.gather(*tasks)

            await websocket.send_text("✅ Done: All model outputs received.")
    except WebSocketDisconnect:
        print("🔌 Client disconnected")


# Basic UI
html = """
<!DOCTYPE html>
<html>
<head>
    <title>LLM WebSocket Streaming (FastAPI + LangChain + Gemini & Claude)</title>
    <style>
        body { font-family: Arial; padding: 20px; background: #f9f9f9; }
        #chat { background: #fff; border: 1px solid #ccc; padding: 10px; height: 400px; overflow-y: scroll; }
        input { width: 300px; padding: 10px; }
        button { padding: 10px 20px; }
    </style>
</head>
<body>
    <h2>LLM WebSocket Streaming (FastAPI + LangChain + Gemini & Claude)</h2>
    <input id="messageInput" placeholder="Enter message" />
    <button onclick="sendMessage()">Send</button>
    <pre id="chat"></pre>

    <script>
        const chatBox = document.getElementById("chat");
        const ws = new WebSocket("ws://localhost:8000/ws");

        ws.onmessage = (event) => {
            chatBox.textContent += event.data + "\\n";
            chatBox.scrollTop = chatBox.scrollHeight;
        };

        function sendMessage() {
            const input = document.getElementById("messageInput");
            ws.send(input.value);
            input.value = "";
        }
    </script>
</body>
</html>
"""

@app.get("/")
async def get():
    return HTMLResponse(html)

