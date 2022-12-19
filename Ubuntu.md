Ubuntu là một hệ điều hành được phát triển dựa trên Linux kernel. Những hệ điều hành được phát triển dựa trên Linux kernel được gọi chung là Linux distro

Do Ubuntu được phát triển dựa trên Linux kernel, tất cả các Linux commands (cd, mkdir, touch, ls, cat, chmod, chown, …) đều chạy bình thường trên Ubuntu. Ngoài ra, Ubuntu còn có giao diện cho người dùng (GUI - Graphical User Interface) tương tự như 2 hệ điều hành Windows và MacOS, giúp cho những người vốn đã quen với 2 hệ điều hành này có thể dễ dàng thao tác và sử dụng Ubuntu

Do là một Linux distro, Ubuntu cũng tổ chức file và thư mục theo cấu trúc dạng cây:
<!--<div align="center"><img src="https://github.com/maivan-hoa/Note/blob/main/images/ubuntu1.png?raw=true" width="700"></div>-->
<div align="center"><img src="https://github.com/maivan-hoa/Note/blob/main/images/ubuntu2.png?raw=true" width="500"></div> 

Một số thư mục chính:

- `/` (hay computer) - Root - Thư mục gốc (khác với thư mục /root): Mọi file trong hệ thống của ubuntu đều bắt đầu từ nguồn này (đường dẫn bắt đầu bằng '/'). Chứa file hệ thống, các tệp tin cá nhân cũng như link tới các ổ đĩa cứng, mềm. Đại khái là chứa tất cả những thằng ở dưới đây.
- `/bin`: (binary) Các tập tin thực thi của người dùng. Chứa các file là những lệnh của Linux cho cá nhân người sử dụng hoặc cho allusers. Các lệnh có thể lưu ở dạng mã nhị phân hoặc là .sh. Chạy được các command như ls, cd, mkdir, touch, rm, … đều do chúng được nhét ở trong thư mục này
- `/boot`: Chứa các file dùng để khởi động hệ thống (Linux kernel, RAM Disk Image, …)
- `/home`: Thư mục home của người dùng. Mỗi user sẽ được cấp một thư mục riêng bên trong thư mục /home
- `/root`: Thư mục home của super user
- `/sbin`: Các tập tin thực thi của hệ thống. Các lệnh trong file này là các lệnh dùng cho quản trị viên và thường dùng trong config hệ thống. Các lệnh trong file này thường chỉ có thể đường dùng bởi root hoặc superuser
- `/etc` - Các tập tin cấu hình. Cấu hình trong file này thường sẽ ảnh hưởng đến tất cả người dùng trên hệ thống. Thường là config của các chương trình được cài đặt toàn cục.
- `/dev` - Các tập tin thiết bị : Chứa tệp tin thiết bị được cho phép kết nối như usb hay các ổ đĩa cứng khác. Ngoài ra còn có 1 tệp tin đặc biệt là dev/null. Tệp tin này có ý nghĩa là không có gì. Khi ta nói chuyển 1 thư mục vào dev/null ta có thể hiểu là thư mục hay tệp tin sẽ bị xóa đi. Dev/null loại bỏ toàn bộ các dữ liệu ghi vào nó mà vẫn báo cáo là đã ghi thành công. (hay được thấy trong crontab)
- `/proc` - thông tin về tiến trình: Các thông tin về hệ thống được biểu diễn dưới dạng file. Nó cung cấp cách thức cho nhân Linux để gửi và nhận thông tin từ các tiến trình đang chạy trên môi trường Linux.
- `/var` - các tệp tin thay đổi: Chứa các tập tin mà dung lượng lớn dần theo thời gian sử dụng. Bao gồm – Các tập tin ghi chú về hệ thống (/var/log); các gói và các tập tin cơ sở dữ liệu (/var/lib); thư điện tử (/var/mail); hàng đợi in queues (/var/spool); các tập tin khóa (/var/lock); các tập tin tạm được dùng khi khởi động lại (/var/tmp).
- `/tmp` - Chứa các tập tin tạm: Các tập tin tạm của hệ thống và người dùng để tăng tốc cho máy tính. Thường được xóa khi reboot.
- `/lib` - Chứa các thư viện của hệ thống. Thông thường khi cài đặt các gói tin sẽ bao gồm các thư viện cài đặt thêm để hỗ trợ. Khi đó hệ thống sẽ sắp xếp các thư viện này vào cùng 1 chỗ để dễ dàng hơn khi gọi ra.
- `/mnt` - Chứa các thư mục của các ổ cứng hay trong cùng 1 mạng.

Để cài đặt phần mềm trên Ubuntu, các bạn có thể sử dụng Ubuntu Software Center. Cách sử dụng gần như y hệt khi bạn sử dụng App Store hay Google Play để cài ứng dụng di động

Nếu như bạn thích gõ command line trên terminal, các bạn có thể sử dụng lệnh `sudo apt-get install`. Ví dụ, bạn có thể cài đặt Git trên Ubuntu bằng lệnh sau:
```
$ sudo apt-get update
$ sudo apt-get install git
```

- Khi mở Terminal, trên giao diện sẽ xuất hiện:
```
A @ B : C D
```
Ví dụ:
```
root@ubuntu-ssh-njzhg:~#
```
Trong đó:
  - A: tên người dùng đang đăng nhập
  - B: là hostname (Hostname là tên được gán cho thiết bị (được gọi là host) trên mạng và được sử dụng để phân biệt thiết bị này với thiết bị khác trên mạng cụ thể hoặc qua Internet. Để hiểu đơn giản hơn hostname là gì? Bạn hãy hiểu hostnam là 1 cụm ký tự chỉ tên của máy chủ )
  - C: sẽ là ký tự `~` khi bạn đang ở thư mục home của mình, nó sẽ chuyển thành `/` khi bạn ở thư mục gốc (thư mục `/`, không phải `/root`)
  - D: sẽ là ký tự `$` khi bạn đang sử dụng quyền của người dùng bình thường, khi bạn sử dụng quyền của root để cài đặt phần mềm hay thay đổi hệ thống, `$` sẽ đổi thành `#` 



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
  
- `cat`: một lệnh khác cũng được dùng để tạo file text, nhưng bạn sẽ được nhập dữ liệu vào file mới trực tiếp từ Terminal. Lệnh này cũng được sử dụng để xem nội dung file, ghi dữ liệu vào file khác:
  - `cat > tên_tệp`
  - Để kết thúc việc nhập dữ liệu vào file bạn có thể nhấn tổ hợp phím `Ctrl + D`
  - `cat filename.txt`: mở file và hiển thị nội dung cho bạn ngay
  - `cat filename.txt | more`: Để hạn chế cuộc file quá lớn, bạn có thể dùng `| more` để xuất kết quả ít hơn
  - `cat *.txt`: hiển thị nội dung của nhiều hơn một file. Ví dụ, để hiển thị toàn bộ nội dung của file text
  - `cat source.txt > destination.txt`: Thay vì hiển thị nội dung trong một file, bạn còn có thể chuyển hướng kết quả vào một file khác với option `>`. Nếu file đích không có sẵn, lệnh này sẽ tự tạo file đó ra. Hoặc ghi đè lên file có cùng tên.
  - `cat source.txt >> destination.txt`: Để ghi nội dung vào trong cuối file, hãy sử dụng dấu `>>`
  
- `rm`: xóa tệp
  - `rm file1 file2 file3`
  - Lưu ý: Lệnh rm không thể hoàn tác được, do đó để tránh trường hợp xóa nhầm file bạn có thể thêm tham số -i để được thông bảo hỏi trước khi xóa, cú pháp:
  - `rm -i tên_file`
  - `rm your/dir/*.log`: xóa toàn bộ file có đuôi .log
  - `rm /your/dir/*bak*.log`: file chỉ cần chứa _bak_ và là file log thì sẽ bị xóa
  
- `cp`: (copy) sao chép file cũng như thư mục:
  - Sao chép tệp: `cp <tên_file_gốc> <tên_file_copy>`
  - Sao chép tệp tin đến thư mục: `cp <file_gốc> <thư_muc/đường dẫn thư mục>`
  - Sao chép thư mục đến thư mục: `cp <thư_mục> <thư_muc/đường_dẫn_thư_mục_lưu>`
  
- `mv`: (move) dùng để di chuyển file, thư mục hoặc dùng để đổi tên file
  - `mv file1 file2`: Lệnh này có tác dụng di chuyển file1 đến file2, việc này cũng như đổi tên file1 thành file2 mà thôi.
  - `mv <file> <thư_muc/đường_dẫn_thư_mục_lưu>`: di chuyển file đến đường dẫn hoặc thư mục nhất định
  - `mv <file1> <thư_muc/đường_dẫn_thư_mục_lưu> && mv <file2> <thư_muc/đường_dẫn_thư_mục_lưu>`: di chuyển nhiều file
- `mkdir`: make directory, tạo thêm một hoặc nhiều thư mục mới: `mkdir thu_muc_1 thu_muc_2`
  - Thêm option `-p` sẽ tạo thư mục nhiều cấp: `mkdir -p /a/b/c`
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


# Phân quyền trong Ubuntu
## Quản lý người dùng, group
- User chính là người có thể truy cập đến hệ thống. Một User có username và password. Có hai loại User là Super User (hay thường gọi là Root) và Regular User. Mỗi User còn có một mã UID riêng. Mỗi loại User và mỗi User khác nhau có quyền trong hệ thống khác nhau phụ thuộc vào hệ thống đã thiết lập cho họ những quyền gì, Super User đã cấp cho họ những quyền gì.
- Mỗi user có một thư mục home riêng, khi đăng nhập sẽ vào thư mục tương ứng của mình
- Group là nhóm người dùng hệ thống. Mỗi nhóm có tên và mã GID riêng. Các User trong Group có thể có những quyền trong hệ thống khác nhau nhưng có một tập hợp quyền chung trong hệ thống đặc trưng cho Group đó.

- Thêm mới/tạo user: `useradd [option] <username>`, với:
  - -c <Thông tin người dùng>
  - -d <Thư mục cá nhân>
  - -m : Tạo thư mục cá nhân nếu chưa tồn tại
  - -g <nhóm của người dùng>

- Thay đổi thông tin cá nhân của user: `usermod [option] <username>`
- Xóa user: `userdel [option] <username>`
- Đặt mật khẩu cho user: `sudo passwd <username>`
- Các quy định cho password trong file `/etc/login.defs.`
- Khóa user: `passwd -l <username>`
- Mở khóa user: `passwd -u <username>`

- Tạo group: `groupadd <ten_group>`
- Để tạo mới 1 user và thêm luôn vào group ta sử dụng lệnh: `sudo useradd -G <tên_group> <tên_user>`
- Còn nếu muốn thêm 1 user có sẵn vào group sử dụng lệnh: `sudo usermod -a -G <tên_group> <tên_user>`
- Để xóa 1 group ta sử dụng lệnh: `groupdel <tên_group>`


## Phân quyền:
- Có 3 nhóm yêu cầu quyền hạn truy cập là: `Owner`, `Group` và `Other`
- Một file hay một thư mục trong hệ thống có 4 loại quyền hạn chính là `read`, `write`, `excute` và `deny`:
  - Read (r): Đối với một file thì quyền Read chính là quyền được xem nội dung của file, còn đối với một folder thì quyền Read chính là quyền xem được danh sách các subfolder và file bên trong folder đó.
  - Write (w): Đối với một file thì quyền Write là cho phép thêm, sửa nội dùng file, còn đối với một folder thì Write cho phép thêm, xóa một subfolder hay file trong thư mục đó.
  - Execute (x): Đây là quyền thực thi. Đối với một file thì Execute cho phép thực thi file trong trường hợp file này thuộc dạng program hoặc script, còn đối với một folder Execute cho phép cd vào thư mục này.
  - Deny (-): Không có quyền làm một thao tác gì đó đối với một file hay folder xác định.

- Thường sẽ sử dụng 10 bits để thể hiện quyền hạn:
  - Bit 1: thể hiện kiểu file, “d” cho biết đó là thư muc, “-” cho biết đó là 1 file thường.
  - 9 bits còn lại: chia làm 3 nhóm, mỗi nhóm thể hiện quyền hạn cho mỗi loại đối tượng.
    - Ba bít đầu thể hiện quyền của owner - user sở hữu file này
    - Ba bít tiếp theo thể hiện quyền của owner group - group sở hữu file này
    - Ba bit cuối thể hiện quyền của các user khác

- Chỉ có User có quyền root hoặc owner user của file mới có thể thay đổi quyền của file đó. Câu lệnh hay được sử dụng nhất là `chmod`, cú pháp câu lệnh này là: `chmod <option> <opcode> <path_to_file>`, với `option` bao gồm:
  - -v: hiển thị báo cáo sau khi chạy lệnh. Nếu bạn chmod nhiều file/folder cùng lúc thì cứ mỗi lần nó đổi quyền của 1 file/folder xong là sẽ hiện báo cáo.
  - -c: giống như trên, nhưng chỉ hiện khi nó đã làm xong tất cả.
  - -f: Hiểu ngắn gọn là kiểu “kemeno”, nếu có lỗi xảy ra nó cũng không thông báo.
  - -R: nếu bạn CHMOD một folder thì kèm theo -R nghĩa là áp dụng luôn vào các file/folder nằm bên trong nó.
  - --help: hiển thị thông báo trợ giúp.

`opcode` có thể là 3, 4 chữ số hoặc chữ cái như biểu diễn ở hình dưới:

<div align="center"><img src="https://github.com/maivan-hoa/Note/blob/main/images/ubuntu3.png?raw=true" width="800"></div> 

- Giả sử với lệnh: `chmod -R 765 laravel/storage` có nghĩa là:
  - Owner tương ứng với số 7 (như hình vẽ sẽ có đủ 3 quyền đọc, ghi, thực thi) như vậy owner hiện tại có thể làm bất cứ điều gì với thư mục này.
  - Group owner tương ứng với số 6 ( như hình vẽ sẽ có 2 quyền là đọc và ghi) tức là các user thuộc group (group này thường là group hiện tại mà user thực thi câu lệnh đang ở trong, thông thường hay ghi tên user vì khi tạo 1 user thì cũng có 1 group có tên như vậy được tạo ra) có quyền đọc và ghi với thư mục này. (Bạn có thể thay đổi group owner cho thư mục)
  - Cuối cùng là số 5 tương ứng với other (ở đây là tất cả các thằng user hay group khác trong hệ thống) như hình vẽ sẽ có quyền đọc và thực thi.

- Với trường hợp chữ cái: `chmod u+x laravel/storage`
  - tức là thêm quyền excute cho thằng owner của thư mục.


# Một số lệnh hữu ích
1. `nohup`
- Giúp chương trình của bạn vẫn chạy kể cả khi bạn thoát hoặc bị thoát khỏi cửa sổ Shell
- Nohup (viết tắt của từ no hangup) là lệnh bỏ qua tín hiệu HUP. Có thể bạn đang băn khoăn tín hiệu HUP là gì. Cụ thể, nó là tín hiệu được gửi đến một process khi shell được liên kết tới nó bị chấm dứt. Thường thì, khi chúng ta logout, khi đó tất cả các chương trình và process đang chạy sẽ bị treo hoặc bị dừng lại. Nếu chúng ta muốn tiếp tục chạy các process thậm chí cả sau khi đã logout hoặc ngắt kết nối khỏi shell hiện tại, khi đó chúng ta có thể sử dụng lệnh nohup. Nó làm cho các process miễn nhiễm  với tín hiệu HUP để làm cho chương trình luôn chạy thậm chí cả khi bạn đã logout. Với nohup, bạn sẽ không cần phải đăng nhập vào hệ thống trong thời gian dài để chờ process chạy đến khi hoàn tất.

- Nếu bạn muốn giữ cho process chạy liên tục thậm chí cả khi bạn đã thoát khỏi shell, sử dụng lệnh nohup với lệnh chạy process đi kèm như sau:
```
nohup command
```
- Một khi bạn đã chạy lệnh ở trên, tất cả output cùng với thông báo lỗi sẽ được thêm vào file nohup.out trong thư mục home hoặc trong thư mục hiện tại bạn đang đứng để chạy lệnh trên. Bây giờ, nếu shell bị đóng hoặc bạn logout ra khỏi hệ thống, lệnh được thực thi ở trên sẽ không bị chấm dứt.

- Để chạy và đặt process vào chế độ chạy ngầm, bạn cần phải sử dụng lệnh nohup như sau: `nohup command &`
- Ký tự & nói cho shell biết rằng nó cần chạy lệnh ở chế độ chạy ngầm. Tương tự như lệnh nohup ở trên ngoại trừ khi session kết thúc, nó ngay lập tức trả về dấu nhắc shell

- Mặc định, ouput của lệnh nohup được thêm vào file nohup.out. Để chuyển hướng output này tới file khác, sử dụng toán tử chuyển hướng “>” theo sau bởi tên file cụ thể. Ví dụ, bạn sử dụng lệnh dưới đây để lưu output của lệnh nohup tới một file mới có tên “autoscript.log”.
```
nohup python autoscript.py > autoscript.log &
```
- Nếu trong trường hợp bạn không muốn ghi log, bạn có thể sửa lại command thành như sau:
```
nohup command >/dev/null 2>&1   # doesn't create nohup.out
# Example:
nohup python autoscript.py >/dev/null 2>&1
```

- Để chấm dứt một process đang chạy ngầm, sử dụng lệnh kill như sau: `kill -9 PID` hoặc `kill PID`. Bạn sẽ thấy PID của process khi sử dụng nohup với “&”.




