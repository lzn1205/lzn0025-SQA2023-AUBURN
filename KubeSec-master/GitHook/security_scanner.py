import subprocess
import csv

def run_security_scan(file_path):
    command = f"bandit -r -f csv {file_path}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    output = result.stdout.strip().splitlines()

    with open('security_report.csv', 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        for line in output:
            csv_writer.writerow(line.split(','))

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        run_security_scan(file_path)
