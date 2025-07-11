import chainlit as cl
import google.generativeai as genai
from dotenv import load_dotenv
import os

from destination_agent import DestinationAgent
from booking_agent import BookingAgent
from explore_agent import ExploreAgent

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

destination_agent = DestinationAgent(model)
booking_agent = BookingAgent()
explore_agent = ExploreAgent(model)

@cl.on_chat_start
async def start():
    await cl.Message(content="👋 Hello! I'm your AI Travel Designer 🌍✈️\n\nTell me your dream vacation idea, mood, or interest and I’ll plan it for you! 💭🏝️\n\nExample: 'I want a peaceful mountain trip' or 'I love beaches with good food' 🍱☀️").send()

@cl.on_message
async def main(message: cl.Message):
    user_input = message.content.strip().lower()

    if user_input in ["thank you", "thanks", "shukriya"]:
        await cl.Message(content="You're welcome! 😊 Let me know if you want more help!").send()
        return

    cl.user_session.set("input", user_input)
    cl.user_session.set("step", "destination")

    destination_raw = destination_agent.run(user_input)

    destination_name = ""
    for line in destination_raw.splitlines():
        if line.startswith("Destination:"):
            destination_name = line.replace("Destination:", "").strip()
            break

    cl.user_session.set("destination", destination_name)

    await cl.Message(content=f"🌍 {destination_raw}").send()

    booking_info = booking_agent.run(destination_name)
    await cl.Message(content=booking_info).send()

    explore = explore_agent.run(destination_name)
    await cl.Message(content=f"🎒 Here's what you can explore in {destination_name}:").send()
    await cl.Message(content=explore).send()
