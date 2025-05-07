#!/usr/bin/python3

import os
import sys

ret = os.fork()
if ret==0:
    # 自身が子プロセス
    print(f"child process: pid={os.getpid()}, parent process: pid={os.getppid()}")
    # execveを使って、自身のプロセスのプログラムをechoに書き換え
    os.execve("/bin/echo", ["echo", f"pid={os.getpid()}からこんにちは"], {})
    exit()
elif ret>0:
    # 自身が親プロセス
    print(f"parent process: pid={os.getpid()}, child process: pid={ret}")
    # execveを使って、自身のプロセスのプログラムをechoに書き換え
    os.execve("/bin/echo", ["echo", f"pid={os.getpid()}"], {})
    exit()
sys.exit(1)