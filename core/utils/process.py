import subprocess
import os


def run_command(command_and_args, working_directory=None):
    try:
        env = os.environ.copy()
        process = subprocess.Popen(command_and_args, env=env, cwd=working_directory, shell=True, stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        return process.returncode, stdout.decode('utf-8'), stderr.decode('utf-8')
    except Exception as e:
        return -1, None, 'Exception when running command: %s\nError:%s'.format(command_and_args, e)
