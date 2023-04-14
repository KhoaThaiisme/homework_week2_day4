list1 = [1,2,3]
list2 = ['a','b','c']

def alternatingList(list1, list2):
    alteratedList = []
    for i in range(len(list1)):
        alteratedList.append(list1[i])
        alteratedList.append(list2[i])
    print(alteratedList)



alternatingList(list1, list2)   

def zippered_list(list_1, list_2):
    zippered_list = list_1[::]
    for item in reversed(list_2):
        zippered_list.insert(list_2.index(item) +1, item)
    return zippered_list