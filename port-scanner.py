import socket
import argparse
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

# Scan one port
def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.5)
            result = sock.connect_ex((ip, port))
            if result == 0:
                return port
    except:
        pass
    return None

# Parse command line arguments
def parse_args():
    parser = argparse.ArgumentParser(description="Multithreaded Port Scanner")
    parser.add_argument("-t", "--target", required=True, help="Target IP address")
    parser.add_argument("-s", "--start", type=int, default=1, help="Start port (default: 1)")
    parser.add_argument("-e", "--end", type=int, default=1000, help="End port (default: 1000)")
    return parser.parse_args()

# Main function
def main():
    args = parse_args()
    ip = args.target
    start_port = args.start
    end_port = args.end
    open_ports = []

    print(f"Starting scan on {ip} (ports {start_port}-{end_port}) with 100 threads...\n")
    start_time = time.time()

    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = {executor.submit(scan_port, ip, port): port for port in range(start_port, end_port + 1)}
        for future in as_completed(futures):
            port = futures[future]
            result = future.result()
            if result is not None:
                print(f"[+] Port {result} is open")
                open_ports.append(result)

    duration = round(time.time() - start_time, 2)
    print(f"\nScan completed in {duration} seconds.")
    if open_ports:
        print("Open ports:", ", ".join(map(str, open_ports)))
    else:
        print("No open ports found.")

if __name__ == "__main__":
    main()
