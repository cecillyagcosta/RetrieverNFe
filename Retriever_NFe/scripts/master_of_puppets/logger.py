from datetime import datetime
from time import gmtime
from os.path import exists

logfile = 'C:/BOT/Retriever_NFe/scripts/master_of_puppets/log.txt'
dt = datetime.now()
str_dt = dt.strftime("%d-%m-%Y, %H:%M:%S")

def makeLog(_self_, _self1_):
    file_exists = exists(logfile)
    if(file_exists):
        with open(logfile, 'a') as f:
            f.write(f'{_self_} -- {str_dt} -- {_self1_} \n')
            f.close()
    else:
        with open(logfile, 'w') as g:
            g.write('---- LOG BEGIN ----\n')
            g.write(f'{_self_} -- {str_dt} -- {_self1_} \n')
            g.close()