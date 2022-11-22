# Sự ra đời của Containerlization
Nói về sự ra đời của Containerlization - ảo hóa mức container thì chắc phải kể từ những vấn đề mà loài người gặp phải trong giai đoạn đầu của cuộc cách mạng công nghệ.

Khi đó chưa có khái niệm VM hay VPS, mỗi máy chủ là một máy vật lý, đặt trên DC hay nhà riêng nào đó =)). Vấn đề gặp phải ở đây là nó chỉ chạy được một hệ điều hành duy nhất, không tận dụng được hết công suất. Trừ khi có thánh nào tính toán để tận dụng được khoảng 98% tài nguyên hệ thống thì mình không nói, nhưng chắc đa số chúng ta chỉ là người phàm mà thôi :v. Chưa kể quá trình nâng cấp, mở rộng vô cùng phức tạp và mất thời gian cộng với việc tốn thêm cả đống tiền thuê diện tích ở DC nữa. Điều này làm đau đầu các doanh nghiệp khi vừa muốn giảm thiểu chi phí lại vừa muốn nâng cao chất lượng dịch vụ.

--> Và ảo hóa ra đời.

Ảo hóa ra đời cho phép những người quản trị chạy được nhiều hệ điều hành, nhiều máy chủ trên cùng một máy chủ duy nhất. Giúp giảm thiểu chi phí, dễ dàng trong việc triển khai và vận hành. Tận dụng tốt hơn tài nguyên hệ thống. Thay vì trước đây server vật lý 64GB ram chỉ để chạy một dịch vụ web thì giờ đây nó có thể chạy thêm cả dịch vụ mail nữa chẳng hạn

Tuy nhiên ảo hóa vẫn chưa phải là giải pháp tối ưu nhất. Chẳng hạn bạn tạo một máy ảo 5GB RAM thì trên máy vật lý sẽ mất 5GB RAM cho máy ảo đó. Nếu không tận dụng tốt thì đâu đó vẫn có sự lãng phí tài nguyên ở đây.

--> Và ở bước tiến tiếp theo, nhân loại đã nghĩ ra Containerlization.

Containerlization - ảo hóa container . Phương pháp ảo hóa này gần giống với phương pháp ảo hóa trước đó ở trên (đều sinh ra các hệ điều hành con nằm trên cùng một hệ điều hành bố). Nhưng nó tối ưu hơn hơn chỗ , các máy con này cùng sử dụng kernel của máy bố nhưng lại hoàn toàn độc lập với nhau như ảnh phía dưới.
<div align="center"><img src="https://github.com/maivan-hoa/Note/blob/main/images/docker1.png?raw=true" width="500"></div> 



# Docker

Docker là một ứng dụng mã nguồn mở cho phép đóng gói các ứng dụng, các phần mềm phụ thuộc lẫn nhau vào trong cùng một container. Container này sau đó có thể mang đi triển khai trên bất kỳ một hệ thống Linux phổ biến nào. Các container này hoàn toàn độc lập với các container khác.


Docker là một nền tảng để cung cấp cách để building, deploying và running ứng dụng dễ dàng hơn bằng cách sử dụng các containers (trên nền tảng ảo hóa). Ban đầu viết bằng Python, hiện tại đã chuyển sang Golang.
- Docker là một nền tảng mở cho phát triển, vận chuyển và chạy ứng dụng.
- Docker cho phép bạn tách các ứng dụng ra khỏi cơ sở hạ tầng của mình để có thể cung cấp phần mềm một cách nhanh chóng.
- Với Docker, bạn có thể quản lý cơ sở hạ tầng theo cùng cách quản lý ứng dụng của mình.
- Bằng cách tận dụng các phương pháp của Docker để vận chuyển, thử nghiệm và triển khai mã một cách nhanh chóng, bạn có thể làm giảm đáng kể sự chậm trễ giữa việc viết mã và chạy nó trong sản xuất

### Những lợi ích mà Docker đem lại:
- Sử dụng ít tài nguyên: Thay vì phải ảo hóa toàn bộ hệ điều hành thì chỉ cần build và chạy các container độc lập sử dụng chung kernel duy nhất.
- Tính đóng gói và di động: Tất cả các gói dependencies cần thiết đều được đóng gói vừa đủ trong container. Và sau đó có thể mang đi triển khai trên các server khác.
- Cô lập tài nguyên: server bố không biết ở trong container chạy gì và container cũng không cần biết bố nó là CentOs hay Ubuntu. Các container độc lập với nhau và có thể giao tiếp với nhau bằng một interface
- Hỗ trợ phát triển và quản lý ứng dụng nhanh: Đối với Dev, sử dụng docker giúp họ giảm thiểu thời gian setup môi trường, đóng gói được các môi trường giống nhau từ Dev - Staging - Production :v
 - Mã nguồn mở: Cộng đồng support lớn, các tính năng mới được release liên tục.


### Các điểm hạn chế của Docker: Docker không phải là hoàn hảo
- Docker base trên Linux 64bit và các tính năng cgroup, namespaces. Vì thế Linux 32bit hoặc môi trường Window không thể chạy được docker (đối với phiên bản CE).
- Sử dụng container tức là bạn sử dụng chung kernel của hệ điều hành. Trong trường hợp bạn download image có sẵn và trong đó có một số công cụ có thể kiểm soát được kernel thì server của bạn có thể bị mất kiểm soát hoàn toàn.
- Các tiến trình chạy container một khi bị stop thì sẽ mất hoàn toàn dữ liệu nếu không được mount hoặc backup. Điều này có thể sẽ gây ra một số bất tiện… Tuy nhiên Docker nói riêng hay Containerlization nói chung vẫn sẽ là tương lai và là xu hướng chung của hầu hết các doanh nghiệp trên toàn thế giới.

### Các thành phần của Docker:
- Docker cho Mac - cho phép chạy Docker container trên hệ điều hành Mac.
- Docker cho Linux - cho phép chạy Docker container trên hệ điều hành Linux.
- Docker cho Windows - cho phép chạy Docker container trên hệ điều hành Windows.
- Docker Engine - được sử dụng để hình thành Docker images và tạo ra Docker container.
- Docker Hub - đây là Registry được sử dụng để thao tác với các Docker images khác nhau.
- Docker Compose - được sử dụng để định nghĩa các ứng dụng sử dụng multi-Docker container.

### Các khái niệm quan trọng trong Docker:
- `Image` là một gói phần mềm trong đó chứa những thứ cần thiết như thư viện, file cấu hình, biến môi trường để chạy một ứng dụng nào đó. Là một template được đóng gói sẵn và không đổi trong toàn bộ quá trình chạy `container` (trừ khi build lại `image`). Liên tưởng đến lập trình hướng đối tượng, `Image` là class và `container` là object của class đó. Các bạn có thể tự build image cho riêng mình, hoặc download các image có sẵn của cộng đồng từ Docker Hub.
- `Container` khi một phiên bản của `image` chạy, phiên bản chạy đó gọi là `container`, bên trong sẽ có đầy đủ các ứng dụng cần thiết mà bạn định nghĩa từ `Image`
- `Docker Registry` là một kho chứa các image. Bạn có thể dựng riêng một con Docker Registry cho riêng mình. Hoặc up lên Docker Hub để đóng góp ngược lại cho cộng đồng :D
- `Docker Compose`: chạy ứng dụng bằng cách định nghĩa cấu hình các Docker container thông qua tệp cấu hình

Bất ký lúc nào bạn cũng có thể kiểm tra xem có bao nhiêu container đang chạy và nó sinh ra từ image nào.

Bước đầu, để có image nào đó bạn tải về từ https://hub.docker.com/search?q=&type=image, tại đó có đủ các loại phù hợp với công việc của bạn!



# Một số lệnh Docker cơ bản:
 1. Kiểm tra phiên bản Docker:
 ```shell
 docker --version
 ```

hoặc lệnh thông tin chi tiết hơn:
```
docker info
```

2. Kiểm tra các `image` hiện đang có
```
docker images -a
```
















