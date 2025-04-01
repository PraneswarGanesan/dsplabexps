import datetime
def error_log(error_message):
    with open("d_errorlog.txt", "a") as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{timestamp}] Error: {error_message}")

try:
    x = 1/0

except Exception as e:
    error_log(str(e))

print("Error logged sucessfuly")