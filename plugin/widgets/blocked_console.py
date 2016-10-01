from subprocess import Popen, STDOUT, PIPE

class BlockedConsole(object):
	def __init__(self, *args):
		handle = Popen(args, stdout=PIPE, stderr=STDOUT)
		self._output = handle.stdout.read().splitlines()

	def pop_rows(self):
		out = self._output
		self._output = []
		return out
