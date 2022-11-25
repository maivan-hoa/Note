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

2. Pull docker image từ docker hub:
```
docker pull <image_name:tag>
```
- `image_name`: là tên của docker image trên docker hub và tag là nhãn đánh dấu phiên bản của docker image. Mặt định không điền nhãn thì sẽ download bản `lasted`

3. Liệt kê danh sách các `image` hiện đang có
```
docker images
```
- Cột IMAGE ID chính là index của image và là duy nhất, xóa một image sẽ dựa trên image id

4. Xóa một image
```
docker rmi <image_id>
#or
docker image rm <image_id>
```

5.  Run một docker image
```
docker run --name <container_name> -it --rm -p 8888:8888 -v $PWD:/tmp -w /tmp <image_name>
```
- `container_name`: tên của container sau khi được khởi tạo. Nếu không thiết lập tên thì docker sẽ sinh ra một tên mặc định cho nó.
- `-it`: là lựa chọn bắt buộc khi run docker với interactive process (chẳng hạn shell)
- `--rm`: sẽ xóa container sau khi exit docker
- `-p {host_port}:{container_port}`: tùy chọn mapping port giữa host và container
- `-v {host_directory}:{container_directory}`: là lệnh mount volumn giữa host với container. Trong lệnh trên chúng ta đã mount `current directory` trên host với thư mục `/tmp` của container. Sau khi mount thì dữ liệu giữa hai thư mục sẽ như nhau.
- `-w` thay đổi thư mục làm việc của container về `/tmp`.

6. Liệt kê danh sách các container đang chạy
```
docker container ls
```

7. Xóa một container
```
docker container rm <container_name>
```
- Bình thường nếu chúng ta thêm argument `--rm` vào lệnh docker run thì container sẽ tự động remove sau khi exit. Nếu không thêm lựa chọn này thì container sẽ vẫn tồn tại và chiếm dụng tài nguyên của máy. Khi đó có thể xóa chúng bằng lệnh.
- Trong đó `container_name` chính là cột `NAMES` mà chúng ta thấy ở lệnh docker `container ls`.


# Build docker
## Build một image
- Để build một docker image, chúng ta sử dụng lệnh docker build. Lệnh này sẽ xây dựng image từ Dockerfile và context. Context ở đây được hiểu là tập hợp các tệp nằm trong PATH hoặc URL được chỉ định
- Có rất nhiều cách khác nhau để khởi tạo một docker image như sử dụng DockerFile; thông qua git repository; context đã được đóng gói sẵn trong các file tar.gz, xz, bzip2 gzip hoặc folder.

### Build image từ Dockerfile
- Dockerfile là một file quy định các lệnh cần thiết để docker engine build một image như FROM, COPY, RUN, EXPOSE
```
docker build -t <image_name:tag> .
```
- Dấu `.` là đại diện cho thư mục hiện hành, nơi chứa Dockerfile và các file context để build image
- VD: build một image in ra dòng hello world:
	- Tạo file hello.txt: `echo "hello world" > hello.txt`
	- Tạo file Dockerfile có nội dung:
	```
	from busybox
	copy hello.txt /
	run cat hello.txt
	```
	- Tại cùng thư mục, gõ lệnh build: `docker build -t hello:v1 .`
 
### Build image từ context
- Giả sử file Dockerfile đang nằm trong thư mục dockerfiles và file hello.txt đang nằm trong thư mục context
- Build image từ các file context phân tán:
```
docker build --no-cache -t hello:v2 -f dockerfiles/Dockerfile context
```

## Các lệnh trong file Dockerfile
- `FROM`: Lệnh này thường được sử dụng đầu Dockerfile để khởi tạo một build stage từ base image. Base image được lấy từ Dockerhub - Repository thường là những image có kích thước rất nhẹ và phù hợp với mục đích mà ta cần build.
- `RUN`: Sẽ thực thi các lệnh terminal trong quá trình build image. Có thể có nhiều lệnh `RUN` liên tiếp nhau.
	- Chẳng hạn:
	```
	RUN apt-get update 
	RUN apt-get install -y package-bar package-baz package-foo 
	RUN rm -rf /var/lib/apt/lists/*
	```
	- Một lệnh RUN dài có thể xuống dòng để dễ đọc, dễ hiểu hơn bằng ký hiệu blash `\`:
	```
	RUN apt-get update && apt-get install -y \
	package-bar \
	package-baz \
	package-foo  \
	&& rm -rf /var/lib/apt/lists/*
	```
 - Trong quá trình build một image thì mỗi lệnh RUN trong Dockerfile sẽ build thành một layer. Các layer sẽ giúp caching quá trình build và khi re-build sẽ nhanh hơn vì chỉ phải build lại bắt đầu từ dòng lệnh bị thay đổi và tận dụng các phần trước đó đã được caching.
 - Khi tách một lệnh RUN ghép thành nhiều lệnh RUN đơn, chúng ta sẽ có nhiều layer caching hơn và quá trình build sẽ nhanh hơn. Ví dụ trong 2 cách chạy lệnh RUN để thực hiện cùng một tác vụ như trên thì với cách chạy thứ 2 chúng ta sẽ phải chạy lại toàn bộ lệnh mỗi khi có một trong ba lệnh con thay đổi. Nhưng với cách chạy đầu tiên thì các lệnh sau thay đổi sẽ chỉ phải build lại từ dòng lệnh đó trở đi vì các dòng lệnh trước đã được lấy lại từ caching.

- `LABEL`: Cung cấp thông tin về metadata cho image như tác giả, email, công ty,…
- `EXPOSE`: Thiết lập port để access container sau khi nó khởi chạy.
- `COPY`: Cú pháp chung của lệnh là này là `COPY <src> <dest>`. Lệnh này nhằm copy thư mục từ host (là máy mà chúng ta cài docker image) vào container. Ví dụ trên máy chúng ta có thư mục host_dir. Chúng ta muốn copy vào container tại địa chỉ tuyệt đối /app/.
	- `COPY /host_dir /app/`
	- Note: Nếu chúng ta lấy đường dẫn của `<dest>` là `/folder/` thì đây là đường dẫn tuyệt đối xuất phát từ `root`. Còn nếu chúng ta lấy đường dẫn của `<dest>` là `folder/` thì nó được xem như đường dẫn tương đối bắt đầu từ `<WORK_DIR>/folder/`. Đây là một kiến thức cơ bản nhưng lại là một trong những nguyên nhân gây lỗi khi build.

- `ADD`: `ADD` cũng làm nhiệm vụ tương tự như `COPY` nhưng nó hỗ trợ thêm 2 tính năng nữa là copy từ một link URL trực tiếp vào container và thứ hai là bạn có thể extract một tar file trực tiếp vào container.
- `CMD`: Là câu lệnh được thực thi mặc định trong docker image. `CMD` sẽ không thực thi trong quá trình build image. Một file sẽ chỉ cần một lệnh `CMD` duy nhất. Cấu trúc của `CMD` là `CMD ["executable", "param1", "param2"…]` hoặc `CMD ["param1", "param2"…]`.
	- Chẳng hạn chúng ta muốn khi run docker thì sẽ in ra địa chỉ `$HOME`. Chúng ta có thể thêm dòng lệnh:
	```
	CMD ["echo", "$HOME"]
	```
	- Ở đây `echo` chính là thành phần `executable` và `$HOME` là `param` được truyền vào

- `ENTRYPOINT`: Cung cấp các lệnh mặc định cùng tham số khi thực thi container. Lệnh `CMD` và `ENTRYPOINT` sẽ có chức năng giống nhau, ngoại trừ `ENTRYPOINT` có thể lặp lại nhiều lần trong một Dockerfile trong khi `CMD` là duy nhất.
- `ENV`: Thiết lập các biến environment cho docker image. Giá trị này sẽ tồn tại trong toàn bộ các build stage.
- `VOLUME`: Mount folder từ máy host tới container.
- `WORKDIR`: thay đổi thư mục làm việc hiện hành cho các lệnh thực thi như `RUN`, `CMD`, `ENTRYPOINT`, `COPY`, `ADD` ở phía sau nó. Lệnh này cũng giống như cd trong linux.
- `ONBUILD`: Tạo một trigger như là một điểm chờ cho việc build image. Các lệnh phía sau lệnh `ONBUILD` sẽ không được thực thi cho đến khi image đó được sử dụng làm base image cho việc build một image khác thì các lệnh sau `ONBUILD` sẽ được được thực thi theo tuần tự.
- `ARG`: Định nghĩa một argument được sử dụng trong quá trình `docker build`. Nó tương tự như argument parser trong python.
	- Giả sử ta có:
	 ```
	 from alpine
	 ARG USER
	 RUN echo $USER
	 ```
	Khi chạy docker build: `docker build --build-arg USER=maivanhoa .`
	- `ARG` sẽ không tồn tại trong nhiều `build stage`, do đó ở các stage tiếp theo muốn sử dụng chúng ta phải định nghĩa lại chúng.
	 ```
	 from busybox
	 ARG SETTINGS
	 RUN ./run/setup $SETTINGS

	 # Re-define in next stage
	 FROM busybox
	 ARG SETTINGS
	 RUN ./run/other $SETTINGS
	 ```























