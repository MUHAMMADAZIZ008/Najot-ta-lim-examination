from abc import abstractmethod

class Employee:
    def __init__(self, name: int, salary: float) -> None:
        self.name = name
        self.salary = salary

    @abstractmethod
    def get_details(self) -> str:
        return f"Name: {self.name}\nSalary: {self.salary}"
    
    @abstractmethod
    def calculate_bonus(self) -> float:
        return 0.0
    
class Manager(Employee):
    def __init__(self, name: int, salary: float, department:str) -> None:
        super().__init__(name, salary)
        self.department = department


    def get_details(self) -> str:
        return f"{super().get_details() }\nDepartment: {self.department}"


    def calculate_bonus(self) -> float:
        bonus = (self.salary * 10) /100
        return f"Manager uchun bonus: {bonus}"
    

class Developer(Employee):

    def __init__(self, name: int, salary: float, programming_language) -> None:
        super().__init__(name, salary)
        self.programming_language = programming_language
    

    def get_details(self) -> str:
        return f"{super().get_details()}\nProgramming language: {self.programming_language}"
    

    def calculate_bonus(self) -> float:
        bonus = (self.salary * 5) /100
        return f"Developer uchun bonus: {bonus}"



manager = Manager("Alice", 120000, "Sales")
print(manager.get_details())
print(manager.calculate_bonus())

print("")
developer = Developer("Bob", 100000, "Python")
print(developer.get_details())
print(developer.calculate_bonus())

