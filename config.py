
CONFIG_PATH = r"C:\Users\Andrey\OneDrive\cloudcbio\python\pomodoro\blocker\config.bin"

def load_configuration():
    with open(CONFIG_PATH, "rb") as file:
        byte = file.read(1)
        return bool(int.from_bytes(byte, "little"))

def save_configuration(is_blocked):
    with open(CONFIG_PATH, "wb") as file:
        byte_arr = [int(is_blocked)]
        bin_format = bytearray(byte_arr)
        file.write(bin_format)

if __name__ == '__main__':
    state = load_configuration()
    print(f"State: {state}")    
    if state:
        overwrite = input("Overwrite? (y/any other key) ") == 'y'
        if overwrite:
            save_configuration(False)

