from dis import findlabels
import renamer
import fileseparator as filesep
import logger
import shutil
from datetime import datetime

dt = datetime.now()
str_dt = dt.strftime("%d-%m-%Y, %H:%M:%S")
srcPDFpath = 'C:/BOT/Retriever_NFe/Files/Original/NFes/'
srcXMLpath = 'C:/BOT/Retriever_NFe/Files/Original/XMLs/'
destPDFsrcpath = 'N:/NOTAS-FISCAIS/OneDrive - HARTMANN BRASIL/NFE - Fiscal/'
PDFfiles = filesep.createList(srcPDFpath)
XMLfiles = filesep.createList(srcXMLpath)

amIRunning = True

def slicer(_self_):
    if _self_.endswith('.pdf'):
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
    else:
        try:
            s = _self_
            ss = s.split('.')
            presplit = ss[0].split('e')
            firstsplit = presplit[1]
            firstslice = slice(0, len(firstsplit)//2+12)
            secondsplit = firstsplit[firstslice]
            finalslice = slice(28, len(secondsplit))
            finalsplit = secondsplit[finalslice]
            y = len(finalsplit)
            return(finalsplit)
        except:
            logger.makeLog(_self_, 'erro')

def movefile(filename):
    if filename.endswith('.pdf'):
        src_srcpath = f'{srcPDFpath}{filename}'
        dst_srcpath = f'{destPDFsrcpath}{filename}'
        shutil.move(src_srcpath, dst_srcpath)
    else:
        src_srcpath = f'{srcXMLpath}{filename}'
        dst_srcpath = f'{destPDFsrcpath}{filename}'
        shutil.move(src_srcpath, dst_srcpath)

def exePDF():
    for each in PDFfiles:
        formatedstring = slicer(each)
        arrange = f"DANFE{formatedstring}.pdf"
        print(arrange)
        logger.makeLog(arrange, each)
        renamer.rename(srcPDFpath, each, arrange)
        movefile(arrange)

def exeXML():
    for each in XMLfiles:
        formatedstring = slicer(each)
        arrange = f"DANFE{formatedstring}.xml"
        print(arrange)
        logger.makeLog(arrange, each)
        renamer.rename(srcXMLpath, each, arrange)
        movefile(arrange)

def callup():
    print(f"rodando exePDF em {str_dt}")
    exePDF()
    print(f"rodando exeXML em {str_dt}")
    exeXML()

print("Iniciando rotina do CoreMain")
callup()