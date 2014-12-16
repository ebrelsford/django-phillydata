download_water_parcels:
	mkdir -p raw/water_parcels
	mkdir -p processed/water_parcels
	curl -L "http://gis.phila.gov/gisdata/PARCELS_PWD.zip" -o raw/water_parcels/water_parcels.zip
	unzip raw/water_parcels/water_parcels.zip -d raw/water_parcels/
	ogr2ogr -simplify 0.2 -t_srs EPSG:4326 -overwrite processed/water_parcels/water_parcels.shp raw/water_parcels/PARCELS_PWD.shp
