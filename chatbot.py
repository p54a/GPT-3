import openai
import asyncio
import re
import speech_recognition as sr

# Set up OpenAI API credentials
openai.api_key = "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"

# Create a recognizer object for speech recognition
recognizer = sr.Recognizer()

async def main():
    while True:
        # Get user input through speech
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)
            
        try:
            # Convert speech to text
            user_input = recognizer.recognize_google(audio)
            print("You said:", user_input)
            
            # Send user input to OpenAI API
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=user_input,
                max_tokens=50,
                n=1,
                stop=None,
                temperature=0.7
            )
            
            # Get the chatbot's response
            bot_response = response.choices[0].text.strip()
            print("Bot:", bot_response)
            
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that. Could you please repeat?")
        except sr.RequestError as e:
            print("Speech recognition request error:", str(e))
            
        # Perform any other actions or logic based on the bot response
        
        # Add a break condition or exit condition if desired

if __name__ == "__main__":
    asyncio.run(main())
