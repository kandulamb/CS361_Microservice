from bs4 import BeautifulSoup
import requests
import random

# text generation function
# Based on these two tutorials:
# 1) https://www.geeksforgeeks.org/web-scraping-from-wikipedia-using-python-a-complete-guide/
# 2) https://www.freecodecamp.org/news/scraping-wikipedia-articles-with-python/
def text_generation(links):
    # open a webpage with http requests
    response = requests.get(
    	url="https://en.wikipedia.org" + links[0],
    )
    # parse it with beautiful soup so that we can pull a paragraph from it
    soup = BeautifulSoup(response.content, 'html.parser')

    # set our randomly generated text variable with beautiful soup commands
    returnText = soup.find_all('p')[0].get_text()
    print(returnText)

    pageLinks = soup.find(id="bodyContent").find_all("a")
	random.shuffle(pageLinks)

    # just for fun add a random wiki page to the possible links for next call
    for link in pageLinks:
        # skip non-wiki links
        if pageLinks[linkIndex]['href'].find("/wiki/") == -1:
            continue
        # otherwise, add this wiki link to possible links and exit the loop
        links.append(link['href'])
        break

    return returnText

# Setup communication channel


# Receive Request


# Generate the text
    possibleLinks = ["/wiki/Link_farm", "/wiki/Belgian_National_Day", "/wiki/White-nosed_saki"]
    random.shuffle(possibleLinks)
    message = text_generation(possibleLinks)

# Send the Response
