caracteres = "[]()+-/*!¡&$#¿?=@abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890"

import random

contra = ""
num = int(input("Numero de caracters"))

for i in range(num):
    contra = contra + (random.choice(caracteres))

print(contra)
