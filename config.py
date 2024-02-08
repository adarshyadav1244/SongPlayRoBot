import os
API_ID = int(os.getenv("27412728"))
API_HASH = os.getenv("0ef7db3bf8f66b685cbdbfd82829ae0b")
BOT_TOKEN = os.getenv("6501387330:AAGKnpLVoFCtw1iGhtK6y33idpldVIlT5TI")
DATABASE_URL = os.getenv("DATABASE_URL")
OWNER_ID = list({int(x) for x in os.environ.get("OWNER_ID", "").split()})
