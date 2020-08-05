import RADWave as rwave
import matplotlib.pyplot as plt

#Loading NETCDF data file
wa = rwave.waveAnalysis(altimeterURL='IMOSURLs.txt', bbox=[152.0,155.0,-36.0,-34.0], 
                  stime=[1995,1,1], etime=[2020,1,1])

#Reading Processed AltimeterData.csv 
wa.readAltimeterData('altimeterData.csv')

#Creating time series (pandas DF)
timeseries = wa.generateTimeSeries()

#Plot the location of waves based with their energy level
fig, ax = plt.subplots()
sc = ax.scatter(timeseries.lon, timeseries.lat, c = timeseries.energy, alpha = 0.5)
ax.set_title('Location of Waves with their Energy', fontsize=18)
ax.set_xlabel('Longitude', fontsize=10)
ax.set_ylabel('Latitude', fontsize=10)
cbar = fig.colorbar(sc)
ax.grid()
fig.tight_layout()
plt.savefig('wave_location.png')

#plotting timeseries
#Significant wave height
wa.plotTimeSeries(series='H', fsize=(10, 5), fsave='Hseries')
#Wave power
wa.plotTimeSeries(time=[1995,2020], series='P', fsize=(10, 5), fsave='Pseries')
#Below are other plots that can be drawn but I am not using them for this project
#Wave period
#wa.plotTimeSeries(time=[1995,2020], series='T', fsize=(10, 5), fsave='Tseries')
#Wave energy
#wa.plotTimeSeries(time=[1995,2020], series='E', fsize=(10, 5), fsave='Eseries')
# Wave group velocity
#wa.plotTimeSeries(time=[1995,2020], series='Cg', fsize=(10, 5), fsave='Cgseries')