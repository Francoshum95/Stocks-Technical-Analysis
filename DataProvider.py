import requests
import os
import constant

class DataProvider:
  def __init__(self, ticker, provider):
    self.ticker = ticker
    self.provider = provider

  def getEndPoint(self):
    if self.provider == constant.TD:
      return "{}/{}/pricehistory".format(constant.TD_API_END_POINT, self.ticker)
    
  def getPayLoad(self):
    if self.provider == constant.TD:
      return {
        'apikey': os.getenv('TD_API_KEY') ,
        'periodType':'year',
        'frequencyType':'weekly',
        'frequency':'1',
        'period':'20',
        'needExtendedHoursData':'false'
        }

  def getRequest(self):
    endPoint = self.getEndPoint()
    payload = self.getPayLoad()

    return requests.get(url=endPoint, params=payload).json()
  
  def getPriceData(self):
    request = self.getRequest()

    if self.provider == constant.TD:
      return request['candles']
  


    


  