a = ['88 99 200', '88 99 300', '99 32 100', '12 12 15']
b = 2
def processlogs(logs, threshold=0):
    id = [] #declared a list
    for i, v in enumerate(logs):
        separado = v.split(' ') #separeted list by each transaction
        if separado[0] != separado[1]: #make sure if 2 id appear in the same transaction they will be count as 1
            id.append(separado[0])
            id.append(separado[1])
        else:
            id.append(separado[0])
    quantidade = {} #declared a new dictionary
    for i, v in enumerate(id): #add to the dictionary the id and number of times it appears
        quantidade[v] = id.count(v)
    ids = []
    for i, v in quantidade.items():
        if v >= threshold:
            ids.append(v)
    return ids


print(processlogs(a, b))