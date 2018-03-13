from data_manager.datatypes.data import Data
from data_manager.datatypes.table import Table
from data_manager.datatypes.image import Image
from data_manager.datatypes.GFF3 import GFF3

datatype_map = {
    "text/csv": "Table",
    "image/tiff": "Image"
}