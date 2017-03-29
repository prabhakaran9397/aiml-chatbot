import aiml
bot = aiml.Kernel()  
bot.learn("aiml/*.aiml")

def response(sentence):
    return bot.respond(sentence)

if __name__ == '__main__':
    request = raw_input('> ')
    while request:
        print 'Bot: ' + response(request)
        request = raw_input('> ')