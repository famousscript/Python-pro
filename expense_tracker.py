import csv

def add_expense(amount, category):
    with open("expenses.csv", mode="a", newline="") as file:
        writer = csv.writer(file)``
        writer.writerow([amount, category])

def view_expenses():
    with open("expenses.csv", mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

# Example usage
add_expense(200, "Stationery")
add_expense(500, "Snacks")
view_expenses()
