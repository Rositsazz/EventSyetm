#!/usr/bin/env python
import platform
import subprocess
import sys

from os.path import dirname, join, isdir

root_path = join(dirname(__file__), '../..')


class VirtualEnvBuilder(object):
    def __init__(self):
        pass

    @property
    def venv_path(self):
        return join(root_path, self.venv_name)

    @property
    def venv_name(self):
        return "VirtEnvs/" + dirname(__file__).split("/")[-1]

    def build(self):
        print("Building virtual env from Python version {}".format(sys.version))

        # Create a fresh virtual env
        self.create_venv(self.venv_path)
        file_name = join(dirname(__file__)) +  "\\requirements.txt"
        import os.path
        if os.path.exists(file_name):
            print("Requirements file exists!")
        else:
            print("Requirements file does not exist!")
        self.run_in_venv('pip3', ['install', '-r', file_name])
        print("Done")

    @staticmethod
    def create_venv(venv_path):
        if isdir(venv_path):
            return

        from virtualenv import create_environment
        create_environment(venv_path)


    def run_in_venv(self, cmd, args):
        virtual_env_bin_path = self.venv_name
        if platform.system() == 'Windows':
            cmd += '.exe'
            virtual_env_bin_path += r'/Scripts'
        else:
            virtual_env_bin_path += r'/bin'

        import os.path
        if not os.path.exists(join(root_path, virtual_env_bin_path, cmd)):
            return "Pip3 not found!"
        subprocess.check_call([join(root_path, virtual_env_bin_path, cmd)] + args)


if __name__ == '__main__':
    builder = VirtualEnvBuilder()
    builder.build()
