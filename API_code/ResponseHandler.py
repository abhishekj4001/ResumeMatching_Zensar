from asyncio.windows_events import NULL
from re import A
from Configuration import *
from AlgoFunc import *
import nltk

def handle_response(extractedSkills, srf_desc,skill_weight,Location_score,exp_weight,location_search,expsearch):
    result = pd.DataFrame(columns=[candidateId, candidateName, city, mobile, email, scoreMark, matchedSkillList, actualS])
    for i in range(len(extractedSkills)):
        try:
            
            score = round(calculate_similarity(str(srf_desc), str(extractedSkills[i][1])) * 100, 2)
            print(score,"Score i=:",i+1)
            actualScore = calculate_Actual_Score(skill_weight,Location_score,exp_weight,score,location_search,extractedSkills[i][6],extractedSkills[i][7],expsearch,extractedSkills[i][8])
            print(actualScore,"actual score: i=",i+1)
            matches = tfidf_match([w for w in str(extractedSkills[i][1]).split(",") if w != "."],
                          list(nltk.word_tokenize(str(srf_desc))))
            matchedSkills = matches['matched'].tolist()
            if(matchedSkills==NULL):
                result = result.append({candidateId: extractedSkills[i][0],
                                candidateName:extractedSkills[i][2]+" "+extractedSkills[i][3],
                                email:extractedSkills[i][4],
                                mobile:extractedSkills[i][5],
                                city:extractedSkills[i][6],
                                scoreMark: actualScore, matchedSkillList: NULL},
                           ignore_index=True)
            else:    
                result = result.append({candidateId: extractedSkills[i][0],
                                candidateName:extractedSkills[i][2]+" "+extractedSkills[i][3],
                                email:extractedSkills[i][4],
                                mobile:extractedSkills[i][5],
                                city:extractedSkills[i][6],
                                scoreMark: actualScore, matchedSkillList: matchedSkills},
                           ignore_index=True)
            #print("Skills successfully compared : ",(i+1))
        except:
            # print(score )
            print("Skills Comparison failed for : ",(i+1))

    result.sort_values(by='score', inplace=True, ascending=False)
    result.insert(0, 'rank', [x for x in range(1, result.shape[0] + 1)])
    #result.set_index(['rank'],inplace=True)
    print("************************")
    print(result)
    print("Similarity Function Run successfully")
    return result
