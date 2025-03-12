import datetime

# Function to log errors
def log_error(error_message):
    with open("error_log.txt", "a") as log_file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"[{timestamp}] ERROR: {error_message}\n")

# Example usage
try:
    x = 1 / 0  # Intentional error
except Exception as e:
    log_error(str(e))

print("Error logged successfully.")
