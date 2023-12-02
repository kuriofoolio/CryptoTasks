

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


   





