from tkinter import NO
import warnings
warnings.filterwarnings('ignore')
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
import re
import string

nlp = spacy.load("en_core_web_sm")

# def calculate_Actual_Score(skill_score_req,loc_score_req,experiance_req,score,location_search,city,MinExpReq):
    
#     value = (skill_score_req*score)/100
   
#     if((len(location_search)>0) or (len(city)>0)):
#         if((location_search.lower().strip()) in (city.lower().strip())):
#             value = value + loc_score_req
#     print("Exp from request",experiance_req)        
#     print("From database",MinExpReq)
#     print(type(MinExpReq))
#     if(MinExpReq == None):
#         return value
#     elif(MinExpReq == 0 ):
#         value= value + experiance_req
#     elif(MinExpReq>=experiance_req):
#         value= value + experiance_req
#     else:
#          print()
    
#     return value

def calculate_Actual_Score(skill_score_req,loc_score_req,experiance_req,score,location_search,city,MinExpReq,expsearch,MaxExpDb):
    
    value = (skill_score_req*score)/100
   #loc_sore_req= parameter from api request %
   #location_search= city from api request
   #city is from database city of candidate.
   #experiance_req==> from api %  wrong now
   #MinExpReq= From Db=> mmin exp required.
   #expsearch= from api ==>ExperienceSearch number of year exp person should have
   #MaxExpDb=> Max exp comming from db
   #change experiance_req to ExperienceSearch and exp_req in %==> Max exp tackle karo
   #tackle null values in location.
    #print("Location Search:",loc_score_req," LOcation search, City",location_search," city",city)
    
    #print(type(city),"Type of city")
    #print(type(location_search))
    try:
        if(loc_score_req>0):
        #if((len(location_search)>0) and (len(city)>0)):
            if((location_search==None) or (city==None)):
                print("Location(City) is null in db or api")
            elif((location_search.lower().strip()) in (city.lower().strip())):
                value = value + loc_score_req
            else:
                print("CITIES DO NOT MATCH")    
     #   print("Exp from request",expsearch)        
      #  print("From database",MinExpReq)
       # print(type(MinExpReq))

    except:
        print("%%%%%%%%  An Error occured Here  %%%%%%%%%%%%%")

    finally:    
        #print("Min exp From database: ",MinExpReq)
        #print("MAx exp from db: ",MaxExpDb)
        #print("From api",expsearch)
        if((MinExpReq == None) or (MinExpReq == 0)):
            return value
    #    elif(MinExpReq == 0 ):
     #       value= value + 0
       # elif( ((MaxExpDb == None) or (MaxExpDb<MinExpReq)) and (MinExpReq>=expsearch)):   #Max cant be less but since db has meta data 
        #    value= value + experiance_req
        elif( (MinExpReq>=expsearch) or (MaxExpDb>=expsearch) ):
           value= value + experiance_req
        else:
            print("^^^^Experiance issue^^^^")
    
    return value
    







def calculate_similarity(resume_text, job_description):  # calculating similarity using NLP
        base = nlp(resume_text)
        compare = nlp(job_description)
        return base.similarity(compare)

def ngrams(string, n=3):
        string = string.encode("ascii", errors="ignore").decode()
        string = string.lower()
        chars_to_remove = [')', '(', '.', '|', '[', ']', '{', '}', "'", '/']
        rx = '[' + re.escape(''.join(chars_to_remove)) + ']'
        string = re.sub(rx, '', string)  # remove the list of chars defined above
        string = string.replace('&', 'and')
        string = string.replace(',', ' ').replace('-', ' ')
        string = string.title()  # Capital at start of each word
        string = re.sub(' +', ' ', string).strip()  # combine whitespace
        string = ' ' + string + ' '  # pad
        string = re.sub(r'[,-./]|\sBD', r'', string)
        ngrams = zip(*[string[i:] for i in range(n)])
        return [''.join(ngram) for ngram in ngrams]

def tfidf_match(list1, list2):
        # For each item in list1, find the match in list2
        list1 = list(set(list1))
        list2 = list(set(list2))
        list1 = [''.join(x for x in par if x not in string.punctuation) for par in list1]
        list2 = [''.join(x for x in par if x not in string.punctuation) for par in list2]
        res1 = []
        for ele in list1:
            if ele.strip():
                res1.append(ele)
        list1 = res1

        res2 = []
        for ele in list2:
            if ele.strip():
                res2.append(ele)
        list2 = res2

        vectorizer = TfidfVectorizer(analyzer=ngrams, lowercase=False)
        tfidf = vectorizer.fit_transform(list2)
        neighbors = NearestNeighbors(n_neighbors=1, n_jobs=-1).fit(tfidf)
        distances, indices = neighbors.kneighbors(vectorizer.transform(list1))

        matches = [(round(distances[i][0], 2), list1[i], list2[j[0]]) for i, j in enumerate(indices)]
        matches = pd.DataFrame(matches, columns=['score', 'original', 'matched'])
        return matches

def ResponseFunc(result):
    res_list =[]
    for ind in range(len(result)):
        try:
            dta = {"CandidateId":int(result.loc[ind][1]),
               "CandidateName":result.loc[ind][2],
               "City":result.loc[ind][3],"Mobile_Phone":result.loc[ind][4],
               "Email": result.loc[ind][5],
               "TotalMatch":int(result.loc[ind][6]),"Rank":int(result.loc[ind][0]) }
            res_list.append(dta)
        except:
            print("Appending ",ind," is Failed")
    return res_list
