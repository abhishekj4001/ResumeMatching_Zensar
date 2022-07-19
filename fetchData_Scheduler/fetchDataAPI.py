import warnings
warnings.filterwarnings('ignore')
from flask import Flask, render_template, request, redirect, url_for
from AlgoFunc import *
from DatabaseConfig import *
from Configuration import *

print("\n Run http://127.0.0.1:6060/fetchData", '\n')


def fetchData():
	print("fetchData() function is called")
	candidate_details=get_candidate_details()
	for i in range(len(candidate_details)):
		try:
			upload_document_on_server(candidate_details.loc[i][candidateId],candidate_details.loc[i][attachmentFileContent],candidate_details.loc[i][attachmentFileName])
			download_document_on_system(candidate_details.loc[i][candidateId],candidate_details.loc[i][attachmentFileName])
			extract_AI_skills(candidate_details.loc[i][candidateId],candidate_details.loc[i][attachmentFileName])
		except:
			print("Error either in uploading or downloading file :: ",candidate_details.loc[i][candidateId])


    
fetchData()
#app = Flask(__name__)
#@app.route('/', methods=['GET','POST'])
##def apiRequest():
##    print("Welcome fetchData API Request")
##    fetchData()
##    print("Program run successfully")
##    return "<h1>This API works correctly</h1>"
##
##if __name__ == '__main__':
##	print("main method")
##	apiRequest()
##	app.run(debug=False,port=fetchDataPort)
