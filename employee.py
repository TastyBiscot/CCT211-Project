class Employee:
    """class to store information about the employee"""

    def __init__(self, fname, lname, job, username, password):
        self.fname = fname
        self.lname = lname
        self.job = job
        self.username = username
        self.password = password

    def __eq__(self, other):
        if isinstance(other, Employee):
            if self.username == other.username:
                return True
        return False


if __name__ == '__main__':
    pass
