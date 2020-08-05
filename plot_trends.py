import RADWave as rwave
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from matplotlib.transforms import offset_copy
from mpl_toolkits.axes_grid1 import make_axes_locatable
from pandas.plotting import register_matplotlib_converters

#Loading NETCDF data file
wa = rwave.waveAnalysis(altimeterURL='IMOSURLs.txt', bbox=[152.0,155.0,-36.0,-34.0], 
                  stime=[1995,1,1], etime=[2020,1,1])

#Reading Processed AltimeterData.csv 
wa.readAltimeterData('altimeterData.csv')

#Creating time series (pandas DF)
timeseries = wa.generateTimeSeries()

#Creating seasonal charactristics
wh_all = wa.computeSeasonalCharacteristics(series='wh', time=[1995,2020], lonlat=None, fsave='whall', plot=True)

# First we create a dictionary of 1 by 1 degree tiles within our regional area of interest(these locations are for my dataset)
tiles = []
tiles.append([152.0,153.0,-36.0,-35.0])
tiles.append([153.0,154.0,-36.0,-35.0])
tiles.append([152.0,153.0,-35.0,-34.0])
tiles.append([153.0,154.0,-35.0,-34.0])

# We also store the geographical locations of the center of each tile (these locations are for my dataset)
lonlat = []
lonlat.append([152.5,-35.5])
lonlat.append([153.5,-35.5])
lonlat.append([152.5,-34.5])
lonlat.append([153.5,-34.5])

# And we define a new dictionary that will be filled with regional wave seasonability
seasons = []

# Finally we loop over the defined tiles and perform seasonability analysis for significant wave height
for k in range(4):
    seasons.append(wa.computeSeasonalCharacteristics(series='wh', time=[1995,2020], 
                                        lonlat=tiles[k], plot=False))

#Plot annual values for each tile based on the seasons dictionary that we built above
register_matplotlib_converters()

plt.rcParams['mathtext.fontset'] = 'cm'

fig, ax = plt.subplots(figsize = (8,4))

for k in range(4):
    yearwh = seasons[k]['mean']
    yearwh.plot(marker='o', linestyle='dashed', linewidth=2, markersize=8)
    
ax.set_title('Annual mean values of significant wave height for each tile',fontsize = 12)
ax.set_ylabel("Hs (m)",fontsize = 12)
ax.set_xlabel('Years',fontsize = 11)
ax.legend([lonlat[0],lonlat[1],lonlat[2],lonlat[3]])
ax.yaxis.set_tick_params(labelsize=10)
ax.xaxis.set_tick_params(labelsize=10, rotation=45)
plt.tight_layout()
plt.savefig('annual_value.png')
plt.show()