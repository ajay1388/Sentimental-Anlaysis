# Sentimental-Anlaysis

Sentiment Analysis, also known as opinion mining is a process of identifying and cataloging a piece of text according to the tone conveyed by it. This text can be tweets, comments, feedback, and even random rants with different sentiments associated with them.

## Pre-Requisites

  * Python IDE

  #### Python Libraries
  
  1. nltk
  2. collections
  3. matplotlib
  4. string

## Twitter Sentiment Analysis

  It is a Natural Language Processing Problem where sentiment analysis is done by Classifying the **Tweets** into different emotions for classification,text mining,text analysis,data analysis and data visualization....<br />Natural Language Processing(NLP) is a field that focuses on interactions between human language and computers.Most common application of NLP is Sentimental Analysis...<br /><br />We are interested in taking some predetermined body of text and performing upon it some basic analysis and transformations, in order to be left with main words which will be much more useful for performing some further, more meaningful analytic task afterward. This further task would be our core text mining or natural language processing work....
  
  Steps followed to clean the text are:
  
  1. **Tokenization**<br />
    Split longer sentences or strings of text into smaller pieces,or tokens...
  2. **Removing Stop Words**<br />
    Stop Words Provide little to no unique information that can be used for analyzing the tweets
  3. Removing **_Numbers_,_Links_,_Punctuation_** as they contribute nothing to sentiments
  4. **Lemmatization**<br />
    Convert each word to their root words....For lemmatization to resolve a word to its lemma, it needs to know its part of speech...

## Built With
  
  Lexical Analysis using Bag of Words
  It traverses the final list of words after all the pre processing is done and then check for each word in the bag of words(here emotions.txt)...And based upon that it classifies into different emptions(**_cheated_,_singled out_,_loved_,_attracted_,_sad_,_fearful_,_angry_,_esteemed_**)
