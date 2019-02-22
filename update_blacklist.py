import os
BLACKLIST_PATH = r"C:\Users\Andrey\OneDrive\cloudcbio\python\pomodoro\blocker\blacklist"

def is_empty(path):
    return os.stat(path).st_size == 0

if __name__ == '__main__':
    while True:
        print("Websites in the blacklist:")
        with open(BLACKLIST_PATH, "r+") as file:
            for line in file:
                print(f"\t{line}", end='')
            print()
        user_input = input("Enter\na - to add a website to the blacklist\n"
                           "r - to remove a website from the blacklist\n"
                           "q to quit\n")
        if user_input == 'a':
            website = input("Enter a website to add: ")
            with open(BLACKLIST_PATH, 'a') as file:
                if not is_empty(BLACKLIST_PATH):
                    file.write('\n')
                file.write(website)
        elif user_input == 'r':
            website = input("Enter a website to remove: ")
            with open(BLACKLIST_PATH, "r+") as file:
                content = file.readlines()
                file.seek(0)
                for line in content:
                    if not line.rstrip() == website:
                        file.write(line)
                file.truncate()
        elif user_input == 'q':
            print("Good day!")
            break
        else:
            print("Unknown command")
