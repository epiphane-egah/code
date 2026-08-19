from dotenv import load_dotenv
import os

load_dotenv()

print(os.environ.get("key"))
print(os.getenv("key"))