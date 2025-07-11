# 🌍 AI Travel Designer Agent
An intelligent travel planning assistant built using **Chainlit**, **Google Gemini 1.5**, and **multi-agent architecture** to help users plan customized vacations — from beach getaways to cultural adventures! ✨✈️🍱🏝️

---

## 🧠 Features

### 🗺️ AI-Powered Destination Suggestions
Recommends ideal travel spots based on user moods or preferences (like relaxing, romantic, adventurous).

### ✈️ Mock Booking System
Provides simulated flight deals and hotel options (luxury to budget) using built-in tools.

### 🍱 Explore Attractions & Food
Suggests cultural experiences, top attractions, and popular local dishes.

### 🤖 Multi-Agent System
Uses 3 intelligent agents:
- `DestinationAgent`: Picks destination 🎯
- `BookingAgent`: Finds flights + hotels 🛫🏨
- `ExploreAgent`: Lists food & fun activities 🍜🗺️

### 💻 Powered by Chainlit UI
Interactive chatbot interface built with Chainlit for real-time vacation planning experience.

---

## 🛠️ Tech Stack
| Layer          | Technologies Used                                  |
|----------------|-----------------------------------------------------|
| **AI Model**    | Google Gemini 1.5 Flash                            |
| **Frontend**    | Chainlit (chat UI framework)                       |
| **Backend**     | Python, dotenv                                     |
| **Agents**      | DestinationAgent, BookingAgent, ExploreAgent       |
| **Tools**       | get_flights.py, suggest_hotels.py                  |

---

## 🚀 Getting Started

### 📦 Requirements
- Python 3.10+
- Valid Gemini API Key

### 🔧 Setup Instructions
```bash
# 1. Clone the repository
$ git clone https://github.com/your-username/ai-travel-agent.git
$ cd ai-travel-agent

# 2. Create virtual environment
$ python -m venv venv
$ venv\Scripts\activate      # Windows
# OR
$ source venv/bin/activate    # macOS/Linux

# 3. Install dependencies
$ pip install chainlit google-generativeai python-dotenv
```

### 🔐 Add Environment Key
Create a `.env` file:
```env
GEMINI_API_KEY=your_gemini_api_key_here
```

### ▶️ Run the App
```bash
chainlit run main.py
```

---

## 📁 Folder Structure
```bash
ai-travel-agent/
├── .env                         # Gemini API Key
├── main.py             # Core logic and UI
├── travel_agents/
│   ├── destination_agent.py     # Suggests destination
│   ├── booking_agent.py         # Simulated flights & hotels
│   └── explore_agent.py         # Local food & activities
├── tools/
│   ├── get_flights.py           # Mock flight deals
│   └── suggest_hotels.py        # Mock hotel deals
```

---

## 💡 Sample Input Examples
```text
I want a romantic vacation in nature 🌿
I need a beach with good food 🌊🍱
Show me a peaceful mountain escape 🏔️
```

## 🙋‍♀️ Created By
Javeria Fatima — 💖 Crafted with creativity, logic, and wanderlust!
