import RADWave as rwave

#loading NETCDF data file
wa = rwave.waveAnalysis(altimeterURL='IMOSURLs.txt', bbox=[152.0,155.0,-36.0,-34.0], 
                  stime=[1995,1,1], etime=[2020,1,1])

#Reading Processed AltimeterData.csv 
wa.readAltimeterData('altimeterData.csv')

#visualising altimeterData on the map
wa.visualiseData(title="Altimeter data tracks", extent=[149.,158.,-38.,-32.], 
                 addcity=['Sydney', 151.2093, -33.8688], markersize=40, zoom=8,
                 fsize=(5, 5), fsave='altimeterdata')

#Creating time series (pandas DF)
timeseries = wa.generateTimeSeries()