class View:

    # Initialization of class View
    def __init__(self, table, records):
        self.table = table
        self.records = records

    # Method that prints the list of DB tables
    @staticmethod
    def list():
        print('''
        1 => client
        2 => contract
        3 => description_client
        4 => description_emp
        5 => description_type
        6 => employeer
        7 => history
        8 => orders
        9 => post
        10 => status_payment
        11 => status_post
        12 => tour
        ''')

    # Method that prints the list of attributes of the selected table
    @staticmethod
    def attribute_list(table):
        if table == 1:
            print('''
            1 => id_client
            2 => surname
            ''')
        elif table == 2:
            print('''
            1 => id_contact
            2 => dat
            3 => id_order
            4 => id_emp
            ''')
        elif table == 3:
            print('''
            1 => id_client
            2 => phone
            3 => passport_number
            4 => sex
            5 => address
            ''')
        elif table == 4:
            print('''
            1 => id_emp
            2 => phone
            3 => passport_number
            4 => sex
            5 => address
            ''')
        elif table == 5:
            print('''
            1 = > id_type
            2 = > people
            3 = > hotel_name
            ''')
        elif table == 6:
            print('''
            1 = > id_emp
            2 = > surname
            ''')
        elif table == 7:
            print('''
            1 = > id_h
            2 = > id_pay
            ''')
        elif table == 8:
            print('''
            1 = > id_order
            2 = > type
            3 = > id_client
            ''')
        elif table == 9:
            print('''
            1 = > id_post
            2 = > category
            ''')
        elif table == 10:
            print('''
            1 => id_pay
            2 => id_contract
            3 => dat
            4 => stage
            ''')
        elif table == 11:
            print('''
            1 = > id_post
            2 = > id_emp
            ''')
        elif table == 12:
            print('''
            1 => id_type
            2 => way
            3 => days
            4 => price
            ''')
    # Method that prints content from a selected table

    def show(self):
        print("____________________\n")
        if self.table == 1:
            for row in self.records:
                print("id_client = ", row[0])
                print("surname = ", row[1])
                print("____________________\n")
        elif self.table == 2:
            for row in self.records:
                print("id_contract = ", row[0])
                print("dat = ", row[1])
                print("id_order = ", row[2])
                print("id_emp", row[3])
                print("____________________\n")
        elif self.table == 3:
            for row in self.records:
                print("id_client = ", row[0])
                print("phone = ", row[1])
                print("passport_number = ", row[2])
                print("sex = ", row[3])
                print("address = ", row[4])
                print("____________________\n")
        elif self.table == 4:
            for row in self.records:
                print("id_emp = ", row[0])
                print("phone = ", row[1])
                print("passport_number = ", row[2])
                print("sex = ", row[3])
                print("address = ", row[4])
                print("____________________\n")
        elif self.table == 5:
            for row in self.records:
                print("id_type = ", row[0])
                print("people = ", row[1])
                print("hotel_name = ", row[2])
                print("____________________\n")
        elif self.table == 6:
            for row in self.records:
                print("id_emp = ", row[0])
                print("surname = ", row[1])
                print("____________________\n")
        elif self.table == 7:
            for row in self.records:
                print("id_h = ", row[0])
                print("id_pay= ", row[1])
                print("____________________\n")
        elif self.table == 8:
            for row in self.records:
                print("id_orders = ", row[0])
                print("id_type = ", row[1])
                print("id_client = ", row[2])
                print("____________________\n")
        elif self.table == 9:
            for row in self.records:
                print("id_post = ", row[0])
                print("category = ", row[1])
                print("____________________\n")
        elif self.table == 10:
            for row in self.records:
                print("id_pay = ", row[0])
                print("id_contract = ", row[1])
                print("dat = ", row[2])
                print("stage = ", row[3])
                print("____________________\n")
        elif self.table == 11:
            for row in self.records:
                print("id_post = ", row[0])
                print("id_emp = ", row[1])
                print("____________________\n")
        elif self.table == 12:
            for row in self.records:
                print("id_type = ", row[0])
                print("way = ", row[1])
                print("days = ", row[2])
                print("price= ", row[3])
                print("____________________\n")
    # Method that prints the result of select query

    def showSelect(self):
        for row in self.records:
            print("id_client = ", row[0])
            print("surname= ", row[1])
            print("____________________\n")
