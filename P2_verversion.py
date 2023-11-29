#Imprimir nombre y version de Qgis3.8
from qgis.core import Qgis
print("El nombre y version de su QGIS es: ")
print(Qgis.QGIS_RELEASE_NAME, Qgis.QGIS_VERSION_INT)
