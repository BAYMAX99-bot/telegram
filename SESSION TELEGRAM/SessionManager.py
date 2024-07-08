from telegram import SessionManager

SessionManager.telethon(session_file=True)

def process_message(menyala):
    # Contoh logika pemrosesan
    response = f"Kamu mengirim pesan: {menyala}"
    return response
