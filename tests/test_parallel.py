from __future__ import with_statement

from datetime import datetime
import copy
import getpass
import sys

import paramiko
from nose.tools import with_setup
from fudge import (Fake, clear_calls, clear_expectations, patch_object, verify,
    with_patched_object, patched_context, with_fakes)

from fabric.context_managers import settings, hide, show
from fabric.network import (HostConnectionCache, join_host_strings, normalize,
    denormalize)
from fabric.io import output_loop
import fabric.network # So I can call patch_object correctly. Sigh.
from fabric.state import env, output, _get_system_username
from fabric.operations import run, sudo
from fabric.decorators import runs_parallel, hosts

from utils import *
from server import (server, PORT, RESPONSES, PASSWORDS, CLIENT_PRIVKEY, USER,
    CLIENT_PRIVKEY_PASSPHRASE)


@server(port=2220)
@server(port=2221)
@server(port=2222)
@server(port=2223)
@server(port=2224)
@server(port=2225)
@server(port=2226)
@server(port=2227)
@server(port=2228)
@server(port=2229)
@server(port=2230)



def test_runs_parallel():
    """
    Do a simple call and respond, in parallel
    """

    @runs_parallel(5)
    @hosts(['127.0.0.1:%s' % x for x in range(2220,2231)])
    def foo():
#   ports = range(2220,2231)
#   hosts = map(lambda x: '127.0.0.1:%s' % x, ports)
#   with settings(all_hosts=hosts, run_in_parallel=True, pool_size=5):
#       for port in ports:
        with settings(hide('everything')):
            cmd = "ls /simple"
            print run(cmd), env.host_string
            eq_(run(cmd), RESPONSES[cmd])

