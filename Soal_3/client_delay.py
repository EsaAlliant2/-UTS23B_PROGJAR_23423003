import socket
import sys

HOST = '127.0.0.1'
PORT = 5051

def client_with_timeout():
    # Buat socket client
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 1. Set timeout 3 detik untuk koneksi
    client_socket.settimeout(3)
    
    try:
        print(f"[CLIENT] Mencoba terkoneksi ke {HOST}:{PORT}...")
        client_socket.connect((HOST, PORT))
        print("[CLIENT] Terhubung ke server!")
        
        # Kirim pesan ke server
        message = "Halo server, saya client dengan timeout!"
        client_socket.sendall(message.encode('utf-8'))
        print(f"[CLIENT] Mengirim pesan: {message}")
        
        # 2. Set timeout 2 detik untuk membaca data
        client_socket.settimeout(2)
        
        try:
            # Menerima respon dari server
            response = client_socket.recv(1024)
            print(f"[CLIENT] Menerima respon dari server: {response.decode()}")
            
        except socket.timeout:
            print("[CLIENT] Timeout! Server tidak merespons dalam 2 detik.")
            return
        
    except socket.timeout:
        print("[CLIENT] Koneksi timeout! Tidak dapat terhubung ke server dalam 3 detik.")
        return
        
    except ConnectionRefusedError:
        print("[CLIENT] Koneksi ditolak! Server tidak aktif atau port salah.")
        return
        
    except Exception as e:
        print(f"[CLIENT] Error: {e}")
        return
        
    finally:
        # Tutup socket
        client_socket.close()
        print("[CLIENT] Socket ditutup.")

if __name__ == "__main__":
    client_with_timeout()