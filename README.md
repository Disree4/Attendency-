# UbuntuTech Community Solutions Attendance Tracker

This is a simple Python-based console application for managing participant attendance and resource usage in community programmes.

## Features

- Capture participant attendance information
- Track basic resource usage
- Process and analyze collected data
- Display meaningful summaries
- **Persistent data storage** - records are automatically saved to `attendance_data.json` and loaded on startup

## Requirements

- Python 3.x

## How to Run

Run the script using Python:

```
python attendance_tracker.py
```

Or use the VS Code task "Run Attendance Tracker".

## Usage

Follow the prompts to enter participant details. After entering data, the application will display records and a summary report.

## Data Persistence

All participant records are automatically saved to `attendance_data.json` in JSON format. When you restart the program, previously entered data is automatically loaded, allowing you to continue building your attendance records across multiple sessions.