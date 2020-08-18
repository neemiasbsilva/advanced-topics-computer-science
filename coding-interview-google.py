import importlib.util

spec = importlib.util.spec_from_file_location("module.name", "union-find.py")
union_find = importlib.util.module_from_spec(spec)
spec.loader.exec_module(union_find)


if __name__ == '__main__':
    

    synonyms = {}
    id = 0
    for i in range(int(input("Enter the number of Synonyms: "))):
        synonym = list(input().split(','))
        synonyms[synonym[0]] = id
        id += 1
        synonyms[synonym[1]] = id
        id += 1

    pset = [i for i in range(len(synonyms))]
    print(pset)
    uf = union_find.UnionFind(pset)

    for i in range(0, len(pset), 2):
        uf.unionSet(list(synonyms.values())[i], list(synonyms.values())[i+1])
    print(uf.pset)
    for i in range(int(input("Enter the number of querys: "))):
        strings = input().split(',')
        st_string = strings[0].split(' ')
        nd_string = strings[1].split(' ')
        equal = False
        for st_word, nd_word in zip(st_string, nd_string):
            if (synonyms.get(st_word) != None and synonyms.get(nd_word) != None) and uf.issameSet(synonyms[st_word], synonyms[nd_word]):
                equal = True
            elif st_word == nd_word :
                equal = True
            else:
                equal = False
                break
        
        print((lambda result: "true" if result == True else "false")(equal))
