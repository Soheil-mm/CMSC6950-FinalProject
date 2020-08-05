import RADWave as rwave

#loading NETCDF data file
wa = rwave.waveAnalysis(altimeterURL='IMOSURLs.txt', bbox=[152.0,155.0,-36.0,-34.0], 
                  stime=[1995,1,1], etime=[2020,1,1])

#Reading Processed AltimeterData.csv 
wa.readAltimeterData(saveCSV = 'altimeterData.csv')

#Creating time series (pandas DF)
timeseries = wa.generateTimeSeries()