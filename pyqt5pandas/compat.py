
import logging
log = logging.getLogger(__name__)


try:
	import sip
	sip.setapi('QString', 2)
	sip.setapi('QVariant', 2)
	sip.setapi('QDate', 2)
	sip.setapi('QDateTime', 2)
	sip.setapi('QTextStream', 2)
	sip.setapi('QTime', 2)
	sip.setapi('QUrl', 2)
except ValueError as e:
	log.error(e)
except ImportError as e:
	log.error(e)

try:
	from PyQt5 import QtCore as QtCore_
	from PyQt5 import QtGui as QtGui_
	from PyQt5.QtCore import pyqtSlot as Slot, pyqtSignal as Signal
	from PyQt5 import QtWidgets as QtWidgets_
except ImportError as e:
	from PySide2 import QtCore as QtCore_
	from PySide2 import QtGui as QtGui_
	from PySide2.QtCore import Slot, Signal


QtCore = QtCore_
QtWidgets = QtWidgets_
QtGui = QtGui_
Qt = QtCore_.Qt

__all__ = ['QtCore', 'QtGui', 'Qt', 'QtWidget', 'Signal', 'Slot']
