import tls_client, time, colorama

session = tls_client.Session(client_identifier="chrome110",h2_settings={"HEADER_TABLE_SIZE": 65536,"MAX_CONCURRENT_STREAMS": 1000,"INITIAL_WINDOW_SIZE": 6291456,"MAX_HEADER_LIST_SIZE": 262144},random_tls_extension_order=True)
token = ""
webhook = ""
a = []
channel = input("Channel id : ")

def get_url():
    r = session.get(f"https://discord.com/api/v9/channels/{channel}/messages", headers={"authorization": token})
    if r.status_code == 200:
        messages = r.json()
        for message in messages:
            if "attachments" in message:
                for attachment in message['attachments']:
                    if "url" in attachment:
                        print(f"{colorama.Fore.LIGHTGREEN_EX}GET {colorama.Fore.LIGHTYELLOW_EX}- {colorama.Fore.LIGHTWHITE_EX}{attachment['url']}")
                        a.append(attachment['url'])

get_url()
for _ in a:
    r = session.post(webhook, json={"content":_})
    if r.status_code == 204:
        print(f"{colorama.Fore.LIGHTGREEN_EX}SENT {colorama.Fore.LIGHTYELLOW_EX}- {colorama.Fore.LIGHTWHITE_EX}{_}")
    elif "retry_after" in r.text:
        time.sleep(r.json()['retry_after'])
    else:
        print(f"{colorama.Fore.LIGHTRED_EX}FAILED SENT {colorama.Fore.LIGHTYELLOW_EX}- {colorama.Fore.LIGHTWHITE_EX}{_}")