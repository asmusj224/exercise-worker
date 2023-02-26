import os
from os.path import isfile, join
import psycopg2


def main():
    conn = psycopg2.connect(os.environ.get('DATABASE_URL'))
    cursor = conn.cursor()
    mypath = './sql'
    files = [f for f in os.listdir(mypath) if isfile(join(mypath, f))]
    
    for idx, file in enumerate(files):
        print(f'{idx + 1} of {len(files)}')
        if not file.endswith('.sql'):
            continue
        fd = open(f'{mypath}/{file}', 'r')
        sqlFile = fd.read()
        fd.close()
       
        sqlCommands = sqlFile.split(';')
        sqlCommands = list(filter(None, sqlCommands))


        if len(sqlCommands) == 0:
            continue

        for command in sqlCommands:
            try:
                cursor.execute(command)
                conn.commit()
            except Exception as msg:
                print(command, 'command', file)
                print('Skipped', msg)
    cursor.close()
    conn.close()



if __name__ == "__main__":
    main()




