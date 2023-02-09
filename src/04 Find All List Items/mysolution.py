def getindex(indexinput, lookup):
    indexlist = []
    for index, value in enumerate(indexinput):
        if value == lookup:
            indexlist.append([index])
        elif isinstance(indexinput[index], list):
            for i in getindex(indexinput[index], lookup):
                indexlist.append([index] + i)
    return indexlist
