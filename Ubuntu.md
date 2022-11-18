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


# Một số lệnh terminal thông dụng làm việc với file và thư mục Ubuntu

- `pwd`: viết tắt của Print Working Directory, được sử dụng để in ra đường dẫn thư mục đang làm việc
- `ls`: liệt kê ra nội dung trong thư mục hiện hành
- `ls -a`: hiển thị tất cả file và thư mục, bao gồm cả file và thư mục ẩn (file và thư mục ẩn thường có dấu '.' ở trước tên)

- `cd`: viết tắt của Change Direction, có nhiệm vụ thay đổi thư mục làm việc
  - `../` là lùi một cấp thư mục
  - Nếu tên thư mục có khoảng trắng, hãy gõ tên nó trong dấu " " hoặc ' '
  
- `dir`: có tác dụng như lệnh `ls`, nhưng `dir` chỉ liệt kê thư mục, không liệt kê các file khác

- `touch`: là một lệnh trong Terminal dùng để thay đổi thời gian truy cập và sửa đổi file, nhưng nó cũng được dùng để tạo nhanh một file mới, với cú pháp như sau:
  - `touch file1 file2 file3`
  - Trong đó file1, file2, file3 là tên tệp bạn muốn tạo mới, các file được tạo thường là file văn bẳn dạng text rỗng.
  
- `cat`: một lệnh khác cũng được dùng để tạo file text, nhưng bạn sẽ được nhập dữ liệu vào file mới trực tiếp từ Terminal:
  - `cat > tên_tệp`
  - Để kết thúc việc nhập dữ liệu vào file bạn có thể nhấn tổ hợp phím Ctrl + D
  
- `rm`: xóa tệp
  - `rm file1 file2 file3`
  - Lưu ý: Lệnh rm không thể hoàn tác được, do đó để tránh trường hợp xóa nhầm file bạn có thể thêm tham số -i để được thông bảo hỏi trước khi xóa, cú pháp:
  - `rm -i tên_file`
  
- `cp`: (copy) sao chép file cũng như thư mục:
  - Sao chép tệp: `cp <tên_file_gốc> <tên_file_copy>`
  - Sao chép tệp tin đến thư mục: `cp <file_gốc> <thư_muc/đường dẫn thư mục>`
  - Sao chép thư mục đến thư mục: `cp <thư_mục> <thư_muc/đường_dẫn_thư_mục_lưu>`
  
- `mv`: (move) dùng để di chuyển file, thư mục hoặc dùng để đổi tên file
  - `mv file1 file2`: Lệnh này có tác dụng di chuyển file1 đến file2, việc này cũng như đổi tên file1 thành file2 mà thôi.
  - `mv <file> <thư_muc/đường_dẫn_thư_mục_lưu>`: di chuyển file đến đường dẫn hoặc thư mục nhất định
  
- `mkdir`: make directory, tạo thêm một hoặc nhiều thư mục mới: `mkdir thu_muc_1 thu_muc_2`
- `rmdir`: remove directory, xóa bỏ một hoặc nhiều thư mục: `rmdir thu_muc_1 thu_muc_2`
  - Lưu ý khi bạn xóa thư mục nào thì thư mục đó phải trống và bạn phải đang ở cùng vị trí với thư mục đó, nếu bạn đang ở trong thư mục cần xóa hoặc thư mục chứa tệp thì lệnh rmdir không thưc hiện được.

- Xem, đọc tệp trên Terminal:
  - có thể sử dụng: `more tên_tệp`, `less tên_tệp`, `cat tên_tệp` 
  - 3 lệnh trên có một điểm khác nhau ở cách hiển thị tệp khi xem

- `du` kiểm tra dung lượng của từng thư mục hay tập tin, thêm trường -h (human readable) cho phép hiển thị kích thước thư mục dưới dạng đơn vị mà con người dễ đọc như Kilobyte (K), Megabyte, Gigabyte
  - `du -h`: hiện thị dung lượng các thư mục trong thư mực hiện hành
  - `du -h đường_dẫn`: xem dung lượng của một thư mục cụ thể
  - có thể kết hợp các tùy chọn -a (all file và thư mục), -s (file hoặc thư mục cụ thể),.. để hiển hiện theo cách mình muốn
  ```
  du -sh duong_dan
  du -ah duong_dan
  ```
  - VD: Để kiểm tra dung lượng từng loại tệp tin cụ thể, ví dụ mình cần check dung lượng các file *.mp4 trong Videos. Mình dùng cd chuyển đến thư mục Videos (/home/gocinfo/Videos) và nhập lệnh: `du -sh *.mp4`

- `who`: hiện thị về tài khoản người dùng hiện đang đăng nhập vào hệ thống. Để tham khảo thêm nhiều tùy chọn cho lệnh who. Hãy sử dụng lệnh man who trong terminal để xem thêm nữa

- bạn có thể dùng lệnh cat để xem thông tin máy tính bằng cách đọc một file thông tin cấu hình máy tính ở đường dẫn /proc/cpuinfo  bằng lệnh cat như sau:
```
cat /proc/cpuinfo
```

- Khởi động lại máy tính: `shutdown -r` (reboot)
- Tắt máy tính: `shutdown`
- Nhưng thông thường các khi bạn sử dụng 2 lệnh trên, máy tính sẽ không tắt hay khởi động lại ngay mà đợi một tẹo nữa (1 phút sau). Để buộc máy tính tắt ngay hoặc khởi động lại ngay, bạn dùng lệnh:
```
shutdown now
shutdown -r now
```





























