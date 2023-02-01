from paver.easy import *
import threading, os, platform
import subprocess


def run_setup_environment(args):
    print("running command: python3 setup_environment.py")
    result = subprocess.run(f"python3 tests/setup_environment.py {args}", shell=True)
    if result.returncode == 0:
        print("Command executed successfully")
    else:
        print("Command failed with return code:", result.returncode)


def run_tear_down_environment(args):
    print("running command: python3 tear_down_environment.py")
    result = subprocess.run(f"python3 tests/tear_down_environment.py {args}", shell=True)

    if result.returncode == 0:
        print("Command executed successfully")
    else:
        print("Command failed with return code:", result.returncode)

@task
@consume_nargs(2)
def run(args):
    if args[0] == 'setup':
        run_setup_environment(args[1])
    elif args[0] == 'teardown':
        run_tear_down_environment(args[1])
    else:
        print("Wrong paver task given")

# @task
# @consume_nargs(1)
# def run(args):
#     if args[0] == 'ct_test':
#         jobs = []
#         for index in range(2):
#             thread = threading.Thread(target=run_behave_test,args=(index,))
#             jobs.append(thread)
#             thread.start()
#
#         for thread in jobs:
#             thread.join()
#     else:
#         print("Wrong paver task given")