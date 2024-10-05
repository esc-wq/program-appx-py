import csv
import matplotlib.pyplot as plt
from datetime import datetime

HABIT_FILE = 'habits.csv'

def add_habit(date, habit):
    with open(HABIT_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, habit])

def view_habits():
    try:
        with open(HABIT_FILE, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No habits found. Please add some habits.")

def generate_report():
    habit_count = {}
    
    try:
        with open(HABIT_FILE, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                date, habit = row
                if habit in habit_count:
                    habit_count[habit] += 1
                else:
                    habit_count[habit] = 1
    except FileNotFoundError:
        print("No habits found for the report.")

    for habit, count in habit_count.items():
        print(f"{habit}: {count} days completed")

    dates = []
    counts = []
    for row in habit_count.items():
        dates.append(row[0])
        counts.append(row[1])

    plt.plot(dates, counts)
    plt.title("Habit Progress Over Time")
    plt.xlabel("Date")
    plt.ylabel("Days Completed")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    while True:
        print("\nHabit Tracker")
        print("1. Add Habit")
        print("2. View Habits")
        print("3. Generate Report")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            habit = input("Enter habit: ")
            add_habit(date, habit)
        elif choice == '2':
            view_habits()
        elif choice == '3':
            generate_report()
        elif choice == '4':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == '__main__':
    main()
