from Application.salary import calculate_salary
from Application.db.people import get_employees
from pprint import pprint
from datetime import date

sal = calculate_salary()
emp = get_employees()


if __name__ == '__main__':
    pprint('Hello')
    pprint(sal)
    pprint(emp)
    pprint(date.today())



