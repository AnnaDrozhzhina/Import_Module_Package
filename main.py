from application.db.people import get_employees
from application.salary import calculate_salary
from datetime import date

print(date.today())

if __name__ == '__main__':
    get_employees()
    calculate_salary()
