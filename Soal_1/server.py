import socket

# Konfigurasi Server
HOST = '127.0.0.1'  # Localhost
PORT = 5050         # Port yang diminta

# Membuat socket TCP/IP
# AF_INET = IPv4, SOCK_STREAM = TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind socket ke alamat dan port
server_socket.bind((HOST, PORT))

# Mulai mendengarkan koneksi (Listen)
server_socket.listen()
print(f"[SERVER] Server berjalan di {HOST}:{PORT}...")

while True:
    # Menerima koneksi dari client
    # conn = objek socket baru untuk komunikasi
    # addr = alamat IP dan port client
    conn, addr = server_socket.accept()
    print(f"[SERVER] Terhubung dengan: {addr}")

    with conn:
        # Menerima data (maksimal 1024 bytes buffer)
        data = conn.recv(1024)
        
        if data:
            pesan = data.decode('utf-8')
            print(f"[SERVER] Pesan diterima: {pesan}")
            
            # Echo: Kirim balik data ke client
            conn.sendall(data) 
            print(f"[SERVER] Pesan dikirim balik (Echo).")
            
    # Loop akan kembali ke atas untuk menunggu client berikutnya
    # (Untuk contoh dasar ini, kita bisa stop manual dengan Ctrl+C)