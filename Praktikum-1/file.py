import shapefile 
dzi = shapefile.Reader ("D:/materi kuliah/sistem informasi geografis/map/ne_10m_admin_0_countries.shp")
shapes = dzi.shapes()
print len(shapes) 