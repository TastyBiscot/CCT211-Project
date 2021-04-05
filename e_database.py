from employee import Employee


class EDatabase:

    def __init__(self, filename):
        self.employees = []
        self.filename = filename
        self._get_employee()

    def _get_employee(self):
        """read from csv file to get employees"""
        pass

    def add_employee(self, fname, lname, job, username, password, ):
        self.employees.append(Employee(fname, lname, job, username, password))

    def remove_employee(self, e):
        if e in self.employees:
            self.employees.remove(e)
            return True
        else:
            return False

    def save(self):
        """save the employees into the csv file"""
        pass


if __name__ == '__main__':
    pass
