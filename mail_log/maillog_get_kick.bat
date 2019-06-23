@echo off

rem 
c:
cd c:\task\maillog

rem python実行パスをフルパスで記述する %1 はタスクマネージャーでの引数を指す
(python execution full path ex)c:\python\python ) maillog_get.py %1