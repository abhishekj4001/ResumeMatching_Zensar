import warnings
warnings.filterwarnings('ignore')
import pyodbc
import pandas as pd
import requests
import os
from datetime import datetime
from resume_parser import resumeparse
from Configuration import *

def database_connection():
    conn = pyodbc.connect('Driver={%s};Server=%s;Database=%s;UID=%s;PWD=%s;Trusted_Connection=%s'
                          % (driverName, serverName, dbName,uID,pwd, connectionTrust))
    cursor = conn.cursor()
    print("Database connection made")
    return cursor,conn

def get_candidate_details():
    print("get_candidate_details() function called")
    cursor,conn = database_connection()
    cursor.execute('''SELECT CandidateID,Attachment_FileName,Attachment_FileContent FROM CandidateProfile''')
    #cursor.execute('''SELECT CandidateID,Attachment_FileName,Attachment_FileContent FROM CandidateProfile ORDER BY ID OFFSET 150 ROWS FETCH NEXT 50 ROWS ONLY;''')
    candidate_profile = cursor.fetchall()
    conn.commit()

    candidate_dataframe = pd.DataFrame([tuple(t) for t in candidate_profile],
                      columns=['CandidateID', 'Attachment_FileName', 'Attachment_FileContent'])
    print(candidate_dataframe)
    return candidate_dataframe
	
	
def extract_AI_skills(candidate_id,file_name):
    try:
        cursor, conn = database_connection()
        new_path = os.path.join("E:/Resumes_Data/"+candidate_id+ "_" + file_name)
        print('new_path :: ',new_path)
        try:
            data = resumeparse.read_file(new_path)
        except:
            print("resume parser error")
        print(candidate_id,':: ',data['skills'])
        #cursor.execute('''UPDATE CandidateProfile set Ai_Extracted_Skills=?,Ai_Extracted_Skills_Lud=? where CandidateID=? and (Attachment_LUD > Ai_Extracted_Skills_Lud or Ai_Extracted_Skills is null)''',(data['skills'],datetime.now(),candidate_id))
        cursor.execute(
            '''UPDATE CandidateProfile set Ai_Extracted_Skills=?,Ai_Extracted_Skills_Lud=? where CandidateID=?''',
            (str(data['skills']), datetime.now(), candidate_id))

        conn.commit()
        print("Skills Insertion in Database Successful : ",candidate_id)
        print('\n\n')
    except:
        print("Skills insertion failed : ",candidate_id)
    
