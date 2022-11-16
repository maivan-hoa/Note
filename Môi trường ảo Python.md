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
