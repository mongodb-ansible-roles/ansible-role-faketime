import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_faketime(host):
    cmd = host.run("faketime --version")
    assert cmd.succeeded
    assert cmd.stdout == """
faketime: Version 0.9.7
For usage information please use 'faketime --help'.
"""
