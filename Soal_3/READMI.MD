TCP Client dengan Timeout Implementation
Sebuah implementasi client TCP Python yang mendukung timeout untuk koneksi dan penerimaan data, dilengkapi dengan exception handling yang robust.

🚀 Fitur
⏱️ Connection Timeout: Timeout 3 detik saat proses koneksi ke server

📨 Receive Timeout: Timeout 2 detik saat membaca data dari server

🔄 Multiple Attempts: Dukungan percobaan koneksi berulang (pada versi advanced)

🚨 Comprehensive Error Handling: Menangani berbagai skenario error dengan graceful degradation

🔒 Resource Management: Pastikan socket selalu ditutup dengan proper cleanup

📋 Persyaratan
Python 3.6 atau lebih baru

Server TCP yang berjalan pada port 5051 (untuk testing)

🛠️ Cara Menggunakan
1. Basic Client
python
python client_basic.py
Fitur:

Timeout koneksi: 3 detik

Timeout receive: 2 detik

Simple exception handling

2. Advanced Client
python
python client_advanced.py
Fitur Tambahan:

3x percobaan koneksi

Delay antar percobaan

Lebih banyak tipe exception yang ditangani

Logging yang lebih detail

📁 Struktur Kode
Basic Client
python
# 1. Set timeout connection
client_socket.settimeout(3)

try:
    client_socket.connect((HOST, PORT))
    
    # 2. Set timeout receive
    client_socket.settimeout(2)
    response = client_socket.recv(1024)
    
except socket.timeout:
    print("Koneksi timeout!")
Advanced Client
python
# Multiple connection attempts
for attempt in range(1, max_attempts + 1):
    try:
        client_socket.connect((HOST, PORT))
        break
    except socket.timeout:
        print(f"Timeout percobaan ke-{attempt}!")
🧪 Testing Scenario
Server Responsif
text
[CLIENT] Terhubung ke server!
[CLIENT] Mengirim pesan: Halo server...
[CLIENT] Menerima respon dari server: Hello Client!
Server Timeout
text
[CLIENT] Terhubung ke server!
[CLIENT] Mengirim pesan: Halo server...
[CLIENT] Timeout! Server tidak merespons dalam 2 detik.
Connection Timeout
text
[CLIENT] Timeout! Tidak dapat terhubung ke server dalam 3 detik.
Connection Refused
text
[CLIENT] Koneksi ditolak! Pastikan server sedang berjalan.
⚙️ Konfigurasi
Ubah parameter berikut sesuai kebutuhan:

python
HOST = '127.0.0.1'      # Alamat server
PORT = 5051             # Port server
CONNECTION_TIMEOUT = 3  # Timeout koneksi (detik)
RECEIVE_TIMEOUT = 2     # Timeout receive (detik)
MAX_ATTEMPTS = 3        # Maksimal percobaan koneksi
🐛 Troubleshooting
"Koneksi ditolak": Pastikan server sedang berjalan

"Timeout koneksi": Periksa network connectivity dan firewall

"Timeout receive": Server mungkin membutuhkan waktu processing yang lebih lama

📝 Catatan
Timeout values dapat disesuaikan berdasarkan kebutuhan aplikasi

Untuk production, consider menggunakan logging module instead of print statements

Implementasi ini compatible dengan berbagai platform (Windows, Linux, macOS)

🤝 Kontribusi
Silakan fork repository ini dan submit pull request untuk improvements.

📄 License
MIT License - bebas digunakan untuk project personal maupun komersial.
