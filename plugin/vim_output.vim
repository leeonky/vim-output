" --------------------------------
" Add our plugin to the path
" --------------------------------
python import sys
python import vim
python sys.path.append(vim.eval('expand("<sfile>:h")'))
python sys.path.append(vim.eval('expand("<sfile>:h")')+'/widgets')

python << endOfPython

import output_form
import blocked_console

class VimOutput(object):
	OutputForm = output_form.OutputForm
	BlockedConsole = blocked_console.BlockedConsole

	@staticmethod
	def execute(title, *commands):
		rich_box = VimETUI.RichMessageBox(title=title)
		rich_box.show()

		console = VimOutput.BlockedConsole(*commands)

		output_form = VimOutput.OutputForm(rich_box, console)
		output_form.synchronize()

		return output_form


endOfPython

function! TestSyncCmd(cmds)
python << endOfPython

VimOutput.execute('Console', *vim.eval('a:cmds'))

endOfPython
endfunction
