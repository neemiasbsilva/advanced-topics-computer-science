
def query_function(querys, synonyms):

    for query in querys:
        query = query.split(' ')
        for word in query:
            if synonyms.get(word) == None:
                return False
    
    return True 


if __name__ == '__main__':
    
    st_string = "taxa coronavirus MS"
    st_string_split = st_string.split(' ')
    nd_string = "percentual covid MS"
    nd_string_split = nd_string.split(' ')

    synonyms = {}

    for i in range(len(st_string_split)):
        synonyms[st_string_split[i]] = nd_string_split[i]
        synonyms[nd_string_split[i]] = st_string_split[i]

    querys = ["taxa coronavirus MS", "percentual MS"]

    print(query_function(querys, synonyms))
    
    
