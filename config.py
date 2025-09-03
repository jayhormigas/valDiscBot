from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
VALORANT_API_KEY = os.getenv("VALORANT_API_KEY")
