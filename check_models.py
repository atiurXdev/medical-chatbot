import google.generativeai as genai
import os

# --- PASTE YOUR API KEY DIRECTLY BELOW FOR TESTING ---
api_key = "AIzaSyDThGNWxA5OWHq2ktdtRnZJUmoTjlRHebs"
# -----------------------------------------------------

genai.configure(api_key=api_key)

print("Searching for available models...")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(f"FOUND: {m.name}")