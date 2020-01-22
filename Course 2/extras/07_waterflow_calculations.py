import numpy as np
import datetime
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

startLine = 7

files = [ \
    ["Q3_MM2 Detectronic-P000008 - Q_Stromning.txt", "blue"], \
    ["Q6_MM3 Detectronic-P001500 - Q_Stromning.txt", "red"], \
    ["Q5_MM7 Detectronic-P001602 - Q_Stromning.txt", "cyan"], \
    ["Q8_MM6 Detectronic-P001502 - Q_Stromning.txt", "black"],
    ]

# Read file data and sanitize
def read_file_data(fileToRead):
    times = []
    values = []
    hasData = []
    i = 0
    check = ((6*60) / 3) # Corresponds to 6 hours time with 0 in every value
    numWithoutData = 0
    with open(fileToRead, "r") as file:
        for line in file:
            if i >= startLine:
                parts = line.split("\t")
                if(len(parts) != 2):
                    break
                time = parts[0]
                value = float(parts[1].strip("\n").replace(",","."))
                if(value == 0.0):
                    numWithoutData += 1
                else:
                    numWithoutData = 0
                times.append(datetime.datetime.strptime(time, "%Y-%m-%d %H:%M:%S"))
                values.append(value)
                if(numWithoutData > check): # Measured every 3 mins
                    hasData.append(0)
                else:
                    hasData.append(1)
            i += 1
    return times,values, hasData

fig,axes = plt.subplots(2, 1, sharex=True)

axes[0].xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
axes[0].xaxis.set_major_locator(mdates.MonthLocator())
axes[0].yaxis.set_major_locator(ticker.AutoLocator())
axes[0].set_ylabel("l/s")
axes[0].set_xlabel("Dato")

for f in files:
    times, values, hasData = read_file_data(f[0])
    dates = mdates.date2num(times)
    ax = axes[0].plot_date(dates, values, linestyle='solid', color=f[1], linewidth=0.3, marker='None')
    ax3 = axes[1].plot_date(dates, hasData, linestyle='solid', color=f[1], linewidth=0.3, marker='None')
    print("Read file " + f[0])

plt.gcf().autofmt_xdate()
plt.show()

