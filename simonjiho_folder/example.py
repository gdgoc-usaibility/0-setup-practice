from dotenv import load_dotenv
import os

# .env 파일 로드
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
print(api_key)