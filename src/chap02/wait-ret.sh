#!/bin/bash

false &
wait $! # falseプロセスの終了を待ち合わせる。falseコマンドのPIDは$!で取得できる。
echo "falseプロセスが終了しました : $?" # wait後にfalseプロセスの戻り値は$?で取得できる。