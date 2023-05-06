import socket
import re
import concurrent.futures

hosts = ['18.118.4.70', '3.17.173.104', '52.90.180.170', '3.145.99.169', '3.21.97.146']

pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
port = 3389

new = []
def testIp(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((host, port))
        if result == 0:
            #new.append(f"Port {port} is open on {host}")
            with open('freshh.txt', 'a') as f:
                f.write(f"{host}\n")
            return f"Port {port} is open on {host}"
        else:
            return f"Port {port} is closed on {host}"
    except Exception as e:
        print(f"Error connecting to {host}:{port}: {e}")
    finally:
        sock.close()

results = []
with open("/home/mk/daemon7/rdp_scripts/portscanner/fresh9.txt") as f:
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        for i in f:
            match = re.search(pattern, i)
            if match:
                results.append(executor.submit(testIp, match.group(0), port))

        for f in concurrent.futures.as_completed(results):
            print(f.result())

print(new)

