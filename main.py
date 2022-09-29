import sys
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import rcParams
from Statistics import TDStatistics 

rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Tahoma']

class Main:
  def __init__(self, ticker, day):
    self.ticker = ticker
    self.day = day
  
  def plotChart(self):
    data = TDStatistics(self.ticker).getChartDataFrame(self.day)

    date = data['date']
    value = data['value']
    mean = data['avg']
    min2sd = data['-2SD']
    min1sd = data['-1SD']
    plus2sd = data['+2SD']
    plus1sd = data['+1SD']

    fig, ax1 = plt.subplots(figsize=(5.9, 3.6), tight_layout=True)

    plt.title('{} {} Days EMA Distance'.format(self.ticker, self.day), fontsize=9)

    ax1.plot_date(date, value, '-',  color = 'darkblue', linewidth=1)
    ax1.plot_date(date, mean, '--', label= ' Avg', color = 'darkblue',linewidth=1)
    ax1.plot_date(date, min2sd, ':', label= '-2SD', color = 'darkblue', linewidth=1)
    ax1.plot_date(date, min1sd, ':', label= '-1SD', color = 'darkblue', linewidth=1)
    ax1.plot_date(date, plus2sd, ':', label= '+2SD', color = 'darkblue', linewidth=1)
    ax1.plot_date(date, plus1sd, ':', label= '+1SD', color = 'darkblue', linewidth=1)
    
    last_value = str("{:.2f}".format(value[-1]))

    ax1.annotate(last_value, (date[-1], value[-1]), xytext = (date[-1], value[-1]), fontsize=8)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    plt.rcParams['font.size'] = '7'

    plt.xticks(fontsize=6)
    plt.yticks(fontsize=6)
    plt.margins(x=0)

    right_side = ax1.spines["right"]
    top_side = ax1.spines["top"]

    right_side.set_visible(False)
    top_side.set_visible(False)

    plt.legend(loc='upper center',  bbox_to_anchor=(0.5,-0.1), fancybox=True, ncol=5, fontsize=7)
    plt.show()


if __name__ == "__main__":
  Main().plotChart(sys.argv[1], sys.argv[2])




