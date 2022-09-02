from importlib.metadata import files
from datetime import datetime
import shutil
import fileseparator as filesep
from os.path import exists

dt = datetime.now()
str_dt = dt.strftime("%d-%m-%Y, %H:%M:%S")
PDFlogfile = 'C:/BOT/Retriever_NFe/Files/Original/log/PDFlog.txt'
XMLlogfile = 'C:/BOT/Retriever_NFe/Files/Original/log/XMLlog.txt'
errorLog = 'C:/BOT/Retriever_NFe/Files/Original/log/Errorlog.txt'

#PDFs no Hanab1
srcPDF_path = 'Y:/TaxPlus/NFe/Produção/PDF/'

#Pasta de destino dos PDFs que são chamados do Hanab1
dstPDF_path = 'C:/BOT/Retriever_NFe/Files/Original/NFes/'

#Novo destino dos PDFs: Onedrive
oneDrivePDF_Path = 'N:/NOTAS-FISCAIS/OneDrive - HARTMANN BRASIL/NFE - Fiscal/'

#XMLs no Hanab1
srcXML_path = 'Y:/TaxPlus/NFe/Produção/Visualizar XML/'

#Pasta de destino dos XMLs que são chamados do Hanab1
dstXML_path = 'C:/BOT/Retriever_NFe/Files/Original/XMLs/'

#Novo destino dos PDFs: Onedrive
oneDrivePDF_Path = 'N:/NOTAS-FISCAIS/OneDrive - HARTMANN BRASIL/XML/'

def retrieveSent(file):
    finallist = []
    with open(file, 'r') as f:
        retrievedLog = f.read()
        f.close()
    loglist = retrievedLog.split(' -- ')
    for each in loglist:
        if each.endswith(".pdf"):
            finallist.append(each)
        elif each.endswith(".xml"):
            finallist.append(each)
    return(finallist)

def checkLog(pdfResponse, xmlResponse):
    pdfResponse = checkPDFLog()
    xmlResponse = checkXMLLog()
    if pdfResponse == 'OK':
        print("PDFLog encontrado")
        print("Verificando XMLLog")
    elif xmlResponse == 'OK':
        print("XMLLog encontrado")

def checkPDFLog():
        if exists(PDFlogfile):
            print("PDFLog.txt encontrado")
            return('OK')
        else:
            print("Criando PDFLog...")
            with open(PDFlogfile, 'w') as g:
                g.write('---- LOG BEGIN ----\n')
                g.close()
            return('Precisou criar')

def checkXMLLog():
    if exists(XMLlogfile):
        print("XMLLog.txt encontrado")
        return('OK')
    else:
        print("Criando XMLLog...")
        with open(XMLlogfile, 'w') as g:
            g.write('---- LOG BEGIN ----\n')
            g.close()
            return('Precisou criar')

def makePDFLog(_self_, _self1_):
    file_exists = exists(PDFlogfile)
    if(file_exists):
        print(f"PDFLog.txt encontrado -- Loggando: {_self_} em {str_dt}")
        with open(PDFlogfile, 'a') as f:
            f.write(f'{str_dt} -- {_self_} -- {_self1_} \n')
            f.close()
    else:
        checkPDFLog()

def makeXMLLog(_self_, _self1_):
    file_exists = exists(XMLlogfile)
    if(file_exists):
        print(f"XMLLog.txt encontrado -- Loggando: {_self_} em {str_dt}")
        with open(XMLlogfile, 'a') as f:
            f.write(f'{str_dt} -- {_self_} -- {_self1_} \n')
            f.close()
    else:
        checkXMLLog()

def pdflist():
    pdf_list = filesep.createList(srcPDF_path)
    dstPDFpath_list = retrieveSent(PDFlogfile)
    s = set(dstPDFpath_list)
    pdfsToMove = [x for x in pdf_list if x not in s]
    return(pdfsToMove)

def xmllist():
    xml_list = filesep.createList(srcXML_path)
    dstXMLpath_list = retrieveSent(XMLlogfile)
    d = set(dstXMLpath_list)
    xmlsToMove = [x for x in xml_list if x not in d]
    return(xmlsToMove)

def movePDF():
    for each in pdflist():
        if exists(f'{dstPDF_path}{each}'):
            makePDFLog(each, 'Já copiado')
        elif shutil.copyfile(f'{srcPDF_path}{each}', f'{dstPDF_path}{each}'):
            makePDFLog(each, 'Sucesso')

def moveXML():
    for each in xmllist():
        if exists(f'{dstXML_path}{each}'):
                makeXMLLog(each, 'Já copiado')
        elif shutil.copyfile(f'{srcXML_path}{each}', f'{dstXML_path}{each}'):
            makeXMLLog(each, 'Sucesso')

def callup():
    print(f"rodando checkPDF em {str_dt}")
    checkPDFLog()
    print(f"rodando checkXML em {str_dt}")
    checkXMLLog()
    print(f"Começando rotinas de movimentação de arquivos")
    print(f"rodando movePDF em {str_dt}") 
    movePDF()
    print(f"rodando moveXML em {str_dt}")
    moveXML()

print("Começando rotina -- bloco 'try-catch' a seguir")
try:
    callup()
except:
    print(f"erro em {str_dt}")