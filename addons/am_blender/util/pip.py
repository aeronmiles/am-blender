# SPDX-License-Identifier: GPL-2.0-or-later

# ----------------------------------------------------------
# Author: Stephen Leger (s-leger)
#
# ----------------------------------------------------------
import typing
import bpy
import subprocess
import os
import sys
import site

PYPATH = sys.executable  # bpy.app.binary_path_python


# TODO: add install location options e.g. site-packages, ./local etc.
class Pip:
    def __init__(self):
        self._ensurepip()

    @staticmethod
    def _ensure_user_site_package():
        site_package = site.getusersitepackages()
        if not os.path.exists(site_package):
            site_package = bpy.utils.user_resource('SCRIPTS', create=True)
            site.addsitedir(site_package)
        if site_package not in sys.path:
            sys.path.append(site_package)

    def _cmd(self, action, options, module):
        if options is not None and "--user" in options:
            self._ensure_user_site_package()

        cmd = [PYPATH, "-m", "pip", action]

        if options is not None:
            cmd.extend(options.split(" "))

        cmd.append(module)
        return self._run(cmd)

    def _popen(self, cmd):
        popen = subprocess.Popen(
            cmd, stdout=subprocess.PIPE, universal_newlines=True)
        for stdout_line in iter(popen.stdout.readline, ""):
            yield stdout_line
        popen.stdout.close()
        popen.wait()

    def _run(self, cmd):
        res = False
        status = ""
        for line in self._popen(cmd):
            if "error" in line.lower():
                status = line.strip()
                print(f'Pip._run() :: Error :: {line}')
            if "successfully" in line.lower():
                status = line.strip()
                res = True
                print(f'Pip._run() :: Success :: {line}')

        return res, status

    def _ensurepip(self):
        pip_not_found = False
        try:
            import pip
        except ImportError:
            pip_not_found = True
            print(f'Pip._ensurepip() :: Error :: pip not found')
        if pip_not_found:
            print(
                f'Pip._ensurepip() :: trying to install pip with {PYPATH} -m --default-pip')
            self._run([PYPATH, "-m", "ensurepip", "--default-pip"])

    @staticmethod
    def upgrade_pip():
        return Pip()._cmd("install", "--upgrade", "pip")

    @staticmethod
    def uninstall(module, options=None):
        """
        :param module: string module name with requirements see:[1]
        :param options: string command line options  see:[2]
        :return: True on uninstall, False if already removed, raise on Error
        [1] https://pip.pypa.io/en/stable/reference/pip_install/#id29
        [2] https://pip.pypa.io/en/stable/reference/pip_install/#id47
        """
        if options is None or options.strip() == "":
            # force confirm
            options = "-y"
        return Pip()._cmd("uninstall", options, module)

    @staticmethod
    def install(module, options=None):
        """
        :param module: string module name with requirements see:[1]
        :param options: string command line options  see:[2]
        :return: True on install, False if already there, raise on Error
        [1] https://pip.pypa.io/en/stable/reference/pip_install/#id29
        [2] https://pip.pypa.io/en/stable/reference/pip_install/#id47
        """

        if options is None or options.strip() == "":
            # store in user writable directory, use wheel
            options = "--user --only-binary all"

        installed = ()
        try:
            installed = Pip()._cmd("install", options, module)
            exec(f'import {module}')
        except Exception as e:
            print(f'{module} install failed! : {e}')

        return installed

    @staticmethod
    def ensure_packages(packages: typing.Iterable[str]):
        Pip._ensure_user_site_package()
        for m in packages:
            try:
                exec(f'import {m}')
            except ImportError:
                Pip.install(m)

    @staticmethod
    def python_version():
        """
        :return: python version object
        """
        # version.major, version.minor, version.micro
        return sys.version_info
