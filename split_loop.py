from dataclasses import dataclass
from typing import List

def compute_stats(employees: List["Employee"]) -> str:
    #employee_ids = []
    # total_consultant_salary = 0
    # for employee in employees:
    #     if employee.consultant:
    #         total_consultant_salary += employee.salary
        #employee_ids.append(employee.id)
    employee_ids = [employee.id for employee in employees]
    total_consultant_salary = sum([e.salary for e in employees if e.consultant])
    print("Employee IDs: " + str(employee_ids))
    return f"Total consultant salary: {total_consultant_salary}; ids: {employee_ids}"

@dataclass
class Employee:
    id: int
    age: int
    salary: int
    consultant: bool