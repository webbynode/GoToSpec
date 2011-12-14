import sublime, sublime_plugin, os

class GoToSpecCommand(sublime_plugin.WindowCommand):
	def open_left(self, file):
		self.window.open_file(file)
		if self.window.active_group() == 0:
			return

		self.window.run_command('close')
		self.window.run_command('set_layout', 
			{ "cols": [0.0, 0.5, 1.0], "rows": [0.0, 1.0], "cells": [[0,0,1,1],[1,0,2,1]] })

		self.window.focus_group(0)
		self.window.open_file(file)

	def open_right(self, file):
		self.window.open_file(file)
		if self.window.active_group() == 1:
			return

		self.window.run_command('close')
		self.window.run_command('set_layout', 
			{ "cols": [0.0, 0.5, 1.0], "rows": [0.0, 1.0], "cells": [[0,0,1,1],[1,0,2,1]] })

		self.window.focus_group(1)
		self.window.open_file(file)

	def find_spec(self, folder, dirname, filename, extension):
		if dirname.startswith('/app'):
			dirname = dirname[4:]

		dirname = "/spec" + dirname + "/"
		filename = filename + "_spec" + extension

		spec_file = folder + dirname + filename
		if os.path.isfile(spec_file):
			return spec_file

		dirname = dirname.replace('spec/', 'spec/requests/')

		spec_file = folder + dirname + filename
		if os.path.isfile(spec_file):
			return spec_file

	def find_test_subject(self, folder, dirname, filename, extension):
		filename = filename[0:-5]
		dirname = dirname[5:] + '/'

		test_subject = folder + dirname + filename + extension
		if os.path.isfile(test_subject):
			return test_subject

		dirname = '/app' + dirname
		test_subject = folder + dirname + filename + extension
		if os.path.isfile(test_subject):
			return test_subject

		dirname = dirname.replace('/requests', '')
		test_subject = folder + dirname + filename + extension
		if os.path.isfile(test_subject):
			return test_subject

	def run(self):
		view = self.window.active_view()
		current_file = view.file_name()

		folders = self.window.folders()
		for folder in folders:
			if current_file.startswith(folder):
				current_folder = folder
				current_file   = current_file.replace(folder, "")
		
		dirname  = os.path.dirname(current_file)
		filename = os.path.basename(current_file)
		filename, extension = os.path.splitext(filename)

		if filename.endswith('_spec'):
			spec_file    = current_folder + current_file
			subject_file = self.find_test_subject(folder, dirname, filename, extension)

			if spec_file and subject_file:
				self.open_left(spec_file)
				self.open_right(subject_file)
		else:
			spec_file    = self.find_spec(folder, dirname, filename, extension)
			subject_file = current_folder + current_file

			if spec_file and subject_file:
				self.open_right(subject_file)
				self.open_left(spec_file)



		