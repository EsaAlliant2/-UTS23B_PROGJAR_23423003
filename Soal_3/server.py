import socket
import time

# Konfigurasi (Harus sama dengan Client)
HOST = '127.0.0.1'
PORT = 5051

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"[SERVER] Server berjalan di {HOST}:{PORT}...")
print("[SERVER] Server ini akan sengaja LAMBAT membalas pesan.")

while True:
    # Menerima koneksi
    conn, addr = server_socket.accept()
    print(f"[SERVER] Client terhubung: {addr}")

    with conn:
        data = conn.recv(1024)
        if data:
            print(f"[SERVER] Pesan diterima: {data.decode('utf-8')}")
            
            # --- SIMULASI DELAY ---
            print("[SERVER] Menunggu 5 detik sebelum membalas...")
            time.sleep(5) 
            # Delay 5 detik > Timeout Client 2 detik
            # Akibatnya Client akan Error Timeout
            
            pesan_balasan = "Halo, maaf saya telat balas!"
            conn.sendall(pesan_balasan.encode('utf-8'))
            print("[SERVER] Balasan dikirim (meskipun client mungkin sudah putus).")