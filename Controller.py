from Model import Model


class Controller:
    # Main Method that calls main manu of the  controller
    @staticmethod
    def mainMenu():
        exit = False
        print('Welcome to DB Controller program')
        while not exit:
            print('''
                Main menu
               0 => Show one table 
               1 => Show all tables
               2 => Insert data
               3 => Delete data
               4 => Update data
               5 => Search text
               6 => Exit''')

            choise = input('\nMake your choise =>  ')
            if choise == '0':
                Model.showOneTable()
            elif choise == '1':
                Model.showAllTables()
            elif choise == '2':
                end_insert = False
                while not end_insert:
                    Model.insert()
                    incorrect = True
                    while incorrect:
                        num = input('\nContinue insertion? 1 - Yes; 2 - No =>')
                        if num == '2':
                            end_insert = True
                            incorrect = False
                        elif num == '1':
                            incorrect = False
                            pass
                        else:
                            print('\nIncorrect input, try again.')
            elif choise == '3':
                end_delete = False
                while not end_delete:
                    Model.delete()
                    incorrect = True
                    while incorrect:
                        num = input('\nContinue deletion? 1 - Yes; 2 - No =>')
                        if num == '2':
                            end_delete = True
                            incorrect = False
                        elif num == '1':
                            incorrect = False
                            pass
                        else:
                            print('\nIncorrect input, try again.')
            elif choise == '4':
                end_update = False
                while not end_update:
                    Model.update()
                    incorrect = True
                    while incorrect:
                        num = input('\nContinue updation? 1 - Yes; 2 - No =>')
                        if num == '2':
                            end_update = True
                            incorrect = False
                        elif num == '1':
                            incorrect = False
                            pass
                        else:
                            print('\nIncorrect input, try again.')
            elif choise == '5':
                end_seacrh = False
                while not end_seacrh:
                    Model.text_search()
                    incorrect = True
                    while incorrect:
                        num = input('\nContinue to find? 1 - Yes; 2 - No =>')
                        if num == '2':
                            end_seacrh = True
                            incorrect = False
                        elif num == '1':
                            incorrect = False
                            pass
                        else:
                            print('\nIncorrect input, try again.')

            elif choise == '6':
                exit = True
            else:
                print('\nIncorrect input, try again.')
            incorrect = True
            while incorrect:
                end = input('\nContinue work with DB? 1 - Yes; 2 - No. = >')
                if end == '2':
                    incorrect = False
                    exit = True
                elif end == '1':
                    incorrect = False
                else:
                    print('\nIncorrect input, try again.')
