# Chat with Hitesh (Chai aur Code Persona)
A Conversational Chatbot using Streamlit & Gemini API

Overview

Chat with Hitesh is an interactive AI chatbot inspired by Hitesh Choudhary's (Chai aur Code) unique teaching style and persona. Built using Streamlit and Google's Gemini API, this project lets users chat in Hinglish and get responses that reflect Hitesh's motivational, practical, and relatable coding advice.
---
Tech Stack: Python, Streamlit, Gemini API

Features:

    Real-time chat interface

    Hinglish persona responses

    Chat history

    Easy deployment and customization

Demo

    Launch the app locally and chat with "Hitesh" about coding, careers, motivation, or tech doubts—just like his YouTube sessions!

Getting Started:

1. Clone the Repository
    
        git clone https://github.com/sbndAbhijeet/Persona-of-my-Sir-Hitesh_Choudary-
    

2. Set Up Environment
        Create a virtual environment and activate it:

        python3 -m venv venv
        .venv/Scripts/activate

3. Install Dependencies

        pip install -r requirements.txt

4. Configure Gemini API Key
        
        Get your Gemini API key from Google AI Studio

        Create a .env file in the project root:

        GOOGLE_API_KEY=your_gemini_api_key_here
5. Run the App

        streamlit run app.py
        Open http://localhost:8501 in your browser.

Usage
Type your question in Hinglish or English (e.g., "Sir, mujhe coding boring lagti hai, kya karun?").

Press Enter.

Get a response in Hitesh's signature style—motivational, practical, and full of chai analogies!

Chat history is displayed for context and continuity.

Project Structure

    project-root/
    ├── app.py                # Streamlit app code
    ├── requirements.txt      # Python dependencies
    ├── .env                  # Your Gemini API 
    ├── images/               # Image assets
    └── backend/
        └── chat_handler.py     
---
### Customization Persona:

        The chatbot is fine-tuned (via prompt engineering) to reply like Hitesh Choudhary, using Hinglish, real-world coding advice, and relatable analogies.

Extend:

        Add more few-shot examples to the prompt for richer responses.

