# Nên chọn git server nào?
- github phổ biến nhất
- gitlab: giao diện tốt - hộ trợ quản lý issue cực thân thiện, có thể cài ở mạng cục bộ sử dụng Docker nhưng chạy hơi chậm vì nó lập trình bằng Ruby On Rails. Nếu có máy chủ mạnh, sao lưu tốt, dùng gitlab rất thích
- bitbucket: là một sản phẩm của Atlassian. Nếu công ty bạn dùng Jira và bộ các công cụ mua của Atlassian, thì bạn dùng Bitbucket cũng được.
- gitea: được viết bằng Golang, chạy cực nhanh, giao diện cũng đơn giản. Nó cũng có giao diện quản lý issue bug đủ dùng. Nếu so sánh với gitlab, gitea đơn giản hơn, ít chức năng phải học, phải mày mò hơn. Team start up dùng gitea rất ổn.

# Đối với lập trình viên sử dụng Visual Studio Code, hãy cài đặt:
- GitGraph: dùng để xem lịch sử commit và các nhánh (branch)
- GitLens: dùng để xem thay đổi giữa các commit

# Hệ thống quản lý version – VCS
Hệ thống quàn lý version là gì? và tại sao chúng ta cần quan tâm và sử dụng nó? Hệ thống quản lý version là một hệ thống lưu lại toàn bộ lịch sử thay đổi của một hoặc nhiều file để chúng ta có thể lấy lại một phiên bản bất kỳ nào đó. Thông thường, chúng ta nghĩ các hệ thống quản lý version dùng để quản lý các file mã nguồn. Tuy nhiên, trong thực thế chúng ta có thể dùng để quản lý version cho bất kỳ định dạng file nào.

Nếu bạn là một nhà thiết kế đồ hoạ hoặc thiếp kế web và mong muốn giữ lại các version của một file ảnh hoặc một thiết kế layout thì việc sử dụng VCS là một lựa chọn sáng suốt. Nó cho phép bản lấy lại được các trạng thái trước đó, so sánh nội dung thay đổi của các trạng thái, hay truy tìm xem ai là người gây ra lỗi lầm khi thay đổi một nội dung nào đó và nhiều việc khác nữa. Tất cả đều được thực hiện một cách dễ dàng với việc sử dụng VCS.

# Ba trạng thái của file trong Git
- Để hiểu rõ cách thức hoạt động của Git thì chúng ta cần chú trọng đến việc hiểu rõ các trạng thái của file trong Git. Nắm rõ được các trạng thái này thì việc tiếp cận Git về sau trở nên thuận lợi hơn rất nhiều. Git có 3 trạng thái của file: `committed`, `staged` và `modified`.
  - `committed` nghĩa là dữ liệu đã được lưu giữ an toàn vào git local database.
  - `staged` nghĩa là chúng ta đã đánh dấu sự thay đổi của dữ liệu và chuẩn bị cho lần commit tiếp theo. (git add)
  - `modified` nghĩa là chúng ta đã thay đổi nội dung của file nhưng chưa được staging hay chưa được commit vào git local database.
  
- Tương ứng với ba trạng thái kể trên, chúng ta sẽ có ba khu vực chính của một dự án Git: `thư mục Git`, `thư mục làm việc`  và `khu vực staging` như hình bên dưới.
  - `Thư mục Git (Git directory)`: là nơi Git lưu giữ toàn bộ dữ liệu dự án. Đây là phần quan trọng nhất của Git, và nó được copy khi bạn thực hiện clone repo dự án từ một máy tính khác về local.
  - `Thư mục làm việc (working tree)`: Là một version riêng lẻ của dự án được checkout từ thư mục Git về một thư mục trên ổ cứng để bạn có thể làm việc và thay đổi trên đó.
  - `Khu vực staging`: Là những file sẽ được đưa vào cho lần commit kế tiếp. Đôi khi được gọi là index, nhưng thường được gọi là khu vực staging.

  --> Code và sửa đổi file trong working tree -> đánh dấu sự thay đổi vào staging -> commit các file được đánh dấu trong stage lưu vào DB

# Git flow
Như vậy, một flow cơ bản của Git sẽ giống như sau:
- Chúng ta thay đổi nội dung của file trên thư mục làm việc
- Sau đó, chúng ta thực hiện staging nội dung thay đổi của file. Đưa snapshot của các file vào khu vực staging dể chuẩn bị cho lần commit tiếp theo.
- Cuối cùng chúng ta thực hiện commit để lưu giữ trạng thái trong khu vực staging vào thư mục Git.

--> git có thêm staging area để cho phép lập trình nhóm những file đang sửa đổi, thêm, xóa ở working directory thành một tập hợp lý để commit. Trong một lần commit, dev không nên và không nhất thiết phải chọn tất cả các file / folder đang thay đổi ở trong working directory mà chỉ chọn nhóm file sửa một lỗi cụ thể, hoàn thành một task nhỏ cụ thể. Sau này khi cần undo sẽ không ảnh hưởng dây truyền đến các mã nguồn không liên đới.

![alt text](https://github.com/maivan-hoa/Note/blob/main/images/1.png?raw=true)













