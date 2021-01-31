import re

def is_isogram(string):
    
    strippedString = set(re.sub('[^a-zA-Z]','', string.lower()))
    return len(strippedString) == len(string.replace("-", "").replace(" ", ""))


