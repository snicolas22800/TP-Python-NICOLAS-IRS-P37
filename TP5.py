import psutil
import os
import time
import platform

def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def display_dashboard():
    try:
        while True:
            clear_screen()

            cpu_total = psutil.cpu_percent(interval=1)
            cpu_per_core = psutil.cpu_percent(percpu=True)
            print("=== Utilisation CPU ===")
            print(f"Total CPU : {cpu_total}%")
            for i, usage in enumerate(cpu_per_core):
                bar = "|" * int(usage / 2)
                print(f"CPU Core {i+1} : {usage}% [{bar}]")
            print()

            mem = psutil.virtual_memory()
            print("=== RAM ===")
            print(f"Totale : {mem.total / 1_000_000_000:.2f} Go")
            print(f"Utilisée : {mem.used / 1_000_000_000:.2f} Go")
            print(f"Libre : {mem.available / 1_000_000_000:.2f} Go")
            print()

            print("=== Disques ===")
            partitions = psutil.disk_partitions()
            for p in partitions:
                try:
                    usage = psutil.disk_usage(p.mountpoint)
                    print(f"{p.device} ({p.mountpoint}) : {usage.percent}% utilisé")
                except PermissionError:
                    continue
            print()

            net = psutil.net_io_counters()
            print("=== Network ===")
            print(f"Octets envoyés : {net.bytes_sent / 1_000_000:.2f} Mo")
            print(f"Octets reçus : {net.bytes_recv / 1_000_000:.2f} Mo")
            print(f"Paquets envoyés : {net.packets_sent}")
            print(f"Paquets reçus : {net.packets_recv}")
            print()

            print("=== Network par interface ===")
            net_if = psutil.net_io_counters(pernic=True)
            for iface, stats in net_if.items():
                print(f"{iface} : {stats.bytes_sent / 1_000_000:.2f} Mo envoyés | {stats.bytes_recv / 1_000_000:.2f} Mo reçus")

            print("\nTapez CTRL+C pour quitter.")
            time.sleep(5)
    except KeyboardInterrupt:
        print("\nArrêt du programme.")

if __name__ == "__main__":
    display_dashboard()
