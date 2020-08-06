#Creating report.pdf
report:	report.tex altimeterdata.png Hseries.png Pseries.png whall_wh_heatmap.png whall_wh_distribution.png wave_location.png annual_value.png
	latexmk -pdf $<

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
	rm report.pdf

almost_clean:
	latexmk -c
