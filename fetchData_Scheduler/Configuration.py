import configparser

#Connection variables
config = configparser.ConfigParser()
config.read('db.properties')


driverName=config.get("db", "driverName")
serverName=config.get("db", "serverName")
dbName=config.get("db", "dbName")
uID=config.get("db","uID")
pwd=config.get("db","pwd")
connectionTrust=config.get("db", "connectionTrust")
fetchDataPort=config.get("db", "fetchDataPort")
sysPath=config.get("db", "sysPath")
getsmartCandidateData_URL=config.get("db", "getsmartCandidateData_URL")
smartRecruitExtractCV_URL=config.get("db", "smartRecruitExtractCV_URL")



#Variables for requested dataFrame
candidateId="CandidateID"
attachmentFileName="Attachment_FileName"
attachmentFileContent="Attachment_FileContent"
attachment_LUD="Attachment_LUD"


