import sublime, sublime_plugin, os

class GoToSpecCommand(sublime_plugin.WindowCommand):
	def open_spec(self, folder, dirname, filename, extension):
		if dirname.startswith('/app'):
			dirname = dirname[4:]

		dirname = "/spec" + dirname + "/"
		filename = filename + "_spec" + extension

		spec_file = folder + dirname + filename

		if os.path.isfile(spec_file):
			self.window.open_file(spec_file)

	def open_test_subject(self, folder, dirname, filename, extension):
		filename = filename[0:-5]
		dirname = dirname[5:]

		test_subject = folder + dirname + '/' + filename + extension
		if os.path.isfile(test_subject):
			self.window.open_file(test_subject)
			return
		
		test_subject = folder + '/app' + dirname + '/' + filename + extension
		if os.path.isfile(test_subject):
			self.window.open_file(test_subject)
			return

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
			self.open_test_subject(folder, dirname, filename, extension)
		else:
			self.open_spec(folder, dirname, filename, extension)


		