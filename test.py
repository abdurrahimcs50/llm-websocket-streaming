from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

from langchain_anthropic import ChatAnthropic

from decouple import config

GOOGLE_API_KEY = config("GOOGLE_API_KEY")
print(GOOGLE_API_KEY)

ANTHROPIC_API_KEY = config("ANTHROPIC_API_KEY")
print(ANTHROPIC_API_KEY)

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", api_key=GOOGLE_API_KEY)


llm2 = ChatAnthropic(
    model="claude-3-5-sonnet-20240620",
    anthropic_api_key=ANTHROPIC_API_KEY,
    streaming=True,
)


# # Simple text invocation
result1 = llm.invoke("Sing a ballad of LangChain.")
print(result1.content)
result2 = llm2.invoke("Sing a ballad of LangChain.")
print(result2.content)

# # Multimodal invocation with gemini-pro-vision
# message = HumanMessage(
#     content=[
#         {
#             "type": "text",
#             "text": "What's in this image?",
#         },
#         {"type": "image_url", "image_url": "https://picsum.photos/seed/picsum/200/300"},
#     ]
# )
# result3 = llm.invoke([message])
# print(result3.content)

# result4 = llm2.invoke([message])
# print(result4.content)

