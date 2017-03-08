import os

#rate_file = os.path.join(os.path.dirname(__file__), "exchange_rates.txt")

from decimal import *
getcontext().prec = 2

#def read_exchange_rates(exchange_file_name):
    #"""
    #Reads a file of exchange rates in file +exchange_file_name+ and returns
    #a mapping of the rates.
    #"""
    #pass
class Money(object):
    Conversion = {"ADF":5.8524,"ADP":148.448,"AED":3.6731,"AFN":64.31,"ALL":127.24,"AMD":473.2,"ANG":1.82,"AOA":135.976,"AON":135.976,"ARS":.4448,"ATS":12.2768,"AUD":1.419,"AWG":1.81,"AZM":3926,"AZN":1.0488,"BAM":1.7447,"BBD":2,"BDT":79.482,"BEF":35.9908,"BGN":1.7513,"BHD":0.3775,"BIF":1554,"BMD":"1","BND":1.4567,"BOB":7.0905,"BRL":3.9375,"BSD":1.006,"BTN":65.372,"BWP":10.726,"BYR":17781,"BZD":2.0401,"CAD":1.3155,"CDF":943,"CHF":0.9718,"CLP":689.6,"CNY":6.3661,"COP":3076,"CRC":547.57,"CUC":1,"CUP":23.1481,"CVE":98.65,"CYP":0.5222,"CZK":24.2419,"DEM":1.745,"DJF":177.72,"DKK":6.6557,"DOP":45.31,"DZD":106.36,"ECS":25587,"EEK":13.9597,"EGP":7.8576,"ESP":148.448,"ETB":21.151,"EUR":0.8922,"FIM":5.3047,"FJD":2.1668,"FKP":0.6589,"FRF":5.8524,"GBP":0.6593,"GEL":2.3954,"GHC":38200,"GHS":3.82,"GIP":0.6589,"GMD":39.59,"GNF":7700,"GRD":304.013,"GTQ":7.8839,"GYD":215.99,"HKD":7.7505,"HNL":22.262,"HRK":6.7997,"HTG":55.027,"HUF":278.678,"IDR":14792.9,"IEP":0.7027,"ILS":4.013,"INR":65.373,"IQD":1210,"IRR":30007,"ISK":127.8,"ITL":1727.52,"JMD":120.43,"JOD":0.7109,"JPY":119.99,"KES":104.35,"KGS":69.025,"KHR":4120,"KMF":439,"KPW":135,"KRW":1174.12,"KWD":0.3025,"KYD":0.8514,"KZT":274.27,"LAK":8175,"LBP":1513,"LKR":144.31,"LRD":89,"LSL":13.7433,"LTL":3.0805,"LUF":35.9908,"LVL":0.627,"LYD":1.39,"MAD":9.735,"MDL":20.385,"MGA":3295,"MGF":9150.46,"MKD":54.961,"MMK":1308.9,"MNT":1998,"MOP":8.1623,"MRO":310,"MTL":0.383,"MUR":36.95,"MVR":15.65,"MWK":560,"MXN":16.7647,"MYR":4.4675,"MZM":42300,"MZN":42.3,"NAD":13.7433,"NGN":199.1,"NIO":27.877,"NLG":1.9661,"NOK":8.4008,"NPR":106.29,"NZD":1.5538,"OMR":0.3861,"PAB":1,"PEN":3.2365,"PGK":2.9551,"PHP":46.727,"PKR":104.55,"PLN":3.7946,"PTE":178.868,"PYG":5707.5,"QAR":3.642,"ROL":39442,"RON":3.9442,"RSD":107.46,"RUB":66.122,"RWF":720,"SAR":3.7527,"SBD":8.1433,"SCR":13.805,"SDD":614.02,"SDG":6.1402,"SDP":2272.3,"SEK":8.3686,"SGD":1.4332,"SHP":0.6684,"SIT":213.804,"SKK":26.8781,"SLL":3795,"SOS":670,"SRD":3.3,"SRG":3300,"STD":22360,"SVC":8.9664,"SYP":220.55,"SZL":13.7433,"THB":36.562,"TJS":6.4729,"TMM":17587.5,"TMT":3.5175,"TND":1.968,"TOP":2.2835,"TRL":2993340,"TRY":2.9933,"TTD":6.4807,"TWD":32.731,"TZS":2214.9,"UAH":21.395,"UGX":3730.6,"USD":1,"UYU":29.668,"UZS":2635,"VEB":6310,"VEF":6.31,"VND":22840,"VUV":105.9,"WST":2.3602,"XAF":587.76,"XAG":0.06562,"XAU":0.0008786,"XCD":2.7169,"XEU":0.8922,"XOF":587.7,"XPD":0.001421,"XPF":106.75,"XPT":0.001094,"YER":215.5,"YUN":107.46,"ZAR":13.7433,"ZMK":5328.9,"ZMW":12.346,"ZWD":376.3}

# Above commands stores each value and the conversion as dictionary values in a class called conversion that will be called upon using Money.conversion

    def __init__(self,amount = '0', currency = 'USD'): #Initialize default values for the amount that is put in
        self.amount = round(amount,2)
        if currency in Money.Conversion:
            self.currency = currency
        else:
            print("Please enter a Valid Currency for Conversion! Thank you!") #If it's not one of the convertable currencies

    def to(self,currency):
        money = (self.amount/Money.Conversion[self.currency] * Money.Conversion[currency]) #simple algebra for conversion
        return Money(money, currency)

    def bills(self):
        billCounter = {}
        tempCurrency = self.to('USD')

        hundreds = int(tempCurrency.amount//100)
        hMod = int(tempCurrency.amount%100)

        fifties = hMod//50
        fMod = hMod%50

        twenties = fMod//20
        tMod = fMod%20

        tens = tMod//10
        tenMod = tMod%10

        fives = tenMod//5
        fiMod = tenMod%5

        ones = fiMod

        billCounter[100] = hundreds
        billCounter[50] = fifties
        billCounter[20] = twenties
        billCounter[10] = tens
        billCounter[5] = fives
        billCounter[1] = ones

        return (billCounter)

    def __str__(self):
        return str(self.currency + " " + format(self.amount, '.2f'))

    def __lt__(self,other):
        s = self.amount/Money.Conversion[self.currency]
        o = other.amount/Money.Conversion[other.currency]
        return s < o

    def __gt__(self,other):
        s = self.amount/Money.Conversion[self.currency]
        o = other.amount/Money.Conversion[other.currency]
        return s > o

    def __add__(self,other):
        o = (other.amount/Money.Conversion[other.currency] * (Money.Conversion[self.currency]))
        return Money(self.amount+o,self.currency)

    def __eq__(self,other):
        s = self.amount/Money.Conversion[self.currency]
        o = other.amount/Money.Conversion[other.currency]
        return s==o

    def __ne__(self,other):
        s = self.amount/Money.Conversion[self.currency]
        o = other.amount/Money.Conversion[other.currency]
        return s!=o

    def __radd__(self,other):
        if other ==0:
            return self
        else:
            return self.__add__(other)





