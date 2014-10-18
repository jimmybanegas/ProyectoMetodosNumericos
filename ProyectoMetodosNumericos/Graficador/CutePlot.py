"""
CutePlot is a platform-independent plotting program for 2-D mathematical functions.
Includes a feature for visualizing positive and negative log-axes together.

Jack Peterson (jack@tinybike.net)
License: GPL
Last modified: 11/14/2012 (v. 0.11)
"""

from __future__ import division	# Int-to-float division auto-convert from Python 3
import sys
from math import *
from PySide.QtGui import *
from PySide.QtCore import *

# Import matplotlib backend, specify PySide
import matplotlib
matplotlib.use('Qt4Agg')
matplotlib.rcParams['backend.qt4'] = 'PySide'
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar
from matplotlib.figure import Figure

class CutePlot(QMainWindow):
    
	def __init__(self, parent=None):
		super(CutePlot, self).__init__(parent)
		
		# Default values for lower and upper bound
		self.LB_default = -10
		self.UB_default = 10
		
		# Create main plot area + menus + status bar		
		self.create_main_frame()
		self.textbox.setText('')
		self.LB_UB_defaults()
		self.on_draw()
	
		self.statusBar()
		self.setWindowTitle('CutePlot')
		self.create_menu()

	def LB_UB_defaults(self):
		# Set default values for lower bound and upper bound
		self.lowerbound.setText(str(self.LB_default))
		self.upperbound.setText(str(self.UB_default))
		
	def create_main_frame(self):
		self.main_frame = QWidget()
		
		# 7x5 inches, 80 dots-per-inch
		self.dpi = 80
		self.fig = Figure((7, 5), dpi = self.dpi)
		self.canvas = FigureCanvas(self.fig)
		self.canvas.setParent(self.main_frame)
		self.is_data = False
		
		self.axes = self.fig.add_subplot(111)
		
		# axis_state keeps track of how many subplots are present
		# axis_state = 0: main plot only
		# axis_state = 1: horizontal split (quadrants 1 and 2)
		# axis_state = 2: vertical split (quadrants 1 and 4)
		# axis_state = 3: show all 4 subplots
		self.axis_state = 0
		
		self.mpl_toolbar = NavigationToolbar(self.canvas, self.main_frame)
		
		# f(x) textbox
		self.title = QLabel('<font size=4><em>f</em> (<em>x </em>) =</font>')
		self.textbox = QLineEdit()
		self.textbox.setMinimumWidth(200)
		self.connect(self.textbox, SIGNAL('returnPressed()'), self.on_draw)
		
		# Lowerbound and upperbound textboxes
		self.LB_title = QLabel('<font size=4>Min:</font>')
		self.lowerbound = QLineEdit()
		self.lowerbound.setMaximumWidth(30)
		self.connect(self.lowerbound, SIGNAL('returnPressed()'), self.on_draw)
		
		self.UB_title = QLabel('<font size=4>Max:</font>')
		self.upperbound = QLineEdit()
		self.upperbound.setMaximumWidth(30)
		self.connect(self.upperbound, SIGNAL('returnPressed()'), self.on_draw)
		
		# Plot button
		self.draw_button = QPushButton("&Plot")
		self.connect(self.draw_button, SIGNAL('clicked()'), self.on_draw)

		# Hold checkbox
		self.hold_cb = QCheckBox("&Hold")
		self.hold_cb.setChecked(False)
		self.connect(self.hold_cb, SIGNAL('stateChanged(int)'), self.on_minor_change)
		self.hold_cb.setToolTip('Prevent new plots from replacing old ones')
		self.hold_cb.setStatusTip('Prevent new plots from replacing old ones')
		
		# Log-x and log-y checkboxes
		self.logx_cb = QCheckBox("Log-&x")
		self.logx_cb.setChecked(False)
		self.connect(self.logx_cb, SIGNAL('stateChanged(int)'), self.on_draw)
		self.logx_cb.setToolTip('Change x-axis to logarithmic scale')
		self.logx_cb.setStatusTip('Change x-axis to logarithmic scale')
		
		self.logy_cb = QCheckBox("Log-&y")
		self.logy_cb.setChecked(False)
		self.connect(self.logy_cb, SIGNAL('stateChanged(int)'), self.on_draw)
		self.logy_cb.setToolTip('Change y-axis to logarithmic scale')
		self.logy_cb.setStatusTip('Change y-axis to logarithmic scale')
		
		# Truncated-log checkbox
		self.trunc_cb = QCheckBox("Show &Negative")
		self.trunc_cb.setChecked(False)
		self.connect(self.trunc_cb, SIGNAL('stateChanged(int)'), self.on_draw)
		self.trunc_cb.setToolTip('Plot negative values of log-transformed functions')
		self.trunc_cb.setStatusTip('Plot negative values of log-transformed functions')
		
		# Grid checkbox
		self.grid_cb = QCheckBox("&Grid")
		self.grid_cb.setChecked(False)
		self.connect(self.grid_cb, SIGNAL('stateChanged(int)'), self.on_minor_change)
		self.grid_cb.setToolTip('Show grid')
		self.grid_cb.setStatusTip('Show grid')
		
		# Grid layout
		grid = QGridLayout()
		grid.setSpacing(10)
		
		gridCol = 0
		for w in [self.title, self.textbox, self.LB_title, self.lowerbound, self.UB_title, 
					self.upperbound, self.draw_button]:
			grid.addWidget(w, 0, gridCol)
			gridCol += 1
		
		grid2 = QGridLayout()
		grid2.setSpacing(10)
		gridCol = 0
		for w in [self.logx_cb, self.logy_cb, self.trunc_cb, self.hold_cb, self.grid_cb]:
			grid2.addWidget(w, 0, gridCol)
			gridCol += 1
		
		vbox = QVBoxLayout()
		vbox.addLayout(grid)
		vbox.addLayout(grid2)
		vbox.addWidget(self.canvas)
		vbox.addWidget(self.mpl_toolbar)
					
		self.main_frame.setLayout(vbox)
		self.setCentralWidget(self.main_frame)
	
	def on_minor_change(self):
		self.on_draw(self.is_data)
	
	def on_draw(self, *args):
		# Get x-domain from user input
		self.LB_input = unicode(self.lowerbound.text())
		self.UB_input = unicode(self.upperbound.text())
		
		# Message box error if the domain inputs aren't int or float types
		# If float, round to the nearest 0.1
		round_to = 10
		try:
			self.LB_float = int(self.LB_input)*round_to
			self.UB_float = int(self.UB_input)*round_to
		except:
			self.LB_UB_defaults()
			QMessageBox.question(self, 'Error',
				'<center>Minimum and maximum values must be<br />\
				integer or floating-point numbers.</center>', QMessageBox.Ok)
		
		# Make sure UB > LB
		if self.UB_float <= self.LB_float:
			self.LB_UB_defaults()
			QMessageBox.question(self, 'Error',
				'<center>Maximum must be greater\
				than minimum value.</center>', QMessageBox.Ok)
		
		# If plotting a function, then get x and y values
		if len(args) == 0:
			self.is_data = False
		
			# Set x values (/round_to is to use range() with floating-point numbers)
			self.input_x = range(self.LB_float, self.UB_float + 1)
			self.input_x = [i/float(round_to) for i in self.input_x]
			
			# Calculate f(x) values for specified function
			fx = unicode(self.textbox.text())
			# If the f(x) field is empty, then default to y = 0 plot
			if fx == '':
				self.y = [0 for i in self.input_x]
			# Otherwise, evaluate the specified function and get ready to plot
			else:
				# Replace exp with numbers
				fx = fx.replace('exp', str(exp(1)) + '**')
				# Allow users to enter ^ for powers (replace ^ with **)
				fx = fx.replace('^', '**')
				# Try and evaluate; if there is an error, then shift slightly to the right
				try:
					self.y = [eval(fx) for x in self.input_x]
				except:
					fx = fx.replace('x', '(x + 10**(-6))')
					self.y = [eval(fx) for x in self.input_x]		
			self.plot_symbol = '-'
			
		if self.is_data:
			self.plot_symbol = 'o'
		
		# If the hold box is checked, then new plots do not erase old ones
		new_state = self.quad_check()
		if self.axis_state == 0:
			self.axes.hold(self.hold_cb.isChecked())
		else:
			if self.hold_cb.isChecked():
				# If 'hold' is checked, see what quadrants will be shown
				# - if the quadrant state changes, remove subplots
				# - otherwise retain subplots
				if self.axis_state == 0 and new_state == 0:
					self.axes.hold(self.hold_cb.isChecked())
				elif self.axis_state == 3 and new_state == 3:
					self.axes_Q1.hold(self.hold_cb.isChecked())
					self.axes_Q2.hold(self.hold_cb.isChecked())
					self.axes_Q3.hold(self.hold_cb.isChecked())
					self.axes_Q4.hold(self.hold_cb.isChecked())
				elif self.axis_state == 1 and new_state == 1:
					self.axes_Q1.hold(self.hold_cb.isChecked())
					self.axes_Q2.hold(self.hold_cb.isChecked())
				elif self.axis_state == 2 and new_state == 2:
					self.axes_Q1.hold(self.hold_cb.isChecked())
					self.axes_Q4.hold(self.hold_cb.isChecked())
				else:
					self.remove_subplots()
			else:
				self.remove_subplots()
		
		# If show negative box is unchecked
		if not self.trunc_cb.isChecked():
			self.add_main()
			self.axes.plot(self.input_x, self.y, self.plot_symbol)
			if not self.logx_cb.isChecked() and not self.logy_cb.isChecked():
				self.axes.set_xscale('linear')
				self.axes.set_yscale('linear')
			elif self.logx_cb.isChecked() and not self.logy_cb.isChecked():
				self.axes.set_xscale('log')
				self.axes.set_yscale('linear')
			elif not self.logx_cb.isChecked() and self.logy_cb.isChecked():
				self.axes.set_xscale('linear')
				self.axes.set_yscale('log')
			else:
				self.axes.set_xscale('log')
				self.axes.set_yscale('log')
		else:
			# Linear plot
			#if not self.logx_cb.isChecked() and not self.logy_cb.isChecked():
			if new_state == 0:
				self.add_main()
				self.axes.plot(self.input_x,self.y,self.plot_symbol)
				
			# Log x, linear y plot
			#elif self.logx_cb.isChecked() and not self.logy_cb.isChecked():
			elif new_state == 1:
				if not self.trunc_cb.isChecked():
					self.add_main()
					self.axes.semilogx(self.input_x,self.y,self.plot_symbol)
				else:
					self.trunc_logx()
					
			# Linear x, log y plot
			#elif not self.logx_cb.isChecked() and self.logy_cb.isChecked():
			elif new_state == 2:
				if not self.trunc_cb.isChecked():
					self.add_main()
					self.axes.semilogy(self.input_x,self.y,self.plot_symbol)
				else:
					self.trunc_logy()
					
			# Log-log plot
			else:
				if not self.trunc_cb.isChecked():
					self.add_main()
					self.axes.loglog(self.input_x,self.y,self.plot_symbol)
				else:
					self.trunc_loglog()
		
		# Add grid if grid checkbox is checked
		if self.axis_state == 0:
			self.axes.grid(self.grid_cb.isChecked())
		else:
			if hasattr(self, 'axes_Q1'):
				self.axes_Q1.grid(self.grid_cb.isChecked())
			if hasattr(self, 'axes_Q2'):
				self.axes_Q2.grid(self.grid_cb.isChecked())
			if hasattr(self, 'axes_Q3'):
				self.axes_Q3.grid(self.grid_cb.isChecked())
			if hasattr(self, 'axes_Q4'):
				self.axes_Q4.grid(self.grid_cb.isChecked())
		
		self.axes.set_xlabel('$x$')
		self.axes.set_ylabel('$f(x)$')
		
		self.canvas.draw()
		
	def remove_subplots(self):
		# Remove all subplots and axis flip flags
		if hasattr(self, 'axes_Q1'):
			self.fig.delaxes(self.axes_Q1)
			del self.axes_Q1
		if hasattr(self, 'axes_Q2'):
			self.fig.delaxes(self.axes_Q2)
			del self.axes_Q2
			if hasattr(self, 'flip_Q2'):
				del self.flip_Q2
		if hasattr(self, 'axes_Q3'):
			self.fig.delaxes(self.axes_Q3)
			del self.axes_Q3
			del self.flip_Q3
		if hasattr(self, 'axes_Q4'):
			self.fig.delaxes(self.axes_Q4)
			del self.axes_Q4
			if hasattr(self, 'flip_Q4'):
				del self.flip_Q4
	
	def add_main(self):
		# Reinsert the main plot
		if self.axis_state > 0:
			self.remove_subplots()
			self.axes = self.fig.add_subplot(111)
			self.axis_state = 0
			
	def create_menu(self):
		exitAction = QAction('Quit', self)
		exitAction.setShortcut('Ctrl+Q')
		exitAction.setStatusTip('Exit application')
		exitAction.triggered.connect(self.close)
		
		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&File')
		
		save_plot_action = self.create_action("&Save plot",
            shortcut = "Ctrl+S", slot = self.save_plot, 
            tip = "Save image to file")
		import_data_action = self.create_action("&Import data",
			shortcut = "Ctrl+I", slot = self.import_data,
			tip = "Import data from file")
		fileMenu.addAction(save_plot_action)
		fileMenu.addAction(import_data_action)
		fileMenu.addAction(exitAction)
		
		helpMenu = self.menuBar().addMenu("&Help")
		about_action = self.create_action("&About", 
			shortcut = 'F1', slot = self.on_about, 
			tip = 'About CutePlot')
		helpMenu.addAction(about_action)

	def create_action(self, text, slot = None, shortcut = None, 
						icon = None, tip = None, checkable = False, 
						signal = "triggered()"):
		action = QAction(text, self)
		if icon is not None:
			action.setIcon(QIcon(":/%s.png" % icon))
		if shortcut is not None:
			action.setShortcut(shortcut)
		if tip is not None:
			action.setToolTip(tip)
			action.setStatusTip(tip)
		if slot is not None:
			self.connect(action, SIGNAL(signal), slot)
		if checkable:
			action.setCheckable(True)
		return action
		
	def save_plot(self):
		file_choices = "PNG (*.png)"
		path = unicode(QFileDialog.getSaveFileName(self, 'Save file', '', file_choices))
		if path:
			self.canvas.print_figure(path, dpi = self.dpi)
			self.statusBar().showMessage('Saved to %s' % path, 2000)
	
	def import_data(self):
		file_choices = "*.csv;;*.txt;;*.tab;;*.dat;;*.*"
		self.path = QFileDialog.getOpenFileName(self, 'Import data', '', file_choices)
		if self.path:
			datafile = open(self.path[0], 'r')
			if datafile:
				self.is_data = True
				delimiter = ','
				input_xy = [map(float, line.strip().split(delimiter)) for line in datafile]
				self.input_x, self.y = [[row[col] for row in input_xy] for col in [0, 1]]
				datafile.close()
				self.statusBar().showMessage('Imported data', 2000)
				self.on_draw(self.is_data)
				
	def on_about(self):
		msg = """<center><b>CutePlot v. 0.1</b></center>
		<center>Free, open-source plotting program,<br />
		written in Python (PySide/Qt + matplotlib).</center>
		<center>(c) Jack Peterson, 2012</center>
		"""
		QMessageBox.about(self, "About", msg.strip())
		
	def quad_check(self):
		# Q = quadrant
		Q1 = False
		Q2 = False
		Q3 = False
		Q4 = False
		
		# Split the x and y values by sign
		for j in range(0, len(self.input_x)):
			if self.input_x[j] > 0 and self.y[j] > 0:
				Q1 = True
			elif self.input_x[j] < 0 and self.y[j] > 0:
				Q2 = True
			elif self.input_x[j] < 0 and self.y[j] < 0:
				Q3 = True
			elif self.input_x[j] > 0 and self.y[j] < 0:
				Q4 = True
		
		if (Q3 or (Q2 and Q4) or ((Q2 or Q4) and self.axis_state == 3)) and self.logx_cb.isChecked() and self.logy_cb.isChecked():
			new_state = 3
		elif (Q2 and self.logx_cb.isChecked()) or (self.hold_cb.isChecked() and self.axis_state == 1):
			new_state = 1
		elif (Q4 and self.logy_cb.isChecked()) or (self.hold_cb.isChecked() and self.axis_state == 2):
			new_state = 2
		else:
			new_state = 0
		
		return new_state
		
	def trunc_logx(self):
		# Q = quadrant
		Q1_x = []
		Q1_y = []
		Q2_x = []
		Q2_y = []
		
		# Split the x and y values by sign
		for j in range(0, len(self.input_x)):
			if self.input_x[j] > 0 and self.y[j] > 0:
				Q1_x.append(self.input_x[j])
				Q1_y.append(self.y[j])
			elif self.input_x[j] < 0 and self.y[j] > 0:
				Q2_x.append(-self.input_x[j])
				Q2_y.append(self.y[j])
		
		# If only Q1 is populated, then use an ordinary semilogx plot
		if Q2_x == [] and not self.hold_cb.isChecked():
			self.add_main()
			self.axes.semilogx(self.input_x, self.y, self.plot_symbol)
		
		# Otherwise, create a truncated plot
		else:
			# Remove main axes
			if self.axis_state == 0:
				self.fig.delaxes(self.axes)
			
			if self.axis_state == 2 or self.axis_state == 3:
				self.axis_state = 3
			else:
				self.axis_state = 1
			
			# Create 2 subplots
			self.axes_Q1 = self.fig.add_subplot(122)
			self.axes_Q2 = self.fig.add_subplot(121)
			self.axes_Q1.autoscale(enable = True)
			self.axes_Q2.autoscale(enable = True)
			self.axes_Q1.semilogx(Q1_x, Q1_y, self.plot_symbol)
			self.axes_Q2.semilogx(Q2_x, Q2_y, self.plot_symbol)
								
			# Reverse Q2 x-axis
			if not hasattr(self, 'flip_Q2'):
				self.flip_Q2 = True
				self.axes_Q2.set_xlim(self.axes_Q2.get_xlim()[::-1])
			
			# Set axis tickmarks at powers of 10
			# Q1 axes
			if Q1_x == [] and not self.hold_cb.isChecked():
				self.axes_Q1.set_xticklabels([])
			else:
				try:
					x_UB_Q1 = int(ceil(log10(max(Q1_x))))
					x_LB_Q1 = int(floor(log10(min(Q1_x))))
				except:
					x_UB_Q1 = 2
					x_LB_Q1 = -1
				Q1_xlabels = []
				for i in range(x_LB_Q1, x_UB_Q1 + 1):
					Q1_xlabels.append('$10^{%s}$' % str(i))
				self.axes_Q1.set_xticklabels(Q1_xlabels)
			self.axes_Q1.xaxis.tick_bottom()
			self.axes_Q1.yaxis.tick_right()
			
			# Q2 axes
			if Q2_x == [] and not self.hold_cb.isChecked():
				self.axes_Q2.set_xticklabels([])
			else:
				try:
					x_UB_Q2 = int(ceil(log10(max(Q2_x))))
					x_LB_Q2 = int(floor(log10(min(Q2_x))))
				except:
					x_UB_Q2 = 2
					x_LB_Q2 = -1
				Q2_xlabels = []
				for i in range(x_LB_Q2, x_UB_Q2 + 1):
					Q2_xlabels.append('$-10^{%s}$' % str(i))
				self.axes_Q2.set_xticklabels(Q2_xlabels)
			self.axes_Q2.xaxis.tick_bottom()
			self.axes_Q2.yaxis.tick_left()
	
	def trunc_logy(self):
		# Q = quadrant
		Q1_x = []
		Q1_y = []
		Q4_x = []
		Q4_y = []
		
		# Split the x and y values by sign
		for j in range(0, len(self.input_x)):
			if self.input_x[j] > 0 and self.y[j] > 0:
				Q1_x.append(self.input_x[j])
				Q1_y.append(self.y[j])
			elif self.input_x[j] > 0 and self.y[j] < 0:
				Q4_x.append(self.input_x[j])
				Q4_y.append(-self.y[j])
		
		# If only Q1 is populated, then use an ordinary semilogy plot
		if Q4_x == [] and not self.hold_cb.isChecked():
			self.add_main()
			self.axes.semilogy(self.input_x, self.y, self.plot_symbol)
		
		# Otherwise, create a truncated plot
		else:
			# Remove main axes
			if self.axis_state == 0:
				self.fig.delaxes(self.axes)
				
			if self.axis_state == 1 or self.axis_state == 3:
				self.axis_state = 3
			else:
				self.axis_state = 2
			
			# Create 2 subplots
			self.axes_Q1 = self.fig.add_subplot(211)
			self.axes_Q4 = self.fig.add_subplot(212)
			self.axes_Q1.autoscale(enable = True)
			self.axes_Q4.autoscale(enable = True)
			self.axes_Q1.semilogy(Q1_x, Q1_y, self.plot_symbol)
			self.axes_Q4.semilogy(Q4_x, Q4_y, self.plot_symbol)
								
			# Reverse Q4 y-axis
			if not hasattr(self, 'flip_Q4'):
				self.flip_Q4 = True
				self.axes_Q4.set_ylim(self.axes_Q4.get_ylim()[::-1])
			
			# Set axis tickmarks at powers of 10
			# Q1 axes
			if Q1_x == [] and not self.hold_cb.isChecked():
				self.axes_Q1.set_yticklabels([])
			else:
				try:
					y_UB_Q1 = int(ceil(log10(max(Q1_y))))
					y_LB_Q1 = int(floor(log10(min(Q1_y))))
				except:
					y_UB_Q1 = 2
					y_LB_Q1 = -1
				Q1_ylabels = []
				for i in range(y_LB_Q1, y_UB_Q1 + 1):
					Q1_ylabels.append('$10^{%s}$' % str(i))
				self.axes_Q1.set_yticklabels(Q1_ylabels)
			self.axes_Q1.xaxis.tick_top()
			self.axes_Q1.yaxis.tick_right()
			
			# Q4 axes
			if Q4_x == [] and not self.hold_cb.isChecked():
				self.axes_Q4.set_yticklabels([])
			else:
				try:
					y_UB_Q4 = int(ceil(log10(max(Q4_y))))
					y_LB_Q4 = int(floor(log10(min(Q4_y))))
				except:
					y_UB_Q4 = 2
					y_LB_Q4 = -1
				Q4_ylabels = []
				for i in range(y_LB_Q4, y_UB_Q4 + 1):
					Q4_ylabels.append('$-10^{%s}$' % str(i))
				self.axes_Q4.set_yticklabels(Q4_ylabels)
			self.axes_Q4.xaxis.tick_bottom()
			self.axes_Q4.yaxis.tick_right()
		
	def trunc_loglog(self):
		# Q = quadrant
		Q1_x = []
		Q1_y = []
		Q2_x = []
		Q2_y = []
		Q3_x = []
		Q3_y = []
		Q4_x = []
		Q4_y = []
		
		# Split the x and y values by sign
		for j in range(0, len(self.input_x)):
			if self.input_x[j] > 0 and self.y[j] > 0:
				Q1_x.append(self.input_x[j])
				Q1_y.append(self.y[j])
			elif self.input_x[j] < 0 and self.y[j] > 0:
				Q2_x.append(-self.input_x[j])
				Q2_y.append(self.y[j])
			elif self.input_x[j] < 0 and self.y[j] < 0:
				Q3_x.append(-self.input_x[j])
				Q3_y.append(-self.y[j])
			elif self.input_x[j] > 0 and self.y[j] < 0:
				Q4_x.append(self.input_x[j])
				Q4_y.append(-self.y[j])
		
		# If only Q1 is populated, then use an ordinary loglog plot
		if Q2_x == [] and Q3_x == [] and Q4_x == [] and not self.hold_cb.isChecked():
			self.add_main()
			self.axes.loglog(self.input_x, self.y, self.plot_symbol)
		
		# Otherwise, create a truncated plot
		else:
			# Remove main axes
			if self.axis_state == 0:
				self.fig.delaxes(self.axes)
			self.axis_state = 3
			
			# Create 4 subplots
			self.axes_Q1 = self.fig.add_subplot(222)
			self.axes_Q2 = self.fig.add_subplot(221)
			self.axes_Q3 = self.fig.add_subplot(223)
			self.axes_Q4 = self.fig.add_subplot(224)
			self.axes_Q1.autoscale(enable = True)
			self.axes_Q2.autoscale(enable = True)
			self.axes_Q3.autoscale(enable = True)
			self.axes_Q4.autoscale(enable = True)
			self.axes_Q1.loglog(Q1_x, Q1_y, self.plot_symbol)
			self.axes_Q2.loglog(Q2_x, Q2_y, self.plot_symbol)
			self.axes_Q3.loglog(Q3_x, Q3_y, self.plot_symbol)
			self.axes_Q4.loglog(Q4_x, Q4_y, self.plot_symbol)
			
			if not hasattr(self, 'flip_Q3'):
				self.flip_Q3 = True
			
				# Reverse Q2 x-axis
				self.axes_Q2.set_xlim(self.axes_Q2.get_xlim()[::-1])	
				
				# Reverse Q3 x- and y-axes
				self.axes_Q3.set_xlim(self.axes_Q3.get_xlim()[::-1])
				self.axes_Q3.set_ylim(self.axes_Q3.get_ylim()[::-1])
				
				# Reverse Q4 y-axis
				self.axes_Q4.set_ylim(self.axes_Q4.get_ylim()[::-1])
			
			# Set axis tickmarks at powers of 10
			# Q1 axes
			if Q1_x == [] and not self.hold_cb.isChecked():
				self.axes_Q1.set_xticklabels([])
				self.axes_Q1.set_yticklabels([])
			else:
				try:
					x_UB_Q1 = int(ceil(log10(max(Q1_x))))
					y_UB_Q1 = int(ceil(log10(max(Q1_y))))
					x_LB_Q1 = int(floor(log10(min(Q1_x))))
					y_LB_Q1 = int(floor(log10(min(Q1_y))))
				except:
					x_UB_Q1 = 2
					y_UB_Q1 = 2
					x_LB_Q1 = -1
					y_LB_Q1 = -1
				Q1_xlabels = []
				Q1_ylabels = []
				for i in range(x_LB_Q1, x_UB_Q1 + 1):
					Q1_xlabels.append('$10^{%s}$' % str(i))
				for i in range(y_LB_Q1, y_UB_Q1 + 1):
					Q1_ylabels.append('$10^{%s}$' % str(i))
				self.axes_Q1.set_xticklabels(Q1_xlabels)
				self.axes_Q1.set_yticklabels(Q1_ylabels)
			self.axes_Q1.xaxis.tick_top()
			self.axes_Q1.yaxis.tick_right()
			
			# Q2 axes
			if Q2_x == [] and not self.hold_cb.isChecked():
				self.axes_Q2.set_xticklabels([])
				self.axes_Q2.set_yticklabels([])
			else:
				try:
					x_UB_Q2 = int(ceil(log10(max(Q2_x))))
					y_UB_Q2 = int(ceil(log10(max(Q2_y))))
					x_LB_Q2 = int(floor(log10(min(Q2_x))))
					y_LB_Q2 = int(floor(log10(min(Q2_y))))
				except:
					x_UB_Q2 = 2
					y_UB_Q2 = 2
					x_LB_Q2 = -1
					y_LB_Q2 = -1
				Q2_xlabels = []
				Q2_ylabels = []
				for i in range(x_LB_Q2, x_UB_Q2 + 1):
					Q2_xlabels.append('$-10^{%s}$' % str(i))
				for i in range(y_LB_Q2, y_UB_Q2 + 1):
					Q2_ylabels.append('$10^{%s}$' % str(i))
				self.axes_Q2.set_xticklabels(Q2_xlabels)
				self.axes_Q2.set_yticklabels(Q2_ylabels)
			self.axes_Q2.xaxis.tick_top()
			self.axes_Q2.yaxis.tick_left()
		
			# Q3 axes
			if Q3_x == [] and not self.hold_cb.isChecked():
				self.axes_Q3.set_xticklabels([])
				self.axes_Q3.set_yticklabels([])
			else:
				try:
					x_UB_Q3 = int(ceil(log10(max(Q3_x))))
					y_UB_Q3 = int(ceil(log10(max(Q3_y))))
					x_LB_Q3 = int(floor(log10(min(Q3_x))))
					y_LB_Q3 = int(floor(log10(min(Q3_y))))
				except:
					x_UB_Q3 = 2
					y_UB_Q3 = 2
					x_LB_Q3 = -1
					y_LB_Q3 = -1
				Q3_xlabels = []
				Q3_ylabels = []
				for i in range(x_LB_Q3, x_UB_Q3 + 1):
					Q3_xlabels.append('$-10^{%s}$' % str(i))
				for i in range(y_LB_Q3, y_UB_Q3 + 1):
					Q3_ylabels.append('$-10^{%s}$' % str(i))
				self.axes_Q3.set_xticklabels(Q3_xlabels)
				self.axes_Q3.set_yticklabels(Q3_ylabels)
			self.axes_Q3.xaxis.tick_bottom()
			self.axes_Q3.yaxis.tick_left()
				
			# Q4 axes
			if Q4_x == [] and not self.hold_cb.isChecked():
				self.axes_Q4.set_xticklabels([])
				self.axes_Q4.set_yticklabels([])
			else:
				try:
					x_UB_Q4 = int(ceil(log10(max(Q4_x))))
					y_UB_Q4 = int(ceil(log10(max(Q4_y))))
					x_LB_Q4 = int(floor(log10(min(Q4_x))))
					y_LB_Q4 = int(floor(log10(min(Q4_y))))
				except:
					x_UB_Q4 = 2
					y_UB_Q4 = 2
					x_LB_Q4 = -1
					y_LB_Q4 = -1
				Q4_xlabels = []
				Q4_ylabels = []
				for i in range(x_LB_Q4, x_UB_Q4 + 1):
					Q4_xlabels.append('$10^{%s}$' % str(i))
				for i in range(y_LB_Q4, y_UB_Q4 + 1):
					Q4_ylabels.append('$-10^{%s}$' % str(i))
				self.axes_Q4.set_xticklabels(Q4_xlabels)
				self.axes_Q4.set_yticklabels(Q4_ylabels)
			self.axes_Q4.xaxis.tick_bottom()
			self.axes_Q4.yaxis.tick_right()

def main():
	# Check if QApplication already exists; if not, create it!
	# (IPython compatibility)
	app = QApplication.instance()
	if not app:
		app = QApplication(sys.argv)
	cp = CutePlot()
	cp.show()
	sys.exit(app.exec_())
			
if __name__ == '__main__':
	main()
