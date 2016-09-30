import unittest
from plugin.widgets.output_form import OutputForm

class TestOutputForm(unittest.TestCase):
	def test_show_form(self):
		class FakeOutputer(object):
			def __init__(self):
				self._content = []
			def append(self, rows):
				self._content.extend(rows)
			def content(self):
				return self._content

		class FakeRowProvider(object):
			def pop_rows(self):
				return ['hello', 'world']

		outputer = FakeOutputer()
		row_provider = FakeRowProvider()

		output_form = OutputForm(outputer, row_provider)

		output_form.synchronize()
		self.assertEqual(outputer.content(), ['hello', 'world'])
