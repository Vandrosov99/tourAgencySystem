import Connect
import random
from View import View
from datetime import datetime, date, time


# Dictionary with DB table names and them identifiers
tables = {
    1: 'client',
    2: 'contract',
    3: 'description_client',
    4: 'description_emp',
    5: 'description_type',
    6: 'employer',
    7: 'history',
    8: 'orders',
    9: 'post',
    10: 'status_payment',
    11: 'status_post',
    12: 'tour',
}


class Model:
    # Method that checks valid of the number of table that user input and returns it
    @staticmethod
    def validTable():
        incorrect = True
        while incorrect:
            table = input('Choose table number => ')
            if table.isdigit():
                table = int(table)
                if table >= 1 and table <= 12:
                    incorrect = False
                else:
                    print('Incorrect input, try again.')
            else:
                print('Incorrect input, try again.')
        return table

    # Method that prints all table of DB
    @staticmethod
    def showAllTables():
        connect = Connect.makeConnect()
        cursor = connect.cursor()
        for table in range(1, 13):
            table_name = '''"''' + tables[table] + '''"'''
            print(tables[table])

            show = 'select * from public.{}'.format(table_name)

            print("SQL query => ", show)
            cursor.execute(show)
            records = cursor.fetchall()
            obj = View(table, records)
            obj.show()
        cursor.close()
        Connect.closeConnect(connect)

    # Method that prints one table
    @staticmethod
    def showOneTable():
        View.list()
        connect = Connect.makeConnect()
        cursor = connect.cursor()

        table = Model.validTable()

        table_name = '''"''' + tables[table] + '''"'''
        print(tables[table])

        show = 'select * from public.{}'.format(table_name)

        print("SQL query => ", show)
        print('')
        cursor.execute(show)
        records = cursor.fetchall()
        obj = View(table, records)
        obj.show()
        cursor.close()
        Connect.closeConnect(connect)

# Inserting data into DB

    # Method that inserts data into DB
    @staticmethod
    def insert():
        connect = Connect.makeConnect()
        cursor = connect.cursor()
        restart = True
        while restart:
            View.list()
            table = Model.validTable()
            if table == 1:
                id_client = input("ID = ")
                surname = "'" + input('surname = ') + "'"

                insert = 'insert into "client" ("id_client","surname") values ({}, {})'.format(
                    id_client, surname)

                restart = False
            elif table == 2:
                id_contract = input('id_contract = ')
                dat = "'" + input('dat = ') + "'"
                id_order = input('id_client = ')
                id_emp = input('id_emp = ')

                insert = 'insert into "contract" ("id_contract","dat", "id_order", "id_emp") values ({}, {}, {}, {})'.format(
                    id_contract, dat, id_order, id_emp)

                restart = False
            elif table == 3:
                id_client = input("id_client = ")
                phone = "'" + input('phone = ') + "'"
                passport_number = "'" + input("passport_number = ") + "'"
                sex = "'" + input("sex = ") + "'"
                address = "'" + input("address = ") + "'"

                insert = 'insert into "description_client" ("id_client", "phone", "passport_number","sex","address") values ({}, {}, {},{},{})'.format(
                    id_client, phone, passport_number, sex, address)

                restart = False
            elif table == 4:
                id_emp = input("id_emp = ")
                phone = "'" + input('phone = ') + "'"
                passport_number = "'" + input("passport_number = ") + "'"
                sex = "'" + input("sex = ") + "'"
                address = "'" + input("address = ") + "'"

                insert = 'insert into "description_emp" ("id_emp", "phone", "passport_number","sex","address") values ({}, {}, {},{},{})'.format(
                    id_emp, phone, passport_number, sex, address)
                restart = False

            elif table == 5:

                id_type = input('id_type = ')
                people = "'" + input('people = ') + "'"
                hotel_name = "'" + input('hotel_name = ') + "'"

                insert = 'insert into "description_type" ("id_type", "people","hotel_name") values ({}, {},{})'.format(
                    id_type, people, hotel_name)

                restart = False
            elif table == 6:
                id_emp = input('id_emp = ')
                surname = "'" + input('surname = ') + "'"

                insert = 'insert into "employer" ("id_emp", "surname") values ({}, {})'.format(
                    id_emp, surname)
                restart = False

            elif table == 10:
                id_pay = input('id_pay = ')
                id_contract = input('id_contract = ')
                dat = "'" + input('dat = ') + "'"
                stage = "'" + input("stage = ") + "'"

                insert = 'insert into "status_payment" ("id_pay", "id_contract", "dat","stage") values ({}, {}, {},{})'.format(
                    id_pay, id_contract, dat, stage)

                restart = False
            elif table == 7:
                id_h = input('id_h = ')
                id_pay = input('id_pay = ')

                insert = 'insert into "history" ("id_h", "id_pay") values ({}, {})'.format(
                    id_h, id_pay)
                restart = False

            elif table == 8:
                id_order = input('id_order = ')
                id_type = input('id_type = ')
                id_client = input('id_client = ')

                insert = 'insert into "orders" ("id_order", "id_type","id_client") values ({}, {},{})'.format(
                    id_order, id_type, id_client)
                restart = False
            elif table == 9:
                id_post = input('id_post = ')
                category = "'" + input('category = ') + "'"

                insert = 'insert into "post" ("id_post", "category") values ({}, {})'.format(
                    id_post, category)
                restart = False
            elif table == 11:
                id_post = input('id_post = ')
                id_emp = input('id_emp= ')

                insert = 'insert into "status_post" ("id_post", "id_emp") values ({}, {})'.format(
                    id_post, id_emp)
                restart = False
            elif table == 12:
                id_type = input('id_type = ')
                way = "'" + input('way = ') + "'"
                days = "'" + input('days = ') + "'"
                price = input("cost = ")

                insert = 'insert into "tour" ("id_type", "way","days","price") values ({}, {},{},{})'.format(
                    id_type, way, days, price)
                restart = False
            else:
                print('\nIncorrect input, try again.')
        print(tables[table])
        print('SQl query => ', insert)
        cursor.execute(insert)
        connect.commit()
        print('Data added successfully!')
        cursor.close()
        Connect.closeConnect(connect)

    # Deleting data from DB

    # Method that deletes data from DB
    @staticmethod
    def delete():
        connect = Connect.makeConnect()
        cursor = connect.cursor()
        restart = True
        while restart:
            View.list()
            table = Model.validTable()

            if table == 1:
                clname = "'" + input('Attribute to delete id_client = ') + "'"
                delete = 'delete from "client" where "id_client"= {}'.format(
                    clname)
                restart = False
            elif table == 2:
                id_contract = "'" + \
                    input('Attribute to delete id_contract = ') + "'"
                delete = 'delete from "contract" where "id_contract"=  {}'.format(
                    id_contract)
                restart = False
            elif table == 3:
                dsname = "'" + input('Attribute to delete id_client = ') + "'"
                delete = 'delete from "description_client" where "id_client"= {}'.format(
                    dsname)
                restart = False
            elif table == 4:
                incorderid = input('Attribute to delete id_emp = ')
                delete = 'delete from "description_emp" where "id_emp"= {}'.format(
                    incorderid)
                restart = False
            elif table == 5:
                orid = input('Attribute to delete id_type = ')
                delete = 'delete from "description_type" where "id_type"=  {}'.format(
                    orid)
                restart = False
            elif table == 6:
                psnumber = "'" + \
                    input('Attribute to delete id_emp = ') + "'"
                delete = 'delete from "employer" where "id_emp"=  {}'.format(
                    psnumber)
                restart = False
            elif table == 7:
                rsname = "'" + \
                    input('Attribute to delete id_h = ') + "'"
                delete = 'delete from "history" where "id_h"= {}'.format(
                    rsname)
                restart = False
            elif table == 8:
                trname = "'" + input('Attribute to delete id_order = ') + "'"
                delete = 'delete from "orders" where "id_order"= {}'.format(
                    trname)
                restart = False
            elif table == 9:
                trname1 = "'" + input('Attribute to delete id_post = ') + "'"
                delete = 'delete from "post" where "id_post"= {}'.format(
                    trname1)
                restart = False

            elif table == 10:
                trname2 = "'" + input('Attribute to delete id_pay = ') + "'"
                delete = 'delete from "status_payment" where "id_pay"= {}'.format(
                    trname2)
                restart = False
            elif table == 11:
                trname11 = "'" + input('Attribute to delete id_post = ') + "'"
                delete = 'delete from "status_post" where "id_post"= {}'.format(
                    trname11)
                restart = False
            elif table == 12:
                trname12 = "'" + input('Attribute to delete id_type = ') + "'"
                delete = 'delete from "tour" where "id_type"= {}'.format(
                    trname12)
                restart = False
            else:
                print('\nIncorrect input, try again.')
        print(tables[table])
        print("SQL query => ", delete)
        cursor.execute(delete)
        connect.commit()
        print('Data deleted successfully!')
        cursor.close()
        Connect.closeConnect(connect)

# Updating data in DB

    # Method that updates data in DB
    @staticmethod
    def update():
        connect = Connect.makeConnect()
        cursor = connect.cursor()
        restart = True
        while restart:
            View.list()
            table = Model.validTable()
            if table == 1:
                clname = input('Attribute to update(where) id_client = ')
                View.attribute_list(1)
                in_restart = True
                while in_restart:
                    num = input('Number of attribute =>')
                    value = "'" + input('New value of attribute = ') + "'"
                    if num == '1':
                        set = '"id_client"= {}'.format(value)
                        in_restart = False
                    elif num == '2':
                        set = '"surname"= {}'.format(value)
                        in_restart = False
                    else:
                        print('\nIncorrect input, try again.')
                update = 'update "client" set {} where "id_client"= {}'.format(
                    set, clname)
                restart = False
                pass
            elif table == 2:
                crname = input('Attribute to update(where) id_contract = ')
                View.attribute_list(2)
                in_restart = True
                while in_restart:
                    num = input('Number of attribute =>')
                    value = "'" + input('New value of attribute = ') + "'"
                    if num == '1':
                        set = '"id_conract"= {}'.format(value)
                        in_restart = False
                    elif num == '2':
                        set = '"dat"= {}'.format(value)
                        in_restart = False
                    elif num == '3':
                        set = '"id_order"= {}'.format(value)
                        in_restart = False
                    elif num == '4':
                        set = '"id_emp"= {}'.format(value)
                        in_restart = False
                    else:
                        print('\nIncorrect input, try again.')
                update = 'update "contract" set {} where "id_contract"= {}'.format(
                    set, crname)
                restart = False
                pass
            elif table == 3:
                dsname = "'" + \
                    input('Attribute to update(where) id_client = ') + "'"
                View.attribute_list(3)
                in_restart = True
                while in_restart:
                    num = input('Number of attribute =>')
                    value = "'" + input('New value of attribute = ') + "'"
                    if num == '1':
                        set = '"id_client"= {}'.format(value)
                        in_restart = False
                    elif num == '2':
                        set = '"phone"= {}'.format(value)
                        in_restart = False
                    elif num == '3':
                        set = '"passport_number"= {}'.format(value)
                        in_restart = False
                    elif num == '4':
                        set = '"sex"= {}'.format(value)
                        in_restart = False
                    elif num == '5':
                        set = '"address"= {}'.format(value)
                        in_restart = False
                    else:
                        print('\nIncorrect input, try again.')
                update = 'update "description_client" set {} where "id_client"= {}'.format(
                    set, dsname)
                restart = False
                pass
            elif table == 4:
                incorderid = input('Attribute to update(where) id_emp = ')
                View.attribute_list(4)
                in_restart = True
                while in_restart:
                    num = input('Number of attribute =>')
                    value = "'" + input('New value of attribute = ') + "'"
                    if num == '1':
                        set = '"id_emp"= {}'.format(value)
                        in_restart = False
                    elif num == '2':
                        set = '"phone"= {}'.format(value)
                        in_restart = False
                    elif num == '3':
                        set = '"passport_number"= {}'.format(value)
                        in_restart = False
                    elif num == '4':
                        set = '"sex"= {}'.format(value)
                        in_restart = False
                    elif num == '5':
                        set = '"address"= {}'.format(value)
                        in_restart = False
                    else:
                        print('\nIncorrect input, try again.')
                update = 'update "description_emp" set {} where "id_emp"= {}'.format(
                    set, incorderid)
                restart = False
                pass
            elif table == 5:
                incorderid = input('Attribute to update(where) id_type = ')
                View.attribute_list(5)
                in_restart = True
                while in_restart:
                    num = input('Number of attribute =>')
                    value = "'" + input('New value of attribute = ') + "'"
                    if num == '1':
                        set = '"id_type"= {}'.format(value)
                        in_restart = False
                    elif num == '2':
                        set = '"people"= {}'.format(value)
                        in_restart = False
                    elif num == '3':
                        set = '"hotel_name"= {}'.format(value)
                        in_restart = False
                    else:
                        print('\nIncorrect input, try again.')
                update = 'update "description_type" set {} where "id_type"= {}'.format(
                    set, incorderid)
                restart = False
                pass
            elif table == 6:
                orid = input('Attribute to update(where) id_emp= ')
                View.attribute_list(6)
                in_restart = True
                while in_restart:
                    num = input('Number of attribute =>')
                    value = "'" + input('New value of attribute = ') + "'"
                    if num == '1':
                        set = '"id_emp"= {}'.format(value)
                        in_restart = False
                    elif num == '2':
                        set = '"surname"= {}'.format(value)
                        in_restart = False
                    else:
                        print('\nIncorrect input, try again.')
                update = 'update "employer" set {} where "id_emp"= {}'.format(
                    set, orid)
                restart = False
                pass
            elif table == 7:
                psnumber = "'" + \
                    input('Attribute to update(where) id_h = ') + "'"
                View.attribute_list(7)
                in_restart = True
                while in_restart:
                    num = input('Number of attribute =>')
                    value = "'" + input('New value of attribute = ') + "'"
                    if num == '1':
                        set = '"id_h"= {}'.format(value)
                        in_restart = False
                    elif num == '2':
                        set = '"id_pay"= {}'.format(value)
                        in_restart = False
                    else:
                        print('\nIncorrect input, try again.')
                update = 'update "history" set {} where "id_h"= {}'.format(
                    set, psnumber)
                restart = False
                pass
            elif table == 8:
                rsname = "'" + \
                    input('Attribute to update(where) id_order = ') + "'"
                View.attribute_list(8)
                in_restart = True
                while in_restart:
                    num = input('Number of attribute =>')
                    value = "'" + input('New value of attribute = ') + "'"
                    if num == '1':
                        set = '"id_order"= {}'.format(value)
                        in_restart = False
                    elif num == '2':
                        set = '"id_type"= {}'.format(value)
                        in_restart = False
                    elif num == '3':
                        set = '"id_type"= {}'.format(value)
                        in_restart = False
                    else:
                        print('\nIncorrect input, try again.')
                update = 'update "orders" set {} where "id_order"= {}'.format(
                    set, rsname)
                restart = False
                pass
            elif table == 9:
                trname = "'" + \
                    input('Attribute to update(where) id_post = ') + "'"
                View.attribute_list(9)
                in_restart = True
                while in_restart:
                    num = input('Number of attribute =>')
                    value = "'" + input('New value of attribute = ') + "'"
                    if num == '1':
                        set = '"id_post"= {}'.format(value)
                        in_restart = False
                    elif num == '2':
                        set = '"category"= {}'.format(value)
                        in_restart = False
                    else:
                        print('\nIncorrect input, try again.')
                update = 'update "post" set {} where "id_post"= {}'.format(
                    set, trname)
                restart = False
                pass
            elif table == 10:
                trname = "'" + \
                    input('Attribute to update(where) id_pay = ') + "'"
                View.attribute_list(10)
                in_restart = True
                while in_restart:
                    num = input('Number of attribute =>')
                    value = "'" + input('New value of attribute = ') + "'"
                    if num == '1':
                        set = '"id_pay"= {}'.format(value)
                        in_restart = False
                    elif num == '2':
                        set = '"id_contract"= {}'.format(value)
                        in_restart = False
                    elif num == '3':
                        set = '"dat"= {}'.format(value)
                        in_restart = False
                    elif num == '4':
                        set = '"stage"= {}'.format(value)
                        in_restart = False
                    else:
                        print('\nIncorrect input, try again.')
                update = 'update "status_payment" set {} where "id_pay"= {}'.format(
                    set, trname)
                restart = False
                pass
            elif table == 11:
                trname = "'" + \
                    input('Attribute to update(where) id_post = ') + "'"
                View.attribute_list(11)
                in_restart = True
                while in_restart:
                    num = input('Number of attribute =>')
                    value = "'" + input('New value of attribute = ') + "'"
                    if num == '1':
                        set = '"id_post"= {}'.format(value)
                        in_restart = False
                    elif num == '2':
                        set = '"id_emp"= {}'.format(value)
                        in_restart = False
                    else:
                        print('\nIncorrect input, try again.')
                update = 'update "status_post" set {} where "id_post"= {}'.format(
                    set, trname)
                restart = False
                pass
            elif table == 12:
                trname = "'" + \
                    input('Attribute to update(where) id_type = ') + "'"
                View.attribute_list(12)
                in_restart = True
                while in_restart:
                    num = input('Number of attribute =>')
                    value = "'" + input('New value of attribute = ') + "'"
                    if num == '1':
                        set = '"id_type"= {}'.format(value)
                        in_restart = False
                    elif num == '2':
                        set = '"way"= {}'.format(value)
                        in_restart = False
                    elif num == '3':
                        set = '"days"= {}'.format(value)
                        in_restart = False
                    elif num == '4':
                        set = '"price"= {}'.format(value)
                        in_restart = False
                    else:
                        print('\nIncorrect input, try again.')
                update = 'update "tour" set {} where "id_type"= {}'.format(
                    set, trname)
                restart = False
                pass
            else:
                print('\nIncorrect input, try again.')
        print(tables[table])
        print("SQL query => ", update)
        cursor.execute(update)
        connect.commit()
        print('Data updeted successfully!')
        cursor.close()
        Connect.closeConnect(connect)
        pass

# ----------TASK 3----------

    # Method that seletes data from DB
    @staticmethod
    def select():
        connect = Connect.makeConnect()
        cursor = connect.cursor()
        print(''' out select based for client 
        ''')

        # ordateL = "'" + input('OrDate: Between ') + "'"
        # print('and')
        # ordateR = "'" + input() + "'"
        # ordelivered = input('OrDelivered: ')
        # rsalltime = input('RsAllTime: ')

        select = 'select * from "client"'

        print("SQL query => ", select)
        cursor.execute(select)
        records = cursor.fetchall()
        obj = View(1, records)
        obj.showSelect()

        print('Data selected successfully!')
        cursor.close()
        Connect.closeConnect(connect)

# ----------TASK 4----------

    # Method that runs full text search in DB
        # Method that runs full text search in DB
    @staticmethod
    def text_search():
        connect = Connect.makeConnect()
        cursor = connect.cursor()
        restart = True
        while restart:
            View.list()
            table = Model.validTable()
            text = "'" + input('Search text = ') + "'"
            incorrect = True
            while incorrect:
                mode = input('''"A you sure? put '2' here = >  "
                 ''')
                if mode.isdigit():
                    mode = int(mode)
                    if mode >= 1 and mode <= 2:
                        incorrect = False
                    else:
                        print('Incorrect input, try again.')
                else:
                    print('Incorrect input, try again.')

            if mode == 2:
                if table == 1:
                    text_search = 'select * from "client" where to_tsvector("surname") @@ plainto_tsquery({})'.format(
                        text)
                    restart = False
                elif table == 2:
                    print("dont have string collumns in this table")
                    restart = False
                elif table == 3:
                    text_search = 'select * from "description_client" where to_tsvector("address") || to_tsvector("sex") || to_tsvector("phone") || ("passport_number") @@ plainto_tsquery({})'.format(
                        text)
                    restart = False
                elif table == 4:
                    text_search = 'select * from "description_emp" where to_tsvector("address") || to_tsvector("sex") || to_tsvector("phone") || ("passport_number")@@ plainto_tsquery({})'.format(
                        text)
                    restart = False
                elif table == 5:
                    text_search = 'select * from "description_type" where to_tsvector("hotel_name") || to_tsvector("people") @@ plainto_tsquery({})'.format(
                        text)
                    restart = False
                elif table == 6:
                    text_search = 'select * from "employer" where to_tsvector("surname") @@ plainto_tsquery({})'.format(
                        text)
                    restart = False
                elif table == 7:
                    print("dont have string collumns in this table")
                    restart = False
                elif table == 8:
                    print("dont have string collumns in this table")
                    restart = False
                elif table == 9:
                    text_search = 'select * from "post" where to_tsvector("category") @@ plainto_tsquery({})'.format(
                        text)
                    restart = False

                elif table == 10:
                    text_search = 'select * from "status_payment" where to_tsvector("stage") @@ plainto_tsquery({})'.format(
                        text)
                    restart = False

                elif table == 11:
                    print("dont have string collumns in this table")
                    restart = False

                elif table == 12:
                    text_search = 'select * from "tour" where to_tsvector("way") || to_tsvector("days") @@ plainto_tsquery({})'.format(
                        text)
                    restart = False

                else:
                    print('\nIncorrect input, try again.')
            else:
                print('\nIncorrect input, try again.')

        print(tables[table])
        print('SQL query => ', text_search)
        cursor.execute(text_search)
        records = cursor.fetchall()
        obj = View(table, records)
        obj.show()
        print('Data searched successfully!')
        cursor.close()
        Connect.closeConnect(connect)
