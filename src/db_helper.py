import mysql.connector

class DbHelper:

    def __init__(self):
        self.db = mysql.connector.connect(
            host='localhost', 
            user='root', 
            passwd='admin@123', 
            database='employees'
            )
        self.pointer = self.db.cursor()

    def get_maximum_salary(self):
        '''
        Implement the logic to find and return maximum salary from employee table
        '''
        self.pointer.execute('SELECT MAX(salary) FROM emp;')
        return self.pointer.fetchone()[0]

    def get_minimum_salary(self):
        '''
        Implement the logic to find and return minimum salary from employee table
        '''
        self.pointer.execute('SELECT MIN(salary) FROM emp;')
        return self.pointer.fetchone()[0]
    
    def print_sal(self):
        min_salary = self.get_minimum_salary()
        max_salary = self.get_maximum_salary()
        print(max_salary)
        print(min_salary)    

# if __name__ == "__main__":
#     db_helper = DbHelper()
#     min_salary = db_helper.get_minimum_salary()
#     max_salary = db_helper.get_maximum_salary()
#     print(max_salary)
#     print(min_salary)