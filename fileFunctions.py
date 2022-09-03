class fileFunctions:

    def __init__(self,filename,dictionary):
        self.filename = filename
        self.dictionary = dictionary        

    def createDictFile(filename, dictionary):
        f = open(str(filename),'w')
        dic_tuple = dictionary.items()
        for pair in dic_tuple:
            f.write(str(pair[0])+" ")
            f.write(str(pair[1]) + "\n")
        f.close()
    #Creates a file and appends a dictionary to that file through spacially organized 'Key' + ' ' + 'Value' + '\n' pairs

    def readDictFile(filename):
            d = {}
            try:
                f = open(str(filename),'r')
                for line in f:
                    (key,value) = line.split()
                    d[key] = int(value)
                f.close()
                return d
            except:
                return d
    #Reads a file created and organized through the createDictFile method and returns the full dictionary

    def incrementDict_N(dictionary,key,n):
        if key not in dictionary:
            dictionary[key] = n
        else:
            dictionary[key] += n
    #Increments by N a Value according to a Dictionary and Key; Creates this Key:Value pair if necessary

    def getScore(filename, name):
            d = fileFunctions.readDictFile(filename)
            score = d[name.lower()]
            return [name, score]
    #Returns a specified Key:Value pair for a File read through the readDictFile method