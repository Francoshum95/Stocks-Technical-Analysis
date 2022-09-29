import datetime 
import pandas as pd
import statistics
from DataProvider import DataProvider
import constant

class TDStatistics:
  def __init__(self, ticker):
    self.histoicalPrices = DataProvider(ticker, constant.TD).getPriceData()
    self.closePrice = self.getClosePrice()
  
  def getDate(self):
    date = []

    for i in self.histoicalPrices:
      timeStamp = i['datetime']
      dateTime = datetime.datetime.fromtimestamp( int(timeStamp) / 1000)

      date.append(dateTime)
    
    return date

  def getClosePrice(self):
    closePrice = []

    for i in self.histoicalPrices:
      closePrice.append(i['close'])
    
    return closePrice
  
  def getEMA(self, day):
    closePrice = self.closePrice

    df = pd.DataFrame(closePrice)
    list_exponential_moving_average = df.ewm(day).mean()
    return list_exponential_moving_average[0].tolist()
  
  def getMovingAvaerageDistance(self, day):
    emaData = self.getEMA(day)
    closePrices = self.closePrice

    distanceEMA = []

    for i in range(len(closePrices)):
      if emaData[i] == 'nan':
        pass
      else:
        mathEMA = (closePrices[i] - emaData[i]) /closePrices[i]
        distanceEMA.append(mathEMA)
    
    return distanceEMA

  def getChartDataFrame(self, day):
    dateData = self.getDate()
    distance = self.getMovingAvaerageDistance(day)

    mean = statistics.mean(distance)
    sd = statistics.stdev(distance)

    sdPlusOne = [mean + 1 * sd] * len(dateData)
    sdPlusTwo = [mean + 2 * sd] * len(dateData)
    sdMinusOne = [mean - 1 * sd] * len(dateData)
    sdMinusTwo = [mean - 2 * sd] * len(dateData)
    average = [mean] * len(dateData)

    return {
      'date': dateData,
      'value': distance,
      '-2SD': sdMinusTwo,
      '-1SD': sdMinusOne,
      '+2SD': sdPlusTwo,
      '+1SD': sdPlusOne,
      'avg': average
    }



      




    











