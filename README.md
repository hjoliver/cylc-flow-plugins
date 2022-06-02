# cylc-flow-plugins

Cylc plugin skeleton examples.

1. cylc install plugin: install/hello

```console
# In your cylc-flow environment:
$ cd /path/to/cylc-flow-plugins/install/hello
$ pip install .

# Now install a workflow
$ cd ~/cylc-src/test
$ cylc install
>>> hello from pre_configure: /home/oliverh/cylc-src/test -> None
INSTALLED test/run8 from /home/oliverh/cylc-src/test
>>> hello from post_install: /home/oliverh/cylc-src/test -> /home/oliverh/cylc-run/test/run8
```
