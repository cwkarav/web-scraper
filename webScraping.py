from bs4 import BeautifulSoup
import requests, string
from collections import Counter

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

def get_words_list(url):
    text = requests.get(url).text
    soup = BeautifulSoup(text, "html5lib")
    x = soup.find(id="priceblock_ourprice")
    print(x.text)
    
    x = soup.find(id="comparison_title1")
    new_url = "https://www.amazon.com" + x.find('a').get('href')
    print(new_url)
    get_words_list(new_url)

    for i in string.punctuation:
        text = text.replace(i, "")
    text_list = text.split()
    word_counts = Counter(text_list).most_common(50)
    return word_counts

def main():
    url = "https://www.amazon.com/gp/product/B004HZGR5Q/ref=s9u_qpp_gw_i4?ie=UTF8&fpl=fresh&pd_rd_i=B004HZGR5Q&pd_rd_r=d2afae98-c107-11e7-b4af-bb8759a2f7d7&pd_rd_w=IJSfn&pd_rd_wg=dv3PO&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=&pf_rd_r=341FGX8R18EPS1EAC58P&pf_rd_t=36701&pf_rd_p=f719e185-4825-42a4-9507-9df1a19229d6&pf_rd_i=desktop"
    words_list = get_words_list(url)

if __name__ == "__main__":
    main()
    
def plot_words(words_list):
    words = []
    numbers = []
    for (w,n) in words_list:
        words.append(w)
        numbers.append(n)
        
    index = np.arange(len(words))
    
    fig = plt.figure()
    plt.bar(index, numbers)
    plt.xticks(index + .5, words, rotation="verctical", size="x-small")
    fig.savefig("guitar")
