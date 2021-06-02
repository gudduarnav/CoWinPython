# require fake-useragent module

from fake_useragent import UserAgent

header = None

def getUA():
    global header

    if header is None:
        u = UserAgent()
        header = { "User-Agent" : u.random }

    return header
