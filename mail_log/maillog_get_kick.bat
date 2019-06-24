@echo off

rem 「c:\task」直下に展開している想定でフォルダ移動します
c:
cd c:\task\maillog

rem python実行パスをフルパスで記述する %1 はタスクマネージャーでの引数を指す
(python execution full path ex)c:\python\python ) maillog_get.py %1
