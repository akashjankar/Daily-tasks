LOG_FILE = "E:\\Report\\program\\task-1\\small.log"


def read_logs():
    with open(LOG_FILE, "r") as f:
        return f.readlines()


def show_log_counts():
    counts = {"ERROR": 0, "WARN": 0, "INFO": 0}

    for line in read_logs():
        for level in counts:
            if level in line:
                counts[level] += 1

    print("ERROR =", counts["ERROR"])
    print("WARN  =", counts["WARN"])
    print("INFO  =", counts["INFO"])





def search_by_time_range(date, start_time, end_time):
    for line in read_logs():
        log_date = line[1:11]
        log_time = line[12:20]

        if log_date == date and start_time <= log_time <= end_time:
            print(line.strip())


while True:
    print("\n--- LOG ANALYZER ---")
    print("1. Show ERROR / WARN / INFO count")
    print("2. Search logs by time range")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_log_counts()

    elif choice == "2":
        d = input("Enter date (yyyy-mm-dd): ")
        st = input("Enter start time (hh:mm:ss): ")
        et = input("Enter end time (hh:mm:ss): ")
        search_by_time_range(d, st, et)

    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")
