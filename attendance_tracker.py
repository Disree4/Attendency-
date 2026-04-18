# UbuntuTech Community Solutions Attendance Tracker
import json
import os

# Data structures
participants = []  # List to store participant dictionaries
DATA_FILE = 'attendance_data.json'  # File to persist data

# Function to save data to file
def save_data():
    try:
        with open(DATA_FILE, 'w') as f:
            json.dump(participants, f, indent=4)
        print("Data saved successfully.")
    except Exception as e:
        print(f"Error saving data: {e}")

# Function to load data from file
def load_data():
    global participants
    try:
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r') as f:
                participants = json.load(f)
            print(f"Loaded {len(participants)} existing participant records.")
        else:
            participants = []
    except Exception as e:
        print(f"Error loading data: {e}")
        participants = []

# Function to capture participant data
def capture_participant():
    while True:
        try:
            name = input("Enter participant name: ").strip()
            if not name:
                print("Name cannot be empty. Please try again.")
                continue
            programme = input("Enter programme name: ").strip()
            attendance = input("Enter attendance status (Present/Absent): ").strip().capitalize()
            if attendance not in ['Present', 'Absent']:
                print("Invalid attendance status. Must be 'Present' or 'Absent'.")
                continue
            date = input("Enter date (e.g., YYYY-MM-DD): ").strip()
            resource = input("Enter resource used: ").strip()
            # Store in dict
            participant = {
                'name': name,
                'programme': programme,
                'attendance': attendance,
                'date': date,
                'resource': resource
            }
            participants.append(participant)
            print("Participant added successfully.")
            save_data()
            more = input("Add another participant? (y/n): ").strip().lower()
            if more != 'y':
                break
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")

# Function to display all records
def display_records():
    if not participants:
        print("No participants recorded.")
        return
    print("\nAll Participant Records:")
    for i, p in enumerate(participants, 1):
        print(f"{i}. Name: {p['name']}, Programme: {p['programme']}, Attendance: {p['attendance']}, Date: {p['date']}, Resource: {p['resource']}")

# Function to calculate attendance per programme
def attendance_per_programme():
    programme_count = {}
    for p in participants:
        prog = p['programme']
        if p['attendance'] == 'Present':
            programme_count[prog] = programme_count.get(prog, 0) + 1
    return programme_count

# Function to calculate resource usage
def resource_usage():
    resource_count = {}
    for p in participants:
        res = p['resource']
        resource_count[res] = resource_count.get(res, 0) + 1
    return resource_count

# Function to generate summary
def generate_summary():
    total_participants = len(participants)
    total_attendance = sum(1 for p in participants if p['attendance'] == 'Present')
    attendance_summary = attendance_per_programme()
    resource_summary = resource_usage()
    threshold = 5  # Predefined threshold for low attendance
    alert = "Low attendance alert: Total attendance is below threshold." if total_attendance < threshold else "Attendance is satisfactory."

    print("\n--- Summary Report ---")
    print(f"Total Number of Participants: {total_participants}")
    print(f"Total Attendance: {total_attendance}")
    print("Attendance Summary per Programme:")
    for prog, count in attendance_summary.items():
        print(f"  {prog}: {count}")
    print("Resource Usage Summary:")
    for res, count in resource_summary.items():
        print(f"  {res}: {count} times")
    print(f"Alert: {alert}")

# Main function
def main():
    print("Welcome to UbuntuTech Community Solutions Attendance Tracker v1.0 - Developed by Lebogang ")
    load_data()
    capture_participant()
    display_records()
    generate_summary()
    save_data()

if __name__ == "__main__":
    main()