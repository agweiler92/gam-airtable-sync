from dotenv import load_dotenv
import os

load_dotenv()

GOOGLE_APPLICATION_CREDENTIALS = os.getenv(
    "GOOGLE_APPLICATION_CREDENTIALS"
)

NETWORK_CODE = os.getenv("GAM_NETWORK_CODE")