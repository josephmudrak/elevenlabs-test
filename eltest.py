import os
import requests

from dotenv import load_dotenv

load_dotenv()  # Load environment variables

api_key = os.environ.get("ELEVENLABS_API_KEY")

voice_id = "oWAxZDx7w5VEj9dCyTzz"  # Grace

CHUNK_SIZE = 1024
url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

headers = {
    "Accept": "audio/mpeg",
    "Content-Type": "application/json",
    "xi-api-key": api_key,
}

data = {
    "text": "The FitnessGram™ Pacer Test is a multistage aerobic capacity test \
		that progressively gets more difficult as it continues. The 20 meter \
		pacer test will begin in 30 seconds. Line up at the start. The running \
		speed starts slowly, but gets faster each minute after you hear this \
		signal.",
    "model_id": "eleven_monolingual_v1",
    "voice_settings": {"stability": 0.5, "similarity_boost": 0.5},
}

response = requests.post(url, json=data, headers=headers)

with open("out.mp3", "wb") as f:
    for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
        if chunk:
            f.write(chunk)

print("Output saved as out.mp3")
