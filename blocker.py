
# works only for Windows for now
HOSTS_PATH = r"C:\Windows\System32\drivers\etc\hosts"

BLACKLIST = [
        "www.facebook.com"
        ]
REDIRECT = "127.0.0.1"

def block():
    with open(HOSTS_PATH, "r+") as file:
        content = file.read()
        for website in BLACKLIST:
            if website not in content:
                # print(f"Blocking {website}...")
                file.write(f"{REDIRECT} {website}\n")
            
def unblock():
    with open(HOSTS_PATH, "r+") as file:
        content = file.readlines()
        file.seek(0)
        for line in content:
            if not any(website in line for website in BLACKLIST):
                file.write(line)
        file.truncate()

if __name__ == '__main__':
    user_action = input("Block or unblock (b/u)?\n")
    if user_action == 'b':
        block()
    elif user_action == 'u':
        unblock()
    else:
        print("Unknown command")
