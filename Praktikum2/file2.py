import shapefile 
sf = shapefile.Reader ("D:/praktikum2/countries.shp")
shapes = sf.shapes()
print len(shapes) 