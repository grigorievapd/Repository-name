if __name__ == "__main__":
    class BasicSalary:
         def __init__(self, name: str, rate: float, hours: int, salary: float):
            """
            Создание и подготовка к работе класса "Основной оклад"
            :param name: Имя сотрудника предприятия
            :param rate: Часовая ставка заработной платы
            :param hours: Количество отработанных часов
            :param salary: Заработная плата сотрудника
            """
            self.name = name
            self.rate = rate
            self.hours = hours
            self.salary = salary


         @property
         def name(self) -> str:
            return self._name

         def salary(self) -> float:
            """ Метод, рассчитывающий окладную часть заработной платы работника. """
            self.salary = self.rate * self.hours

         def __str__(self) -> str:
            return f"Сотрудник {self.name} по окладу получит заработную плату в размере {self.salary}."

         def __repr__(self) -> str:
            return f"{self.__class__.__name__}(name={self.name!r}, salary={self.!r})"

    class PayrollSettlements(Salary):

        def __init__(self, name: str, salary: float, personal_income_tax_rate: float, insurance_premiums: float, bonus:float, payroll_settlements: float):
            """
            Создание и подготовка к работе класса "Расчеты по заработной плате" для определения общих выплат по заработной плате
            :param personal_income_tax_rate: Ставка НДФЛ
            :param insurance_premiums: Страховые взносы
            :param bonus: Премиальная часть заработной платы
            :param payroll_settlements: Общие выплаты по заработной плате
            """
            super().__init__(name, salary)
            self.personal_income_tax_rate = personal_income_tax_rate
            self.insurance_premiums = insurance_premiums
            self.bonus = bonus
            self.payroll_settlements = payroll_settlements

        def salary (self) -> float:
            """ Метод, рассчитывающий зарплату работника с учетом премиальных отчислений.
                Метод перегружается, так как необходимо учесть новый аргумент (премия)
            """
            self.salary = self.rate * self.hours * (1 + self.bonus)

        def personal_income_tax_rate (self) -> float:
            """ Метод, рассчитывающий зарплату работника к выплате
            """
        def insurance_premiums (self) -> float:
            """ Метод, рассчитывающий страховые взносы к выплате
            """
        def payroll_settlements (self) -> float:
            """ Метод, рассчитывающий общие выплаты по заработной плате
            """
            self.payroll_settlements = self.salary + self.insurance_premiums
            ...

        def __str__(self) -> str:
            return f"Общие выплоты по заработной плате для сотрудника {self.name} составили {self.payroll_settlements}"

        def __repr__(self) -> str:
             return f"{self.__class__.__name__}(name={self.name!r}, payroll_settlements={self.payroll_settlements!r})"



