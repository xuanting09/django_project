1. 為專案建立虛擬環境 virtualenv
    1. 創建資料夾：`mkdir tutorial`
    2. 進入資料夾： `cd tutorial`
    3. 建立虛擬環境：`python3 -m venv <name_of_env>`
        1. conda查看虛擬環境：`conda env list`
        2. conda刪除虛擬環境：`conda env remove --name <name_of_env>`
        3. 刪除python 虛擬環境：`rm -rf <name_of_env>`
    4. 啟動虛擬環境：`source <name_of_env>/bin/activate`
2. 啟用虛擬環境、安裝專案所需套件
    1. 安裝 Django：`pip install django`
3. 建立新Django專案
    1. 創建一個新的 Django 項目：`django-admin startproject <name_of_project>`
    2. 進入項目：`cd <name_of_project>`
4. 啟動伺服器，讓網站在本地電腦運作
    1. 運行 Django 開發服務器：`python [manage.py](http://manage.py/) runserver`
    2. 想在不同的IP地址或端口上運行服務器：`python [manage.py](http://manage.py/) runserver 0.0.0.0:8080`
    3. 查看 Django 項目：http://127.0.0.1:8000/
5. Django 管理權限位置：http://127.0.0.1:8000/admin
