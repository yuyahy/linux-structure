#!/usr/bin/python3
import signal
# SIGINTシグナルを無視する
# 第一引数にハンドラを設定するシグナルの番号を、
# 第二引数にシグナルハンドラを指定する
signal.signal(signal.SIGINT, signal.SIG_IGN)
while True:
    pass