#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name="John Doe", job="Sales"):
        self.name = name
        self.job = job

    # ----- name property -----
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value.title()
        else:
            print("Name must be string between 1 and 25 characters.")

    # ----- job property -----
    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        if value in APPROVED_JOBS:
            self._job = value
        else:
            print("Job must be in list of approved jobs.")


p1 = Person(name="alice walker", job="Finance")
print(p1.name)  # Alice Walker
print(p1.job)   # Finance

p2 = Person(name="", job="Spy")
# => Name must be string between 1 and 25 characters.
# => Job must be in list of approved jobs.

p2.name = "jane smith"
p2.job = "ITC"
print(p2.name)  # Jane Smith
print(p2.job)   # ITC
