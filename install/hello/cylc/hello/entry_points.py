"""
cylc install plugin example.
"""

from cylc.hello.utils import speak


def pre_configure(srcdir=None, opts=None, rundir=None):
    speak("pre_configure", srcdir, rundir)
    return {
        "env": {},
        "template_variables": {},
        "templating_detected": None
    }


def post_install(srcdir=None, opts=None, rundir=None):
    speak("post_install", srcdir, rundir)
    return True
