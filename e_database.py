class EDatabase:

    def __init__(self, filename):
        self.employees = []
        self.filename = filename
        self._get_employee()

    def _get_employee(self):
        """read from csv file to get employees"""
        pass

    def add_employee(self):
        pass

    def remove_employee(self):
        pass

    def save(self):
        """save the employees into the csv file"""
        pass


if __name__ == '__main__':
    pass
