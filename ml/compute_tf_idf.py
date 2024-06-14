# a user defined way of computing tf idf for word embeddings

import math

N,df, tf , info_dict =3,3, [50,10,2], {}

def compute_idf(N:int,df:int):
    return math.log((N+1)/(df+1))+1

info_dict ['idf']= compute_idf(N,df)

wtd = [ i*compute_idf(N,df) for i in tf]
info_dict['wtd']=wtd

squared_wtd = list(map(lambda x: x ** 2, wtd))

divisor= math.sqrt(sum(squared_wtd))
info_dict['divisor']=divisor


normalized= [i/divisor for i in wtd]
info_dict['normalized']=normalized

print(info_dict)