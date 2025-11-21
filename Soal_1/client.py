import socket

# Konfigurasi Target (Harus sama dengan server)
HOST = '127.0.0.1'
PORT = 5050

# Membuat socket TCP/IP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Menghubungkan ke server
    client_socket.connect((HOST, PORT))
    print(f"[CLIENT] Terhubung ke server {HOST}:{PORT}")

    # Mengirim pesan
    pesan = "Tes Koneksi"
    print(f"[CLIENT] Mengirim: {pesan}")
    client_socket.sendall(pesan.encode('utf-8'))

    # Menerima balikan (Echo) dari server
    data = client_socket.recv(1024)
    print(f"[CLIENT] Diterima dari server: {data.decode('utf-8')}")

finally:
    # Menutup koneksi agar resource aman
    print("[CLIENT] Menutup koneksi.")
    client_socket.close()