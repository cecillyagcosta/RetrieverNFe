from dis import findlabels
import renamer
import fileseparator as filesep
import logger
import shutil

srcXMLpath = 'C:/BOT/Retriever_NFe/Files/Original/XMLs/'
destsrcpath = 'N:/NOTAS-FISCAIS/OneDrive - HARTMANN BRASIL/XML/'
XMLfiles = filesep.createList(srcXMLpath)


def slicer(_self_):
    s = _self_
    ss = s.split('.')
    firstsplit = ss[0]
    firstslice = slice(0, len(firstsplit)//2+12)
    secondsplit = firstsplit[firstslice]
    finalslice = slice(28, len(secondsplit))
    finalsplit = secondsplit[finalslice]
    y = len(finalsplit)
    print(finalsplit)
    return(finalsplit)

def movefile(filename):
    src_srcpath = f'{srcXMLpath}{filename}'
    dst_srcpath = f'{destsrcpath}{filename}'
    shutil.move(src_srcpath, dst_srcpath)

for each in XMLfiles:
    formatedstring = slicer(each)
    arrange = f"{formatedstring}.xml"
    print(arrange)
    logger.makeLog(arrange, each)
    renamer.rename(srcXMLpath, each, arrange)
    movefile(arrange)