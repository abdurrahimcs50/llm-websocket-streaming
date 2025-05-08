# LLM WebSocket Streaming (FastAPI + LangChain + Gemini & Claude)

---

### Introduction:

A real-time chat-based application that streams responses from multiple LLMs (Google Gemini and Anthropic Claude) using WebSockets, powered by LangChain.

### Features:

* **Real-time streaming**: Multi-LLM responses via WebSocket.
* **Supports Gemini and Claude models**.
* **Modular architecture**: Easy to add more models.
* **FastAPI & WebSocket**: Real-time, low-latency communication.

---

### Getting Started

#### 1. Clone the repository:

```bash
git clone https://github.com/abdurrahimcs50/llm-websocket-streaming.git
cd llm-websocket-streaming
```

#### 2. Install dependencies:

```bash
python3 -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install -r requirements.txt
```

#### 3. Configure API Keys:

Create a `.env` file and add:

```
GOOGLE_API_KEY=your_google_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key
```

#### 4. Run the server:

```bash
uvicorn main:app --reload
```

#### 5. Access the UI:

Go to `http://localhost:8000` in your browser to interact with the models.

---

### How It Works:

* **WebSocket**: Real-time bidirectional communication.
* **LangChain**: Streams responses from LLMs (Gemini, Claude).
* **FastAPI**: Handles WebSocket connections.

---

### Future Improvements:

* Support more LLMs (e.g., GPT-4, Mistral).
* Dockerize for easy deployment.
* Enhance UI for a better user experience.

---

### License:

MIT License - see the [LICENSE](LICENSE) file for details.
