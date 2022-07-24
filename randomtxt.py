from bs4 import BeautifulSoup
import requests
import random
import pika

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
        if link['href'].find("/wiki/") == -1:
            continue
        # otherwise, add this wiki link to possible links and exit the loop
        links.append(link['href'])
        break

    return returnText


# Setup communication channel
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='text_gen')

# What to do when we receive a request:
def on_request(chann, method, props, body):
    print(" [randomtxt.py] generating text....")
    # Generate the text
    possibleLinks = ["/wiki/Link_farm", "/wiki/Belgian_National_Day", "/wiki/White-nosed_saki"]
    random.shuffle(possibleLinks)
    message = text_generation(possibleLinks)
    print(f" [randomtxt] sending message: {message}")
    # And then send it back
    chann.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                         props.correlation_id),
                     body=str(message))
    chann.basic_ack(delivery_tag=method.delivery_tag)

# Actually receive requests and send responses
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='text_gen', on_message_callback=on_request)

print(" [randomtxt.py] Waiting for random text generation requests")
channel.start_consuming()
