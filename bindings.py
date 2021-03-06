# vim like online text editing
config.bind('\\', 'mode-enter normal', mode='insert')
config.bind('$', 'fake-key <End>')
config.bind('0', 'fake-key <Home>')
config.bind('I', 'fake-key <Home>;; mode-enter insert')
config.bind('A', 'fake-key <End>;; mode-enter insert')
config.bind('cw', 'fake-key <Ctrl-Delete>;; mode-enter insert')
config.bind('cc', 'fake-key <Home><Shift-End><Delete>;; mode-enter insert')
config.bind('c$', 'fake-key <Shift-End><Delete>;; mode-enter insert')
# for Google Docs
config.bind('*', 'fake-key <Ctrl-Shift-Right><Ctrl-b>')
config.bind('_', 'fake-key <Ctrl-Shift-Right><Ctrl-i>')
