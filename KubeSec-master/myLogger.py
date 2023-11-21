import logging

def createLoggerObj(): 
    fileName  = 'ForensicReport.log' 
    formatStr = '%(asctime)s %(message)s'
    logging.basicConfig(format=formatStr, filename=fileName, level=logging.INFO)
    myLogObj = logging.getLogger('lzn0025-sqa2023-logger') 
    return myLogObj
