#Seasonal and annual plots
trends:	IMOSURLs.txt altimeterData.cs
	python plot_trends.py

#Timeseries plots
timeseries:	IMOSURLs.txt altimeterData.csv
	python plot_timeseries.py

#altimeter data locations
altimeterData:		IMOSURLs.txt altimeterData.csv
	python altimeter_geo.py

.PHONY: clean almost_clean

clean:	almost_clean
	rm *.png
	rm .csv
	
almost_clean:
	latexmk -c
