# CS361_Microservice
Wikipedia-scraping random text generator

In order to connect to this micro-service, please follow these steps:
1) Install RabbitMQ per the instructions here: https://www.rabbitmq.com/download.html
2) Review this tutorial on Remote Procedure Call to understand how to setup a server-client relationship that talk to each other in RabbitMQ: https://www.rabbitmq.com/tutorials/tutorial-six-python.html
3) In order to request data from the micro-service, import client.py into your program and create an object of the RandomTextRPC class
4) Use the RandomTextRPC_object.request_text() to send a request to the random text generator
5) To receive the string of text, catch the return value of RandomTextRPC_object.request_text()

## UML Diagran:
![CS361_Microservice_UML](https://user-images.githubusercontent.com/72116228/180860038-607a406f-82a0-4748-9e39-23a3d364bb70.jpg)
