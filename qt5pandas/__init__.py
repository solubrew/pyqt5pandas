# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
from qt5pandas.models.DataFrameModel import DataFrameModel, read_file, read_sql

from qt5pandas.models.ColumnDtypeModel import ColumnDtypeModel
from qt5pandas.models.DataSearch import DataSearch
from qt5pandas.views.CSVDialogs import CSVExportDialog, CSVImportDialog
from qt5pandas.views.EditDialogs import AddAttributesDialog, RemoveAttributesDialog
# __import__('pkg_resources').declare_namespace(__name__)
__version__ = '0.0.1'

