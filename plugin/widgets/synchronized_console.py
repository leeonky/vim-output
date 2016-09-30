from subprocess import Popen, STDOUT, PIPE

class SynchronizedConsole(object):
	def __init__(self, *args):
		handle = Popen(list(args), shell=True, stdout=PIPE, stderr=STDOUT, stdin=PIPE)
		self._output = handle.stdout.read()

	def pop_rows(self):
		out = self._output
		self._output = []
		return out
