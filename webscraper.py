from bs4 import BeautifulSoup
import requests, string
from collections import Counter

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

def get_word_list(url):
    r = requests.get(url).text
    soup = BeautifulSoup(r, "html5lib")
    #text = soup.findAll('span',{"class":"scrolling-script-container"})[0].text.lower()
    text = soup.findAll('p')[0].text.lower()
    for char in string.punctuation:
        text = text.replace(char,"")
    text_list = text.split()
    counts = Counter(text_list).most_common(50)
    return counts
    
def plot_words(words_list):
    words=[]
    numbers=[]
    for(w,n) in words_list:
        words.append(w)
        numbers.append(n)
        
    index = np.arrange(len(words))
        
    fig=plt.figure()
    plt.bar(index,numbers)
    plt.xticks(index +.5, words, rotation="vertical", size="x-small")
    fig.savefig("plot_name")
    
def main():
    words_list = get_word_list("http://www.springfieldspringfield.co.uk/movie_script.php?movie=finding-nemo")
    print(words_list)    
    plot_words(words_list)
    
main()