Ubuntu là một hệ điều hành được phát triển dựa trên Linux kernel. Những hệ điều hành được phát triển dựa trên Linux kernel được gọi chung là Linux distro

Do Ubuntu được phát triển dựa trên Linux kernel, tất cả các Linux commands (cd, mkdir, touch, ls, cat, chmod, chown, …) đều chạy bình thường trên Ubuntu. Ngoài ra, Ubuntu còn có giao diện cho người dùng (GUI - Graphical User Interface) tương tự như 2 hệ điều hành Windows và MacOS, giúp cho những người vốn đã quen với 2 hệ điều hành này có thể dễ dàng thao tác và sử dụng Ubuntu

Do là một Linux distro, Ubuntu cũng tổ chức file và thư mục theo cấu trúc dạng cây:
<div align="center"><img src="https://github.com/maivan-hoa/Note/blob/main/images/ubuntu1.png?raw=true" width="700"></div> 
<div align="center"><img src="https://github.com/maivan-hoa/Note/blob/main/images/ubuntu2.png?raw=true" width="500"></div> 

Một số thư mục chính:

- /bin: Chứa các file binary của các command như ls, cd, mkdir, touch, rm, …
- /boot: Chứa các file dùng để khởi động hệ thống (Linux kernel, RAM Disk Image, …)
- /home: Thư mục home của người dùng. Mỗi user sẽ được cấp một thư mục riêng bên trong thư mục /home
- /root: Thư mục home của super user
- /sbin: Chứa file binary của các command chỉ có thể được dùng bởi superuser
- …

Để cài đặt phần mềm trên Ubuntu, các bạn có thể sử dụng Ubuntu Software Center. Cách sử dụng gần như y hệt khi bạn sử dụng App Store hay Google Play để cài ứng dụng di động

Nếu như bạn thích gõ command line trên terminal, các bạn có thể sử dụng lệnh `sudo apt-get install`. Ví dụ, bạn có thể cài đặt Git trên Ubuntu bằng lệnh sau:
```
$ sudo apt-get update
$ sudo apt-get install git
```

- Chạy lệnh trên Ubuntu có dạng: `command [options][arguments]`
- Trợ giúp lệnh: `man [lệnh]`













































