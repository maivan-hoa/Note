# Cài đặt
1. Tải file cài đặt: `wget https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh`
	- Thay 2020.02 bằng phiên bản muốn cài

2. Run Anaconda Installation Script: `bash Anaconda3-2022.10-Linux-x86_64.sh`
	- Ấn Enter để đọc license và cuối cùng gõ 'yes'
	- Ấn Enter để xác nhận location cài đặt
	- Gõ yes để kết thúc cài đặt

3. Activate installation: `source ~/.bashrc`


# Các lệnh với Anaconda 
- (https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
- https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf
- `conda info`
- `conda env list`
- Tạo môi trường: `conda create ––name name_environment python=3`
- Activate môi trường: `conda activate name_environment`
- Xóa môi trường: `conda env remove --name name_environment`
- Sharing an environment (To allow them to quickly reproduce your environment, with all of its packages and versions, give them a copy of your environment.yml file):
	- Exporting the environment.yml file:
		- Activate the environment to export: `conda activate myenv`
		- Export your active environment to a new file: `conda env export > environment.yml`
	- Create the environment from the environment.yml file: `conda env create -f environment.yml`

- `conda install --file requirements.txt`




