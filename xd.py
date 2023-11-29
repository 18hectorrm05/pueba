gpkg_layer = QgsVectorLayer(r"C:\Users\20180234\Desktop\site\conjunto_de_datos", "banco_nivel_p", "ogr")
QgsProject.instance().addMapLayer(gpkg_layer)