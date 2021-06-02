# require fake-useragent module

# Code is written and maintained by Arnav Mukhopadhyay
# * Do not misuse. Help this code to save live *
# * Get everyone vaccinated so that we can be have a COVID free World *
# * This code uses CoWin Open API and works when vaccinating in India *
# * Stay Safe and Get Vaccinated *


from fake_useragent import UserAgent

header = None

def getUA():
    global header

    if header is None:
        u = UserAgent()
        header = { "User-Agent" : u.random }

    return header
