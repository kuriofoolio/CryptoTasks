

import numpy as np
key=np.array([
     [1,2,3],
    [4,5,6],
    [7,8,9]
])
   

# encrypt war

col_vec=[
    [22],
    [0],
    [17]

]

# print (np.dot(key,col_vec))

list=[73,190,307]
cipher=[]
[cipher.append(i%26) for i in list]
# print (cipher)

# #decrypting
key_inverse=np.linalg.inv(key)
prod=np.dot(key_inverse,[cipher])
# #simply assert if this plain is the same above
plain=[]
[plain.append(i%26) for i in prod]
print(plain)
# # [print(chr(j)) for j in plain]
# for i in plain:
#     print(i)




