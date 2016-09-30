" --------------------------------
" Add our plugin to the path
" --------------------------------
python import sys
python import vim
python sys.path.append(vim.eval('expand("<sfile>:h")'))
python sys.path.append(vim.eval('expand("<sfile>:h")')+'/widgets')

python << endOfPython

import output_form
import synchronized_console

class VimOutput(object):
	OutputForm = output_form.OutputForm
	SynchronizedConsole = synchronized_console.SynchronizedConsole

endOfPython

function! TestSyncCmd(cmds)
python << endOfPython
import vim

rich_box = VimETUI.RichMessageBox(title='Console')
rich_box.show()

console = VimOutput.SynchronizedConsole(*vim.eval('a:cmds'))

VimOutput.OutputForm(rich_box, console).synchronize()

endOfPython
endfunction
