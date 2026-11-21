import json
from datetime import date
from pathlib import Path

DATA_FILE = Path("sessions.json")


def load_sessions():
    if DATA_FILE.exists():
        return json.loads(DATA_FILE.read_text())
    return []


def save_sessions(sessions):
    DATA_FILE.write_text(json.dumps(sessions, indent=2))


def add_session(sessions):
    subject = input("Subject: ").strip()
    try:
        minutes = int(input("Minutes studied: "))
    except ValueError:
        print("Please enter a whole number.")
        return
    sessions.append({"date": str(date.today()), "subject": subject, "minutes": minutes})
    save_sessions(sessions)
    print("Session saved!")


def show_summary(sessions):
    if not sessions:
        print("No sessions logged yet.")
        return
    totals = {}
    for s in sessions:
        totals[s["subject"]] = totals.get(s["subject"], 0) + s["minutes"]
    print("\nTotal minutes per subject:")
    for subject, minutes in sorted(totals.items(), key=lambda x: -x[1]):
        print(f"  {subject}: {minutes} min ({minutes / 60:.1f} hrs)")


def main():
    sessions = load_sessions()
    while True:
        print("\n1) Log a session  2) View summary  3) Quit")
        choice = input("Choose: ").strip()
        if choice == "1":
            add_session(sessions)
        elif choice == "2":
            show_summary(sessions)
        elif choice == "3":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
