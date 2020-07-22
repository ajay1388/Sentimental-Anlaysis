from string import digits
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from collections import Counter
import matplotlib.pyplot as plt
import re


#reading text file
text = open('read.txt',encoding='utf-8').read()

#Remove Numbers
cleaned_text = ''.join([i for i in text if not i.isdigit()])

#Remove Links
cleaned_text = re.sub(r'https?:\/\/\S*', '', cleaned_text, flags=re.MULTILINE)

#convert text to lower case
cleaned_text = cleaned_text.lower()

#Remove all punctuations i.e. (!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~)
#str1 : specifies list of characters which need to be replaced
#str2 : specifies list of characters with which the characters need to be replaced
#str3 : specifies the list of characters that need to be deleted
cleaned_text = cleaned_text.translate(str.maketrans('','',string.punctuation))

#splitting text into words
tokenized_words = word_tokenize(cleaned_text,"english")

#remove stop words
#words that do not add any meaning to the sentence
final_list = []
for word in tokenized_words:
    if word not in stopwords.words("english"):
        final_list.append(word)

def lemmatization(filtered_sent):
    lem = WordNetLemmatizer()

    lemmatized_words = []
    for w in filtered_sent:
        lemmatized_words.append(lem.lemmatize(w))
    return lemmatized_words

final_list = lemmatization(final_list)
print(final_list)
print()

#match emotions
emotion_list = []
with open('emotions.txt','r') as file:
    for line in file:
        clear_line = line.replace("\n","").replace(",","").replace("'",'').strip()
        word,emotion = clear_line.split(":")

        if word in final_list:
            emotion_list.append(emotion)

w=Counter(emotion_list)

fig, axl = plt.subplots()
#axis automatically updates
axl.bar(w.keys(),w.values())
#automatically updates axis to make sure all vaues are plotted properly
fig.autofmt_xdate()
plt.savefig('graph.png')
#plt.show()

if len(w)!=0:
    print(w.most_common()[0][0].upper()+" SENTIMENT")
else:
    print("NEUTRAL SENTIMENT")
