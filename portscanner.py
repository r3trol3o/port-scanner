import socket

print("⚡ Starting scan test...")

target = input("Enter IP address or hostname to scan: ")
port = 80
print(f"🎯 Target: {target}, Port: {port}")

sock = socket.socket()
sock.settimeout(5)

try:
    print("📡 Trying to connect...")
    sock.connect((target, port))
    print(f"[+] Port {port} is OPEN on {target}")
except socket.timeout:
    print(f"[!] Port {port} TIMED OUT on {target}")
except ConnectionRefusedError:
    print(f"[-] Port {port} is CLOSED on {target}")
except Exception as e:
    print(f"[x] ERROR: {e}")
finally:
    sock.close()
    print("🔚 Socket closed.")
print("✅ Scan completed.")