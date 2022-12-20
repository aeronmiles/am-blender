import pkg_resources
import subprocess
import sys
import os

modules = ("jsonpickle",)
for m in modules:
    sys.path.insert(0, os.path.join(os.path.dirname(
        os.path.realpath(__file__)), f"lib/{m}"))


def install_modules():
    missing = {m for m in modules} - \
        {pkg.key for pkg in pkg_resources.working_set}

    if not missing:
        return

    python_exe = os.path.join(sys.prefix, 'bin', 'python.exe')
    target = os.path.join(sys.prefix, 'lib', 'site-packages')

    subprocess.call([python_exe, '-m', 'ensurepip'])
    subprocess.call([python_exe, '-m', 'pip', 'install', '--upgrade', 'pip'])

    for pkg in missing:
        subprocess.call([python_exe, '-m', 'pip', 'install',
                        '--upgrade', pkg, '-t', target])
