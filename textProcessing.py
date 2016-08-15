
def main():
        #read file
        file = open("peace.txt", "r")
        msg = file.readlines()
        file.close()

        #check for patterns
        countLove = 0
        countPeace = 0
        countUnity = 0 
        for words in msg:
            words = words.strip().upper()
         # print(words)

            if words.find ("LOVE") != -1:
               countLove = countLove + 1

            if words.find ("PEACE") != -1:
                countPeace = countPeace + 1

            if words.find ("UNITY") != -1:
                countUnity = countUnity + 1

        #display results
        print ("Love: ", countLove)
        print ("Peace : ", countPeace)
        print ("Unity : ", countUnity) 
    
     
