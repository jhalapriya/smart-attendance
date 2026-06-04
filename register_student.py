import os
import csv

# Base folder path
DATASET_PATH = "dataset/student_images"
CSV_FILE = "database/students.csv"

def register_student():
    print("\n===== Student Registration =====")

    student_id = input("Enter Student ID: ").strip()
    student_name = input("Enter Student Name: ").strip()

    # Validation
    if not student_id or not student_name:
        print("ID and Name cannot be empty")
        return

    # Create folder name
    folder_name = f"{student_id}_{student_name}"
    student_folder = os.path.join(DATASET_PATH, folder_name)

    # Create student folder
    os.makedirs(student_folder, exist_ok=True)

    # Ensure CSV directory exists
    os.makedirs(os.path.dirname(CSV_FILE), exist_ok=True)

    # Check if CSV exists
    file_exists = os.path.isfile(CSV_FILE)

    # Save student data in CSV
    with open(CSV_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)

        # Add header if file is new or empty
        if not file_exists or os.path.getsize(CSV_FILE) == 0:
            writer.writerow(["student_id", "name"])

        writer.writerow([student_id, student_name])

    print("\nStudent Registered Successfully!")
    print(f"Folder Created: {student_folder}")

# Run program
if __name__ == "__main__":
    register_student()