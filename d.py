import tls_client, time, colorama

req = tls_client.Session(client_identifier="chrome110",h2_settings={"HEADER_TABLE_SIZE": 65536,"MAX_CONCURRENT_STREAMS": 1000,"INITIAL_WINDOW_SIZE": 6291456,"MAX_HEADER_LIST_SIZE": 262144},random_tls_extension_order=True)
a = "token"
b = "webhook url"
c = []
d = input("Channel id : ")

def get_url():
    r = req.get(f"https://discord.com/api/v9/channels/{d}/messages", headers={"authorization": a})
    if r.status_code == 200:
        for i in r.json():
            if "attachments" in i:
                for _ in i['attachments']:
                    if "url" in _:
                        print(f"{colorama.Fore.LIGHTGREEN_EX}GET {colorama.Fore.LIGHTYELLOW_EX}- {colorama.Fore.LIGHTWHITE_EX}{_['url']}")
                        c.append(_['url'])

get_url()
for _ in c:
    r = session.post(b, json={"content":_})
    if r.status_code == 204:
        print(f"{colorama.Fore.LIGHTGREEN_EX}SENT {colorama.Fore.LIGHTYELLOW_EX}- {colorama.Fore.LIGHTWHITE_EX}{_}")
    elif "retry_after" in r.text:
        time.sleep(r.json()['retry_after'])
    else:
        print(f"{colorama.Fore.LIGHTRED_EX}FAILED SENT {colorama.Fore.LIGHTYELLOW_EX}- {colorama.Fore.LIGHTWHITE_EX}{_}")
