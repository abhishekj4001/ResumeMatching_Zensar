
import warnings
warnings.filterwarnings('ignore')
import pyodbc
import warnings
warnings.filterwarnings('ignore')
from AlgoFunc import *
from Configuration import *

#use this when there is no user and pass in database 
# def get_extracted_skills(srf_desc):
#     conn = pyodbc.connect('Driver={%s};Server=%s;Database=%s;Trusted_Connection=%s'
#                           % (driverName, serverName, dbName,  connectionTrust)) #Move it to properties file

def get_extracted_skills(srf_desc):
    conn = pyodbc.connect('Driver={%s};Server=%s;Database=%s;UId=%s;PWD=%s'
                          % (driverName, serverName, dbName, uid, pas)) #Move it to properties file

    cursor = conn.cursor()
    print("Database connection made")

    # cursor.execute('''SELECT a.CandidateID,a.First_Name,a.Last_Name,a.Email,a.Mobile_Phone,a.City,b.ai_Appended_Skills FROM candidateprofile as a,
    #                   CandidateSkillList as b where a.CandidateID=b.CandidateID''')
                      #Move query to some another text file
    cursor.execute(select)
    extractedSkills=cursor.fetchall()
    #print(extractedSkills)
    conn.commit()
    return extractedSkills
