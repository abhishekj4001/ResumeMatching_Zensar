import warnings
warnings.filterwarnings('ignore')
import urllib.request
from DatabaseConfig import *
from Configuration import *

def upload_document_on_server(candidate_id,base64String,file_name):
	try:
		with urllib.request.urlopen('file:////ze42-v-mbpolapp//ExtractedCV//SmartRecruit_ExtractCV//ExtractFolder/' + candidate_id+ "_" + file_name) as f:
			print("Document Already Exists :: ", candidate_id)
			return
	except:
		myobj = {"Base64String": base64String,"Attachment_FileName":candidate_id+ "_" +file_name}
		requests.post(smartRecruitExtractCV_URL, json=myobj)
		print("Upload Document Successfully :: ",candidate_id)
   
def download_document_on_system(candidate_id,file_name):
	try:
		with urllib.request.urlopen('file:////ze42-v-mbpolapp//ExtractedCV//SmartRecruit_ExtractCV//ExtractFolder/' +candidate_id+ "_" + file_name) as f:
			open(os.path.join(sysPath,candidate_id+ "_" + file_name),'wb').write(f.read())
			print("Download Document Successfully :: ",candidate_id)
	except:
		print("Document Doesn't exist :: ",candidate_id)

