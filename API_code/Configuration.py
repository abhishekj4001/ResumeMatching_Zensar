import configparser

#Connection variables
config = configparser.ConfigParser()
config.read('db.properties')

driverName=config.get("db", "driverName")
serverName=config.get("db", "serverName")
uid=config.get("db", "UId")
pas=config.get("db", "PWD")
dbName=config.get("db", "dbName")
connectionTrust=config.get("db", "connectionTrust")
portNo=config.get("db", "demoCodePort")


portNo=config.get("db", "fetchDataPort")
sysPath=config.get("db", "sysPath")
URL=config.get("db", "getsmartCandidateDataURL")

# matcher_py #flag 
#Query for fetching the data from DATABASE--> when you want to use 2 tables
# select = '''SELECT a.CandidateID,b.aiExtractedSkills,a.First_Name,a.Last_Name,a.Email,a.Mobile_Phone,a.City,a.TOTAL_EXPERIENCE_FROM FROM candidateprofile as a,

#                       CandidateSkillList as b where a.CandidateID=b.CandidateID'''

select = 'SELECT CandidateID, Ai_Extracted_Skills, First_Name, Last_Name, Email, Mobile_Phone, City, TOTAL_EXPERIENCE_FROM,TOTAL_EXPERIENCE_TO FROM candidateprofile where Ai_Extracted_Skills is not null'

#Variables for requested json
actualS = "actualScore"
email = "email"
candidateId = "candidateId"
candidateName = "candidateName"
city = "city"
mobile = "mobile"
matchedSkillList = "matchedSkillList"
scoreMark="score"
LocationWeightage ='LocationWeightage'
SkillWeightage ='SkillWeightage'
ExperienceWeightage = 'ExperienceWeightage'
LocationSearch = 'LocationSearch'

SrfNo = 'SrfNo'
skill = 'Skills'
Job_Desc='Job_Description'
ExperienceSearch='ExperienceSearch'

# def makeconn():
#     conn = pyodbc.connect('Driver={%s};Server=%s;Database=%s;Trusted_Connection=%s'
#                           % (driverName, serverName, dbName, connectionTrust))

#     cursor = conn.cursor()
#     return cursor