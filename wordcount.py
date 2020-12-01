from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import re
import hashlib

newsList=["londonnews.txt","delhinews.txt","chengdunews.txt","berlinnews.txt","istanbulnews.txt","moscownews.txt"]

stopwords= open("stopWords.txt", encoding="utf8").read().lower().rstrip().split("\n")
positivewords= open("PositiveWordList.txt", encoding="utf8").read().lower().split(" ")
negativewords= open("NegativeWordList.txt", encoding="utf8").read().split(" ")

class CityWordFreq():
    def __init__(self):
        self.stopFrequency=[0]
        self.positiveFrequency=[0]
        self.negativeFrequency=[0]
        self.stopDic=dict()
        self.positiveDic=dict()
        self.negativeDic=dict()
        self.politicalSentiment=[0]

def testHash(string):
    result =hashlib.md5(string.encode())
    final = result.hexdigest()
    return final

# Modified Rabin Karp algorithm to eliminate stop words
def rabinRemoveStop(hashmap,stopwords,stopF):
    p=0 #hash value for hashmap key
    t=0 #hash value for stopword
    newDic=dict()
    freq = 0

    for key,value in hashmap.items():
        cont = False
        p=testHash(key)
        for word in stopwords:
            t=testHash(word)
            if(p==t):
                freq += value
                cont=True
                break

        if(cont==False):
            newDic[key] = value
    stopF[0] += freq
    return newDic

# optimized version to eliminate stop words
def removeStopFromDic(hashmap,stopwords,stopF,stopDic):
    eliminateStop = dict()
    freq=0
    for key,value in hashmap.items():
        if(key in stopwords):
            freq+=value
            stopDic[key] = value
        if(key not in stopwords):
            eliminateStop[key]=value
    stopF[0]+=freq
    return eliminateStop

# rabin karp version to get political sentiment and word counts
def rabinCountFreq(hashmap,positivewords,negativewords,positiveF,negativeF,politicalSentiment):
    p = 0  # hash value for hashmap key
    t = 0  # hash value for stopword
    newDic = dict()
    negativefreq = 0
    positivefreq = 0
    for key, value in hashmap.items():
        p = testHash(key)
        for word in negativewords:
            t = testHash(word)
            if (p == t):
                negativefreq += value
                break
        for word in positivewords:
            t = testHash(word)
            if (p == t):
                positivefreq += value
                break
    positiveF[0] += positivefreq
    negativeF[0] += negativefreq
    fraction = positivefreq / (positivefreq + negativefreq)
    politicalSentiment[0] += fraction

# optimized version to get political sentiment and word count
def countFreq(hashmap,positivewords,negativewords,positiveF,negativeF,politicalSentiment):
    negativefreq = 0
    positivefreq = 0
    for key, value in hashmap.items():
        if (key in negativewords):
            negativefreq += value
        if (key in positivewords):
            positivefreq += value
    negativeF[0] += negativefreq
    positiveF[0] += positivefreq
    fraction = positivefreq/(positivefreq+negativefreq)
    politicalSentiment[0] +=fraction


# Given a list of words, return a dictionary of
# word-frequency pairs.
def wordListToFreqDict(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    return dict(zip(wordlist,wordfreq))

# Function to get text from URL, and return a word_list
def getWords(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

    web_byte = urlopen(req).read()

    html = web_byte.decode('utf-8')
    # html = urllib.request.urlopen(url).read()
    web_word_list = BeautifulSoup(html, features="html.parser")

    # kill all script and style elements
    for script in web_word_list(["script", "style"]):
        script.extract()  # rip it out
    # get the word list
    #[^\w] in re package means all character excluding (characters from a to Z, digits from 0-9, and the underscore _ character)
    # replace characters in [^\w] with " " (empty space)
    web_word_list = re.sub("[^\w]", " ", web_word_list.get_text().lower()).split()
    return web_word_list

def testThread(news,return_list,positivelist,negativelist,politicalList):
    frequencyObj = CityWordFreq()
    mynews = open(news, encoding="utf8").read().lower().rstrip().split("\n")
    for newss in mynews:
        wordlist = getWords(newss)
        dictionary = wordListToFreqDict(wordlist)
        # newdic is the dictionary after eliminating stop words
        # rabinCountFreq is slower version to get political sentiment using rabin karp algorithm
        newdic = rabinRemoveStop(dictionary, stopwords, frequencyObj.stopFrequency)
        rabinCountFreq(newdic,positivewords,negativewords,frequencyObj.positiveFrequency,frequencyObj.negativeFrequency,frequencyObj.politicalSentiment)
        # countFreq is optimized version to get political sentiment
        # newdic = removeStopFromDic(dictionary, stopwords, frequencyObj.stopFrequency, frequencyObj.stopDic)
        # countFreq(newdic,positivewords,negativewords,frequencyObj.positiveFrequency,frequencyObj.negativeFrequency,frequencyObj.politicalSentiment)

    # to save the frequency and political sentiment value into dictionary
    if (news == "londonnews.txt"):
        return_list['London']=frequencyObj.stopFrequency[0]
        positivelist['London'] = frequencyObj.positiveFrequency[0]
        negativelist['London'] = frequencyObj.negativeFrequency[0]
        politicalList['London'] = frequencyObj.politicalSentiment[0]

    elif (news == "delhinews.txt"):
        return_list['Delhi'] = frequencyObj.stopFrequency[0]
        positivelist['Delhi'] = frequencyObj.positiveFrequency[0]
        negativelist['Delhi'] = frequencyObj.negativeFrequency[0]
        politicalList['Delhi'] = frequencyObj.politicalSentiment[0]

    elif (news == "chengdunews.txt"):
        return_list['Chengdu']=frequencyObj.stopFrequency[0]
        positivelist['Chengdu'] = frequencyObj.positiveFrequency[0]
        negativelist['Chengdu'] = frequencyObj.negativeFrequency[0]
        politicalList['Chengdu'] = frequencyObj.politicalSentiment[0]

    elif (news == "berlinnews.txt"):
        return_list['Berlin']=frequencyObj.stopFrequency[0]
        positivelist['Berlin'] = frequencyObj.positiveFrequency[0]
        negativelist['Berlin'] = frequencyObj.negativeFrequency[0]
        politicalList['Berlin'] = frequencyObj.politicalSentiment[0]

    elif (news == "istanbulnews.txt"):
        return_list['Istanbul']=frequencyObj.stopFrequency[0]
        positivelist['Istanbul'] = frequencyObj.positiveFrequency[0]
        negativelist['Istanbul'] = frequencyObj.negativeFrequency[0]
        politicalList['Istanbul'] = frequencyObj.politicalSentiment[0]

    else:
        return_list['Moscow']=frequencyObj.stopFrequency[0]
        positivelist['Moscow'] = frequencyObj.positiveFrequency[0]
        negativelist['Moscow'] = frequencyObj.negativeFrequency[0]
        politicalList['Moscow'] = frequencyObj.politicalSentiment[0]
