from asyncio.windows_events import NULL
from importlib.metadata import files
import time
import shutil
import subprocess
from weakref import CallableProxyType
import logger
from datetime import datetime

#Come crawling fasteeeeeer!
#Obey your Masteeer!
#Your life burns fasteeeeeer!
#Obey your...
#MASTER! MASTER!

IamRunning = True
dt = datetime.now()
str_dt = dt.strftime("%d-%m-%Y, %H:%M:%S")

movescript = 'C:/BOT/Retriever_NFe/scripts/filemover/runMovefiles.bat'
corescript = 'C:/BOT/Retriever_NFe/scripts/core/runCoreMain.bat'

def callMoveScript():
    try:
        if subprocess.call(movescript):
            return(f"movescript - Sucesso em {str_dt}")
        else:
            return(f"movescript - SEM Sucesso em {str_dt}")
    except:
        print(f"movescript: erro em {str_dt}")
        logger.makeLog('movescript', 'erro')
        return(f"movescript - ERRO em {str_dt}")

def callCoreScript():
    try:
        if subprocess.call(corescript):
            return(f"movescript - Sucesso em {str_dt}")
        else:
            return(f"movescript - SEM Sucesso em {str_dt}")
    except:
        print(f"movescript: erro em {str_dt}")
        logger.makeLog('movescript', 'erro')
        return(f"movescript - ERRO em {str_dt}")

def callScripts(_self_):
    if _self_ == 'MakeMove':
        if callMoveScript():
            logger.makeLog('CallScripts', 'MakeMove')
            return(callScripts('Moved'))
    elif _self_ == 'Moved':
        if callCoreScript():
            logger.makeLog('CallScripts', 'Moved')
            return(callScripts('CoreApplied'))
    elif _self_ == 'CoreApplied':
            logger.makeLog('CallScripts', 'CoreApplied')
            return(callScripts('CompletedCicle'))
    elif _self_ == 'CompletedCycle':
            logger.makeLog('CallScripts', 'CoreApplied')
            print(f"Em espera desde {str_dt}")
            time.sleep(120)
            return(callScripts('MakeMove'))
    elif _self_ == "":
        print("NULL - Empty String")
        logger.makeLog('CallScripts', 'NULL - Chamando MakeMove')
        return(callMoveScript('MakeMove'))
        
while IamRunning:
    print(f'Começando rotina em {str_dt}')
    callScripts('MakeMove')