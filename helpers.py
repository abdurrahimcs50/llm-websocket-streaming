from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage
from decouple import config
from typing import AsyncGenerator, Callable
import asyncio

GOOGLE_API_KEY = config("GOOGLE_API_KEY")
ANTHROPIC_API_KEY = config("ANTHROPIC_API_KEY")

# Convert sync generator to async
async def to_async_iter(sync_gen) -> AsyncGenerator:
    for item in sync_gen:
        yield item
        await asyncio.sleep(0)


# Streaming wrapper class
class LLMStreamer:
    def __init__(self, name: str, stream_func: Callable[[str], AsyncGenerator]):
        self.name = name
        self.stream_func = stream_func

    async def stream_to_websocket(self, message: str, websocket):
        try:
            async for chunk in self.stream_func(message):
                await websocket.send_text(f"{self.name}: {chunk}")
        except Exception as e:
            await websocket.send_text(f"{self.name}: [Error] {str(e)}")


# Gemini stream generator
def gemini_streamer(message: str) -> AsyncGenerator[str, None]:
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        api_key=GOOGLE_API_KEY,
        model_kwargs={"streaming": True},
    )
    stream = llm.stream([HumanMessage(content=message)])
    return to_async_iter(chunk.content for chunk in stream)


# Claude stream generator
def claude_streamer(message: str) -> AsyncGenerator[str, None]:
    llm = ChatAnthropic(
        model="claude-3-5-sonnet-20240620",
        anthropic_api_key=ANTHROPIC_API_KEY,
        streaming=True,
    )
    stream = llm.stream([HumanMessage(content=message)])
    return to_async_iter(chunk.content for chunk in stream)
