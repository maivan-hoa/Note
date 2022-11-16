# Pipenv
Quản lý các package như npm của NodeJS

- Cài đặt: `pip install pipenv`

- Tạo thư mục project, sau đó dùng lệnh: `pipenv install`
--> sẽ tạo hai file pipfile và pipfile.log nhằm lưu thông tin các thư viện và các dependencies

- Tìm nơi môi trường ảo được lưu trữ: 
`pipenv --where` hoặc  `pipenv --venv`

- Xem các package của dự án dưới dạng graph: `pipenv graph`

- Kích hoạt môi trường ảo: `pipenv shell`
- Thoát môi trường ảo: `exit`
- Chạy code sau khi đã active môi trường ảo: `python my_file.py`

- Chạy code mà không cần active môi trường ảo: `pipenv run python my_file.py`


# Virtualenv
- Cài đặt: `pip install virtualenv`

- Tạo virtual environment: `virtualenv my_env`
--> This creates a folder in the current directory with the name of the environment (my_env/). This folder contains the directories for installing modules and Python executables.

- Activate môi trường ảo: `source my_env/bin/activate`
--> sau khi kích hoạt môi trường ảo, tất cả những package được cài đặt mới sẽ nằm trong thư mục my_env/

- Thoát khỏi môi trường ảo: `deactivate`

- Cài đặt package: 
```
pip install some-package
pip install -r requirements.txt
```

- Tạo file requirements.txt: `pip freeze > requirements.txt`








