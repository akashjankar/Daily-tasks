from concurrent.futures import ThreadPoolExecutor
import re


def analyze_logs_parallel(log_files):
    def analyze_single_file(file_path):
        info = warn = error = 0

        with open(file_path, "r") as file:
            for line in file:
                if "INFO" in line:
                    info += 1
                elif "WARN" in line:
                    warn += 1
                elif "ERROR" in line:
                    error += 1

        return file_path, info, warn, error

    with ThreadPoolExecutor(max_workers=len(log_files)) as executor:
        results = executor.map(analyze_single_file, log_files)

    print("\n===== LOG LEVEL COUNT REPORT =====")
    for file_name, info, warn, error in results:
        print(f"\nFile: {file_name}")
        print(f"INFO  : {info}")
        print(f"WARN  : {warn}")
        print(f"ERROR : {error}")



def regex_search_logs(log_files):
    pattern = input("\nEnter search pattern (regex): ")

    
    regex = re.compile(pattern, re.IGNORECASE)

    print("\n===== REGEX SEARCH RESULTS =====")

    for file_path in log_files:
        print(f"\nFile: {file_path}")
        found = False

        with open(file_path, "r") as file:
            for line in file:
                if regex.search(line):
                    print(" ", line.strip())
                    found = True

        if not found:
            print("  No matching entries found.")



if __name__ == "__main__":

    log_files = [
        "small.log",
        "medium.log",
        "large.log"
    ]

    while True:
        print("\n========= LOG ANALYZER MENU =========")
        print("1. Analyze log levels (INFO / WARN / ERROR)")
        print("2. Regex search in log files")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            analyze_logs_parallel(log_files)

        elif choice == "2":
            regex_search_logs(log_files)

        elif choice == "3":
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Please try again.")
