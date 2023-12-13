
import re,requests, os, hashlib

from dotenv import load_dotenv 

# Load any environment variables from .env
load_dotenv()
 

# this code checks whether public key exchange was successful using diffie hellman algorithm
def diffie_hellman(g:int,n:int,a :int, b:int )->None:
    # diffie hellman key exchange depends on the formula of primitive roots:
    # g^k mod n =a
    #where g is a real number that is relatively co-prime to n  
    # k is in the set {1,...,n-1}

    # Steps:
    # agree on g and n first 

    #generate private keys

    #compute with private keys
    A=pow(g,a,n)
    B=pow(g,b,n)
    # print(f'A: {A}\t B:{B}')

    # swap solutions above and recompute with private keys
    secret_A=pow(B,a,n)
    secret_B=pow(A,b,n)
    # print(f'secret_A: {secret_A}\t secret_B:{secret_B}')

    # confirm exchange was successful 
    try:
        assert (secret_A==secret_B)
        print('key exchange successful')
    except AssertionError:
        print('key exchange unsuccessful')

# this function removes html tags from a string 
def remove_html_tags(text):
    """Remove html tags from a string"""
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

# this function defines a word using wordnik api
def defineWord(word:str):
    
    #wordnik only accesses words as lowercase
    word=word.lower()

    # Access your wordnik API key
    wordnik_api_key = os.getenv("WORDNIK_API_KEY")

    hashed_api_key = hashlib.sha1(wordnik_api_key.encode()).hexdigest()

    url=f'https://api.wordnik.com/v4/word.json/{word}/definitions'
    params={
        'limit':200,
        'partOfSpeech':'noun',
        'includeRelated':'false',
        'sourceDictionaries':'wiktionary',
        'useCanonical':'false',
        'includeTags':'false',
        'api_key':f'{hashed_api_key}'
    }
    response=requests.get(url,params=params)
    try:
        return remove_html_tags(response.json()[0]['text'])
    except KeyError:
        return response.json()['message']




# this function finds the gcd of a number through recursion
def gcd(a, b):
    if(b == 0):
        return a
    else:
        return gcd(b,a%b)

#this function expresses a number as its prime factors
def factorize(num):
    factors = []

    # Find factors of 2
    while num % 2 == 0:
        factors.append(2)
        num = num // 2

    # Find factors of odd numbers starting from 3
    for i in range(3, int(num**0.5) + 1, 2):
        while num % i == 0:
            factors.append(i)
            num = num // i

    # If the remaining num is greater than 2, add it (it's a prime number)
    if num > 2:
        factors.append(num)

    return factors


#this function finds the euler totient of an odd number
def find_euler_totient(num:int)->int:
    totient=1
    factors=factorize(num)
    for f in factors:
        if f%2==0:
            continue
        factors_minused=[(f-1) for f in factors] 
    
    for f in factors_minused:
        totient*=f

    return totient



