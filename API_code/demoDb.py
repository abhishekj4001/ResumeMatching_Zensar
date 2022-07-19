import warnings
warnings.filterwarnings('ignore')
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
from nltk.corpus import stopwords
import nltk
from flask import Flask, request
import json
from AlgoFunc import *
from DatabaseConfig import *
from Configuration import *
from ResponseHandler import *
import flask

def calculate_result(srf_desc,skill_weight,Location_score,exp_weight,location_search,expsearch):
    extractedSkills = get_extracted_skills(srf_desc)  #From DatabaseConfig.py file
    #print(extractedSkills)
    #response handler py handle_response func from
    
    return handle_response(extractedSkills, srf_desc,skill_weight,Location_score,exp_weight,location_search,expsearch) #ResponseHandler py

app = Flask(__name__)

@app.route('/', methods=['POST'])
def apiRequest():
    content = request.json
    #print(content)
    if content[SrfNo][1].isdigit():
        result = calculate_result(content[Job_Desc],content[SkillWeightage],content[LocationWeightage],content[ExperienceWeightage],content[LocationSearch],content[ExperienceSearch])
        res_list = ResponseFunc(result)  #From AlgoFunc.py file
        json_data  = json.dumps(res_list, indent=4)
        print("Response sent successfully")
        return json_data
    else:
        status_code=flask.Response(status=404)
        return status_code

#if __name__ == '__main__':
    #app.run(debug=False,port=portNo)










## ## ##
    # result = pd.DataFrame(columns=[candidateId, candidateName, city, mobile, email, scoreMark, matchedSkillList, actualS])
    # for i in range(len(extractedSkills)):
    #     try:
    #         score = round(calculate_similarity(str(srf_desc), str(extractedSkills[i][1])) * 100, 2)
    #         print("i7")
    #         print(extractedSkills[i][7])
    #         print("i7 above")
    #         actualScore = calculate_Actual_Score(skill_weight,Location_score,exp_weight,score,location_search,extractedSkills[i][6],extractedSkills[i][7])
    #         print( actualScore)
    #         matches = tfidf_match([w for w in str(extractedSkills[i][1]).split(",") if w != "."],
    #                       list(nltk.word_tokenize(str(srf_desc))))
    #         matchedSkills = matches['matched'].tolist()
    #         result = result.append({candidateId: extractedSkills[i][0],
    #                             candidateName:extractedSkills[i][2]+" "+extractedSkills[i][3],
    #                             email:extractedSkills[i][4],
    #                             mobile:extractedSkills[i][5],
    #                             city:extractedSkills[i][6],
    #                             scoreMark: actualScore, matchedSkillList: matchedSkills},
    #                        ignore_index=True)
    #         #print("Skills successfully compared : ",(i+1))
    #     except:
    #         # print(score )
    #         print("Skills Comparison failed for : ",(i+1))

    # result.sort_values(by='score', inplace=True, ascending=False)
    # result.insert(0, 'rank', [x for x in range(1, result.shape[0] + 1)])
    # #result.set_index(['rank'],inplace=True)
    # print("************************")
    # print(result)
    # print("Similarity Function Run successfully")
    # return result
    ## ## ##
