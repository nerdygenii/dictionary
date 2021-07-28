import json
from difflib import get_close_matches

data = json.load(open("dictionary.json"))

def find(w):
    w=w.upper()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys()))>0:
        query=input('Did you mean %s if yes type Y if no type N ' % get_close_matches(w,data.keys())[0])
        if query.lower()=='y':
            return data[get_close_matches(w,data.keys())[0]]
        elif query.lower()=='n':
            return 'The word doesn\'t exist please double check it'
        else:
            return 'we do\'nt understand the word you\'re searching for'
    else:
        return 'The word doesn\'t exist please double check it'

word= input("input word: ")
output=find(word)
if type(output)==list:
    for i in output:
        print(i + '\n')
else:
    print(output)