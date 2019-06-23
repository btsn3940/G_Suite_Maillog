@echo off

rem 該当日何回目のバッチかでファイル名を生成する
rem 1　…　YYYYMMDD-0200-YYYYMMDD-1000（10:XX実行）
rem 2　…　YYYYMMDD-1000-YYYYMMDD-1600（16:XX実行）
rem 3　…　YYYYMMDD-1600-YYYYMMDD-0200（02:XX実行）
set EXEC_DATE=%date:~0,4%%date:~5,2%%date:~8,2%

rem 昨日の日付を取得するロジック
set YY=%date:~0,4%
set MM=%date:~5,2%
set DD=%date:~8,2%
set /a DD=%DD%-1
set DD=00%DD%
set DD=%DD:~-2%
set /a ymod=%YY% %% 4
if %DD%==00 (
if %MM%==01 (set MM=12&& set DD=31&& set /a YY=%YY%-1)
if %MM%==02 (set MM=01&& set DD=31)
if %MM%==03 (set MM=02&& set DD=28&& if %ymod%==0 (set DD=29))
if %MM%==04 (set MM=03&& set DD=31)
if %MM%==05 (set MM=04&& set DD=30)
if %MM%==06 (set MM=05&& set DD=31)
if %MM%==07 (set MM=06&& set DD=30)
if %MM%==08 (set MM=07&& set DD=31)
if %MM%==09 (set MM=08&& set DD=31)
if %MM%==10 (set MM=09&& set DD=30)
if %MM%==11 (set MM=10&& set DD=31)
if %MM%==12 (set MM=11&& set DD=30)
)
set EXEC_DATE_YESTERDAY=%YY%%MM%%DD%

rem csvがダウンロードされたパスに移動してファイルのmove処理を行う
cd (change directory full path ex)C:\Users\xxxxxxxx\Downloads )
rem 何回目の実行かによって振り分ける
rem （移動先は仮で入力しているので実際の環境に合わせて下さい）
if %1 == 1 (
	move LogSearchResults* \\file_server_path\maillog\LogSearchResults-%EXEC_DATE%-0200-%EXEC_DATE%-1000.csv
) else if %1 == 2 (
	move LogSearchResults* \\file_server_path\maillog\LogSearchResults-%EXEC_DATE%-1000-%EXEC_DATE%-1600.csv
) else if %1 == 3 (
	move LogSearchResults* \\file_server_path\maillog\LogSearchResults-%EXEC_DATE_YESTERDAY%-1600-%EXEC_DATE%-0200.csv
)