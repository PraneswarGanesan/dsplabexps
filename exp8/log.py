import datetime
def log_error(error_message):
    with open("error_log.txt", "a") as log_file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"[{timestamp}] ERROR: {error_message}\n")

try:
    x = 1 / 0 
except Exception as e:
    log_error(str(e))

print("Error logged successfully.")
