import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


@pytest.mark.parametrize("p", ["python",
                               "python36",
                               "python-setuptools",
                               "python36-setuptools"])
def test_python_installed(host, p):
    pkg = host.package(p)
    assert pkg.is_installed


# @pytest.mark.parametrize("pip_package", ["pytest"])
# def test_python_tools(host):
#     assert host.pip_package.get_packages()


@pytest.mark.parametrize("p", ["ruby",
                               "ruby-devel",
                               "ruby-irb",
                               "ruby-libs",
                               "rubygems"])
def test_ruby_installed(host, p):
    pkg = host.package(p)
    assert pkg.is_installed


def test_security_updates(host):
    '''
    check the stuff that quay gives you and test for vulnerabilities
    '''
    assert not host.package('kernel_headers').is_installed
