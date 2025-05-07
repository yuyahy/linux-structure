#!/usr/bin/python3

import os
import sys

# プロセスのコピーを生成
# - 親プロセスの場合はretが子プロセスのPID
# - 子プロセスの場合はretが0
# ※プロセスIDは1以上
ret=os.fork()

if ret==0:
    # 自身が子プロセス
    print(f"child process: pid={os.getpid()}, parent process: pid={os.getppid()}")
    exit()
elif ret>0:
    # 自身が親プロセス
    print(f"parent process: pid={os.getpid()}, child process: pid={ret}")
    exit()

sys.exit(1)
