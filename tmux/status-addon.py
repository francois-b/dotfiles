#!/usr/bin/env python
import datetime
foo = "#[fg=green,bg=default,bright]{0}"
foo2 = "#[fg=blue,bg=default,bright]{0}"
seconds = datetime.datetime.now().strftime("%s")
if int(seconds) %2:
    print foo.format(seconds)
else:
    print foo2.format(seconds)

