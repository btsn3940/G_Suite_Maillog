@echo off

rem �Y��������ڂ̃o�b�`���Ńt�@�C�����𐶐�����
rem 1�@�c�@YYYYMMDD-0200-YYYYMMDD-1000�i10:XX���s�j
rem 2�@�c�@YYYYMMDD-1000-YYYYMMDD-1600�i16:XX���s�j
rem 3�@�c�@YYYYMMDD-1600-YYYYMMDD-0200�i02:XX���s�j
set EXEC_DATE=%date:~0,4%%date:~5,2%%date:~8,2%

rem ����̓��t���擾���郍�W�b�N
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

rem csv���_�E�����[�h���ꂽ�p�X�Ɉړ����ăt�@�C����move�������s��
cd (change directory full path ex)C:\Users\xxxxxxxx\Downloads )
rem ����ڂ̎��s���ɂ���ĐU�蕪����
rem �i�ړ���͉��œ��͂��Ă���̂Ŏ��ۂ̊��ɍ��킹�ĉ������j
if %1 == 1 (
	move LogSearchResults* \\file_server_path\maillog\LogSearchResults-%EXEC_DATE%-0200-%EXEC_DATE%-1000.csv
) else if %1 == 2 (
	move LogSearchResults* \\file_server_path\maillog\LogSearchResults-%EXEC_DATE%-1000-%EXEC_DATE%-1600.csv
) else if %1 == 3 (
	move LogSearchResults* \\file_server_path\maillog\LogSearchResults-%EXEC_DATE_YESTERDAY%-1600-%EXEC_DATE%-0200.csv
)