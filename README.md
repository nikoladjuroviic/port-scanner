
# 🛡️ Advanced Port Scanner

A simple, fast, multithreaded port scanner written in Python.  
It scans a range of ports on a given IP address using 100 threads to speed up the process.

---

## ⚙️ Features

- Multithreaded scanning (100 threads)
- Custom IP address and port range
- Clean and readable CLI output
- Measures total scan time
- Python 3 compatible

---

## 🚀 Usage

### ✅ 1. Clone the repo or copy the script

```bash
git clone https://github.com/your-username/port-scanner.git
cd port-scanner
```

Or just download `advanced_port_scanner.py`.

---

### ✅ 2. Run the scanner

```bash
python3 advanced_port_scanner.py -t <target_ip> [-s <start_port>] [-e <end_port>]
```

#### 🔸 Arguments:

| Argument      | Description                            | Required | Default  |
|---------------|----------------------------------------|----------|----------|
| `-t, --target` | Target IP address (e.g. 127.0.0.1)     | ✅       | —        |
| `-s, --start`  | Start port (e.g. 1)                    | ❌       | 1        |
| `-e, --end`    | End port (e.g. 1000)                   | ❌       | 1000     |

---

### ✅ 3. Example usage

```bash
python3 advanced_port_scanner.py -t 127.0.0.1
python3 advanced_port_scanner.py -t 192.168.0.1 -s 20 -e 100
```

---

## 📦 Requirements

No external libraries needed — only Python’s built-in modules:
- `socket`
- `argparse`
- `time`
- `concurrent.futures`

---

## 🧠 Legal Warning

> ⚠️ This tool is for **educational and ethical testing purposes only**.  
> Do not scan IPs or networks you don't own or have explicit permission to test.

---

## 👨‍💻 Author

Made by Džony — with focus, discipline and caffeine. ☕
