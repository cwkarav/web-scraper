from bs4 import BeautifulSoup
import requests, string
from collections import Counter

def get_words_list(url):
    text = requests.get(url).text
    soup = BeautifulSoup(text, "html5lib")
    x = soup.find(id="priceblock_dealprice")
    print(x.text)
    x = soup.find(id="ccc-device-title")
    soup.find('div', )
    for i in soup.find_all("a"):
        print(i.get("href"))
    for i in string.punctuation:
        text = text.replace(i, "")
    text_list = text.split()
    word_counts = Counter(text_list).most_common(50)
    return word_counts

def main():
    url = "https://www.amazon.com/dp/B0758XXCSC/ref=ods_gw_ha_bt_tk?pf_rd_p=55c7d20b-0760-4c92-8d47-f38f565a5981&pf_rd_r=8K47AQMC61WCD3C5EHZR"
    words_list = get_words_list(url)

if __name__ == "__main__":
    main()