# Edit text online with vim-like style
I did this to make editing in editors like Google Docs and Overleaf a little bit better.

## Installation
You only need to copy the contents of `bindings.py` to your `config.py` and then you also may check if you have already set one of those bindings to another command.

## Available mechanics
General

`'\'  enter Normal mode`

`'0'  cursor to the beginning of the line`

`'$'  cursor to the ending of the line`

`'I'  cursor to beginning of line and enter Insert mode`

`'A'  cursor to ending of line and enter Insert mode`

`'cw' delete whole line and enter Insert mode`

`'c$' delete to the end of the line and enter Insert mode`

Google Docs specific

`'*'  toggle bold until end of word`

`'_'  toggle italic until end of word`

