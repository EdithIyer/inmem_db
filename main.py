import sys

from dbhelper import DatabaseHelper


def begin_transaction():
    line = sys.stdin.readline()
    if 'BEGIN' == line:
        print('Beginning Transaction')

def get_name_values(line):
    # line = sys.stdin.readline()
    return line[0], line[1:]

transaction_tracker = []


def run_database_helper():
    ext_db = {}
    # run = True
    if sys.stdin.readline().startswith('BEGIN'):
        run = True
        while run == True:
            db_helper = DatabaseHelper('./inmemdb.json')

            command = sys.stdin.readline().strip('\n')
            if command.startswith('SET'):
                keyval = command[3:]
                name, value = get_name_values(keyval)
                db_helper.set(name, value, ext_db)
                transaction_tracker.append({'function': 'SET', 'name': name, 'value':value})
            elif command.startswith('GET'):
                keyval = command[3:]
                print(db_helper.get(get_name_values(keyval)[0], ext_db))
            elif command.startswith('DELETE'):
                name = command[6:]
                value = db_helper.get(name, ext_db)
                transaction_tracker.append({'function': 'DELETE', 'name': name,'value':value })
                db_helper.delete(name, ext_db)
            elif command.startswith('COUNT'):
                value=command[5:]
                print(db_helper.counter(value, ext_db))
            elif command.startswith('END'):
                print('Exiting DB')
                run = False
                break
            elif command.startswith('RESET'):
                print('Clearing Database')
                db_helper.resetdb(ext_db)
            elif command.startswith('ROLLBACK'):
                if len(transaction_tracker) == 0:
                    print('TRANSACTION NOT FOUND')
                else:
                    most_recent = transaction_tracker[-1]
                    db_helper.rollback(most_recent, ext_db)
            else:
                print('Command not found')
    else:
        print('Type Begin to Start Transaction')

def main():
    run_database_helper()

if __name__ == "__main__":
    main()
