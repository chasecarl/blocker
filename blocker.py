import config

# works only for Windows for now
HOSTS_PATH = r"C:\Windows\System32\drivers\etc\hosts"
BLACKLIST_PATH = r"C:\Users\Andrey\OneDrive\cloudcbio\python\pomodoro\blocker\blacklist"

REDIRECT = "127.0.0.1"

def load_blacklist():
    with open(BLACKLIST_PATH, 'r') as file:
        return file.readlines()

def block():
    blacklist = load_blacklist()
    with open(HOSTS_PATH, "r+") as file:
        content = file.read()
        for website in blacklist:
            if website not in content:
                # print(f"Blocking {website}...")
                file.write(f"{REDIRECT} {website}")
    config.save_configuration(True)
            
def unblock():
    blacklist = load_blacklist()
    with open(HOSTS_PATH, "r+") as file:
        content = file.readlines()
        file.seek(0)
        for line in content:
            if not any(website in line for website in blacklist):
                file.write(line)
        file.truncate()
    config.save_configuration(False)

if __name__ == '__main__':
    is_blocked = config.load_configuration()
    state = "blocked" if is_blocked else "unblocked" 
    print(f"State: {state}")
    user_action = input("Block or unblock (b/u)?\n")
    if user_action == 'b':
        if not is_blocked:
            block()
    elif user_action == 'u':
        if is_blocked:
            unblock()
    else:
        print("Unknown command")
