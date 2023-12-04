
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
    
    #wordnik only accesses word as lowercase
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





