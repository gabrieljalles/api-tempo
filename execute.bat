echo -----------------------%DATE%--------------------------- >> C:\api-tempo\log.txt
echo Stating script at  %DATE% %TIME% >> C:\api-tempo\log.txt

rem Ative o ambiente virtual
call C:\api-tempo\venv\Scripts\activate

rem Execute o script Python no ambiente virtual
python C:\api-tempo\main.py >> C:\api-tempo\log.txt 2>&1

rem Desative o ambiente virtual
call C:\api-tempo\venv\Scripts\deactivate

echo Finished script at %DATE% %TIME% >> C:\api-tempo\log.txt
