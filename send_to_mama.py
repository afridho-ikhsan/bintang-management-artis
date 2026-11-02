import json
import urllib.request
import time

chat_id = "23928017789133@lid"

# 1. Send Updated Media (PDF Report)
pdf_payload = json.dumps({
    "chatId": chat_id,
    "filePath": "/home/hermesagent/obsidian-vault/projects/Laporan_Website_Management_Artis_Mama.pdf",
    "mediaType": "document",
    "fileName": "Laporan_Website_Management_Artis.pdf",
    "caption": "mak, ini tampilan web nya udah edo rapihin lagi yaa mak. jarak tombol sama tulisannya udah dibikin lebih lega dan rapi biar enak dilihat di hp, terus bahasanya udah dibikin resmi standar agensi. ada bukti penjelasannya di dalem pdf ini yaa mak"
}).encode("utf-8")

req1 = urllib.request.Request(
    "http://127.0.0.1:3005/send-media",
    headers={"Content-Type": "application/json"},
    data=pdf_payload
)

try:
    with urllib.request.urlopen(req1, timeout=20) as resp:
        print("Send PDF:", resp.read().decode())
except Exception as e:
    print("Error PDF:", e)

time.sleep(2)

# 2. Send Text for Website Link
msg_text = """trus ini link web terbarunya yaa mak:
https://afridho-ikhsan.github.io/bintang-management-artis/

tampilannya udah makin rapi dan udah online mak, nanti bisa ditunjukin ke bunda mega sama saiful yaa mak"""

text_payload = json.dumps({
    "chatId": chat_id,
    "message": msg_text
}).encode("utf-8")

req2 = urllib.request.Request(
    "http://127.0.0.1:3005/send",
    headers={"Content-Type": "application/json"},
    data=text_payload
)

try:
    with urllib.request.urlopen(req2, timeout=15) as resp:
        print("Send Text:", resp.read().decode())
except Exception as e:
    print("Error Text:", e)
