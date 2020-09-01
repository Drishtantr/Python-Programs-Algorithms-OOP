from nepal_forex.nepal_forex import nepal_forex

def hello_world():
    def conversion(cur):
        return(nepal_forex.exchange_rate(currency=cur))
    USD=conversion("USD")
    return USD

print(hello_world())