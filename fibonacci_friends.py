def Xbonacci(signature,n):
    size_of_signature_beginning = len(signature)
    iteration = 0
    sum = 0

    while(iteration < (n - size_of_signature_beginning)):
        for i in range(iteration, len(signature)):
            sum += signature[i]
            
        signature.append(sum)
        iteration += 1
        sum = 0
    
    return signature[slice(0, n)]


print(Xbonacci([0,1],10))
print(Xbonacci([1,1],10))
print(Xbonacci([0,0,0,0,1],10))
print(Xbonacci([1,0,0,0,0,0,1],10))
print(Xbonacci([1,0,0,0,0,0,0,0,0,0],20))
print(Xbonacci([0, 0, 3, 6, 6, 9, 7, 1, 19, 8, 11, 8, 5, 9],2))
