import socket
import argparse
import threading

def scan_port(ip, port, verbose):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)
        result = s.connect_ex((ip, port))
        if result == 0:
            print(f"[+] Port {port} ouvert")
            return True
        elif verbose:
            print(f"[-] Port {port} fermé")
    return False

def thread_scan(ip, start_port, end_port, verbose, open_ports):
    threads = []
    for port in range(start_port, end_port + 1):
        t = threading.Thread(target=lambda p=port: open_ports.append(p) if scan_port(ip, p, verbose) else None)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

parser = argparse.ArgumentParser(description="Scanner de ports TCP")
parser.add_argument('--ip', required=True, help="Adresse IP")
parser.add_argument('--start-port', type=int, required=True, help="Port de début")
parser.add_argument('--end-port', type=int, required=True, help="Port de fin")
parser.add_argument('--verbose', action='store_true', help="Afficher aussi les ports fermés")

args = parser.parse_args()

open_ports = []
thread_scan(args.ip, args.start_port, args.end_port, args.verbose, open_ports)
