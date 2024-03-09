import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "21782653")

API_HASH = os.environ.get("API_HASH", "b9516b83f8c00a7b1157c785cfd7aa3e")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7144496753:AAFUeFX5j6bK3weVd1ioE36TcW2Bm8AWVko") 

FORCE_SUB = os.environ.get("FORCE_SUB", "WebXBots") 

DB_NAME = os.environ.get("DB_NAME","ICONEZION")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://iconezion:TOS4k85@Ps8FbNnv@cluster037.dndwcx6.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/Rename-Bot-01-15")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5443243023').split()]

PORT = os.environ.get("PORT", "8080")
