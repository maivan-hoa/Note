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

### Kiến trúc và các thành phần của docker
1. Docker Engine
- Docker Engine là một ứng dụng client-server. Có hai phiên bản Docker Engine phổ biến là:
	- Docker Community Edition (CE): Là phiên bản miễn phí và chủ yếu dựa vào các sản phầm nguồn mở khác.
	- Docker Enterprise: Khi sử dụng phiên bản này bạn sẽ nhận được sự support của nhà phát hành, có thêm các tính năng quản lý và security

- Các thành phần chính của Docker Engine gồm có:
	- Server hay còn được gọi là docker daemon (dockerd): chịu trách nhiệm tạo, quản lý các Docker objects như images, containers, networks, volume.
	- REST API: docker daemon cung cấp các api cho Client sử dụng để thao tác với Docker
	- Client là thành phần đầu cuối cung cấp một tập hợp các câu lệnh sử dụng api để người dùng thao tác với Docker. (Ví dụ docker images, docker ps, docker rmi image v.v..)
	
	<div align="center"><img src="https://github.com/maivan-hoa/Note/blob/main/images/docker2.png?raw=true" width="500"></div> 

2. Kiến trúc của Docker
Docker sử dụng kiến trúc client-server. Docker server (hay còn gọi là daemon) sẽ chịu trách nhiệm build, run, distrubute Docker container. Docker client và Docker server có thể nằm trên cùng một server hoặc khác server. Chúng giao tiếp với nhau thông qua REST API dựa trên UNIX sockets hoặc network interface.
- Docker daemon (dockerd) là thành phần core, lắng nghe API request và quản lý các Docker object. Docker daemon host này cũng có thể giao tiếp được với Docker daemon ở host khác.
- Docker client (docker) là phương thức chính để người dùng thao tác với Docker. Khi người dùng gõ lệnh docker run imageABC tức là người dùng sử dụng CLI và gửi request đến dockerd thông qua api, và sau đó Docker daemon sẽ xử lý tiếp.
- Docker registry là một kho chứa các Image. Nổi tiếng nhất chính là Docker Hub, ngoài ra bạn có thể tự xây dựng một Docker registry cho riêng mình.

<div align="center"><img src="https://github.com/maivan-hoa/Note/blob/main/images/docker3.png?raw=true" width="700"></div> 



# Một số lệnh Docker cơ bản:

- Chú ý: Giả sử ta có hai command:
```
docker run httpd
docker container run httpd
```
Cả hai command trên đều tương tự như nhau. Các bạn có thể chọn một trong hai. Bản thân mình thì thường sử dụng command trên cho nó ngắn gọn.
Vì đâu có sự tương đương này? Là do Docker v1.13 đã tái cấu trúc lại CLI.

- Một số option hay sử dụng trong các command:
	- `-d`: detach container (Có thể hiểu là chạy ngầm container cũng được). Ví dụ nếu không có option này chạy container, cửa sổ dòng lệnh phải giữ phiên. Nếu kết thúc cửa sổ dòng lệnh, container cũng stop theo.
	- `-t`: Tạo một pseudo-TTY. Ví dụ nếu không có option này khi attach lại container thì sẽ không có cửa sổ dòng lệnh. (Nó có nghĩa là console, cho phép kết nối với terminal để tương tác)
	- `-i`: giữ lại một STDIN kể cả khi detach, duy trì mở stdin để nhập lệnh. Ví dụ nếu không có option này khi attach lại container thì khi gõ command sẽ không có kết quả trả về. **Theo khuyến cáo thì nên sử dụng cả 3 option này theo dạng -itd đối với các command như: docker run, docker create …**

- Docker làm việc, tương tác với các thành phần qua ID hoặc NAME

0. Tìm kiếm images
```
docker search <name_image>
```

1. Kiểm tra phiên bản Docker:
 ```shell
 docker --version
 ```

hoặc lệnh thông tin chi tiết hơn:
```
docker info
```


## Các câu lệnh với image
-  Liệt kê danh sách các `image` hiện đang có: `docker images` hoặc `docker image ls`
	- REPOSITORY: là kho chứa của một Image. Image này có thể có nhiều TAG
	- TAG: TAG có thể hiểu là version của Image cũng được
	- IMAGE ID: ID của Image, index của image và là duy nhất, xóa một image sẽ dựa trên image id
	- CREATED: Thời gian tạo Image
	- SIZE: Dung lượng của Image

-  Pull docker image từ Registry (mặc định là docker hub): `docker pull <image_name:tag>`
	- `image_name`: là tên của docker image trên docker hub và tag là nhãn đánh dấu phiên bản của docker image. Mặt định không điền nhãn thì sẽ download bản `lasted`

- Hiển thị chi tiết của một image: `docker inspect <image_name>`
- Hiển thị lịch sử của image: `docker image history <image_name>:<tag>`
- Tạo một tag mới từ image đang có: `docker image tag <image_name>:<tag1> <image_name>:<tag2>`
- Nếu muốn copy image ra máy khác ngoài cách đưa lên repository có thể lưu ra file .tar (file này sẽ bao gồm các Layer sử dụng để tạo image đó, các file data dạng .json …), lệnh sau lưu image có tên myimage ra file: `docker save --output myimage.tar myimage` hoặc `docker image save -o /opt/my_image_file.tar <image_name>`
- Tạo lại image bằng việc load lại file tar: `docker image load -i my_image_file.tar` or `docker load -i myimage.tar`

- Xóa một image: `docker rmi <image_id>` or `docker image rm <image_id>`
- Đổi tên một image đang có: `docker tag image_id imagename:version`
- trong quá trình Docker build image mới từ Dockerfile, có thể tạo ra các image tạm thời gây rác hệ thống. Để xóa các image tạm này hãy dùng lệnh: `docker image prune`

## Các câu lệnh với container
- Tạo mới một container nhưng không start
```
docker create [OPTION] <image_name>
```
Ví dụ: `docker create -itd centos`

-  Tạo một container và start container đó luôn
	```
	docker run --name <container_name> -it --rm -p 8888:80 -v $PWD:/tmp -w /tmp <image_name>
	```
	- `container_name`: tên của container sau khi được khởi tạo. Nếu không thiết lập tên thì docker sẽ sinh ra một tên mặc định cho nó.
	- `-it`: là lựa chọn bắt buộc khi run docker với interactive process (chẳng hạn shell)
	- `--rm`: sẽ xóa container sau khi exit docker
	- `-p {host_port}:{container_port}`: tùy chọn ánh xạ port giữa host và container. Giả sử trong image này chỉ định khi thiết lập container, container sẽ thực hiện lắng nghe ở cổng 80. Ta cần ánh xạ cổng này tương ứng với một cổng trong HOST, ta có thể để cổng tương ứng của HOST là 80 hoặc 8888 như ví dụ trên
	- `-v {host_directory}:{container_directory}`: là lệnh mount volumn giữa host với container. Trong lệnh trên chúng ta đã mount `current directory` trên host với thư mục `/tmp` của container. Sau khi mount thì dữ liệu giữa hai thư mục sẽ như nhau.
	- `-w` thay đổi thư mục làm việc của container về `/tmp`.
	- Khi chạy container nếu Image không có sẵn trong Docker host thì Docker sẽ tự động tải từ Registry về Docker host trước (tag mặc định là lastest).

- Liệt kê danh sách các container đang được Docker quản lý
	- Danh sách các container đang chạy: `docker container ls` or `docker ps`
	- Danh sách tất cả các container: `docker ps -a`
		- CONTAINER ID một con số (mã hash) gán cho container, bạn dùng mã này để quản lý container này, như xóa bỏ, khởi động, dừng lại ...
		- IMAGE cho biết container sinh ra từ image nào.
		- COMMAND cho biết lệnh, ứng dụng chạy khi container chạy (/bin/bash là terminate)
		- STATUS cho biết trạng thái, (exit - đang dừng)
	
-  Xóa một container
	- Xóa container đã stop: `docker rm <container_name>`
		- Bình thường nếu chúng ta thêm argument `--rm` vào lệnh docker run thì container sẽ tự động remove sau khi exit. Nếu không thêm lựa chọn này thì container sẽ vẫn tồn tại và chiếm dụng tài nguyên của máy. Khi đó có thể xóa chúng bằng lệnh.
		- Trong đó `container_name` chính là cột `NAMES` mà chúng ta thấy ở lệnh `docker ps`.

	- Xóa container chưa stop (container đang chạy): `docker rm -f <container_name>`
	- Xóa tất cả container đang stop: `docker prune`
	- Xóa tất cả các container: `docker rm -f $(docker ps -aq)`

- Start một container: `docker start <container_name>`
- Stop một container: `docker stop <container_name>`
- Restart container: `dockert restart <container_name>`
- Pause (tạm dừng container): `docker pause <container_name>`
- Kill container (kill ở đây giống như stop, container chỉ bị stop chứ không bị mất đi): `docker kill <container_name>`
- Hiển thị thông tin chi tiết của container: `docker inspect <container_name>`
- Hiển thị log của container: `docker logs <container_name>`
- Hiển thị tài nguyên đang sử dụng của container: `docker stats <container_name>`
- Hiển thị các tiến trình đang chạy trong container: `docker top <container_name>`
- Hiển thị các port mapping hoặc một port mapping cụ thể: `docker port <container_name>`
- Attach container: Attach một màn hình cho phép nhập input và hiển thị output đối với một container đang chạy (quay quay trở lại terminal của container): `docker attach <container_name>`
- Thực thi một câu lệnh trong container đang chạy (chạy lệnh bên ngoài máy host, không phải trong terminal của container): `docker exec [OPTIONS] CONTAINER COMMAND [ARG...]`
- Đổi tên container: `docker rename <old_name> <new_name>`
- Thoát terminal nhưng vẫn giữ container chạy: `CTRL + P,Q`
- Thoát terminal và dừng container: `gõ lệnh exit`

- Một Image bạn có thể sinh ra các Container, mỗi Container là bản thực thi của Image, khi sử dụng Container bạn có thể cấu hình, cài đặt thêm vào nó các package, đưa thêm dữ liệu ... Đến một lúc, bạn muốn lưu những thay đổi này và ghi lại thành một Image để sau này bạn sinh ra các Container khác bản thân nó đã chữa những thay đổi bạn đã lưu. Giả sử bạn có một container có tên (hoặc id) là mycontainer nếu muốn lưu thành image thực hiện lệnh: `docker commit mycontainer myimage:version`
	- Trong đó myimage và version là tên và phiên bản do bạn đặt. Nếu lưu cùng tên với image tạo ra container này, coi như image cũ được cập nhật mới.
	- Để lưu container lại thành image: trước tiên nếu container đang chạy thì cho dừng lại: `docker stop mycontainer`

# Build docker
## Build một image
- Để build một docker image, chúng ta sử dụng lệnh docker build. Lệnh này sẽ xây dựng image từ Dockerfile và context. Context ở đây được hiểu là tập hợp các tệp nằm trong PATH hoặc URL được chỉ định
- Có rất nhiều cách khác nhau để khởi tạo một docker image như sử dụng DockerFile; thông qua git repository; context đã được đóng gói sẵn trong các file tar.gz, xz, bzip2 gzip hoặc folder.

### Build image từ Dockerfile
- Dockerfile là một file dạng text không có extension, và tên bắt buộc phải là Dockerfile
- Dockerfile là một file kịch bản sử dụng để tạo mới một image, quy định các lệnh cần thiết để docker engine build một image như FROM, COPY, RUN, EXPOSE
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
- `FROM`: Lệnh này thường được sử dụng đầu Dockerfile để khởi tạo một build stage từ base image. Base image được lấy từ Dockerhub - Repository thường là những image có kích thước rất nhẹ và phù hợp với mục đích mà ta cần build. Để xây dựng image từ image cơ sở nào đó thì bạn cần đọc document của Image đó để biết trong đó đang chứa gì, có thể chạy các lệnh gì trong đó ... Ví dụ, nếu bạn chọn xây dựng từ image centos:laste thì bạn bắt đầu bằng hệ điều hành CentOS và bạn có thể cài đặt, cập nhật các gói với yum, ngược lại nếu bạn chọn ubuntu:latest thì trình quản lý gói của nó là APT ...
- `RUN`: thực hiện một câu lệnh Linux. Tùy vào image gốc mà có các câu lệnh tương ứng. Sẽ thực thi các lệnh terminal trong quá trình build image. Có thể có nhiều lệnh `RUN` liên tiếp nhau.
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

- `LABEL`: Cung cấp thông tin về metadata cho image như tác giả, email, công ty,…. Để xem được các label này sử dụng câu lệnh `docker inspect <IMAGE ID>`
- `MAINTERNER`: là author (tác giả) build image đó
- `EXPOSE`: thiết lập cổng mà container lắng nghe, cho phép các container khác trên cùng mạng liên lạc qua cổng này hoặc để ánh xạ cổng host vào cổng này.. (chỉ định các port sẽ Listen trong container khi khởi chạy container từ image)
- `COPY`: Cú pháp chung của lệnh là này là `COPY <src> <dest>`. Lệnh này nhằm copy thư mục từ host (là máy mà chúng ta cài docker image) vào image trong quá trình build image. Ví dụ trên máy chúng ta có thư mục host_dir. Chúng ta muốn copy vào image tại địa chỉ tuyệt đối /app/.
	- `COPY /host_dir /app/`
	- Note: Nếu chúng ta lấy đường dẫn của `<dest>` là `/folder/` thì đây là đường dẫn tuyệt đối xuất phát từ `root`. Còn nếu chúng ta lấy đường dẫn của `<dest>` là `folder/` thì nó được xem như đường dẫn tương đối bắt đầu từ `<WORK_DIR>/folder/`. Đây là một kiến thức cơ bản nhưng lại là một trong những nguyên nhân gây lỗi khi build.

- `ADD`: `ADD` cũng làm nhiệm vụ tương tự như `COPY` nhưng nó hỗ trợ thêm 2 tính năng nữa là copy từ một link URL trực tiếp vào container và thứ hai là bạn có thể extract một tar file trực tiếp vào container.
- `CMD`: Là câu lệnh được thực thi mặc định trong docker image. `CMD` sẽ không thực thi trong quá trình build image. Dùng để chạy lệnh Linux khi khởi tạo container từ image. Một file sẽ chỉ cần một lệnh `CMD` duy nhất. Cấu trúc của `CMD` là `CMD ["executable", "param1", "param2"…]` hoặc `CMD ["param1", "param2"…]`.
	- Chẳng hạn chúng ta muốn khi run docker thì sẽ in ra địa chỉ `$HOME`. Chúng ta có thể thêm dòng lệnh:
	```
	CMD ["echo", "$HOME"]
	```
	- Ở đây `echo` chính là thành phần `executable` và `$HOME` là `param` được truyền vào

- `ENTRYPOINT`: Cung cấp các lệnh mặc định cùng tham số khi thực thi container. Lệnh `CMD` và `ENTRYPOINT` sẽ có chức năng giống nhau, ngoại trừ `ENTRYPOINT` có thể lặp lại nhiều lần trong một Dockerfile trong khi `CMD` là duy nhất.
- `ENV`: Thiết lập các biến environment cho docker image. Giá trị này sẽ tồn tại trong toàn bộ các build stage.
	```
	ENV source /var/www/html/
	COPY index.html ${source}
	```
	- `ENV` chỉ có thể được sử dụng trong các command sau: ADD, COPY, ENV, EXPOSE, FROM, LABEL, STOPSIGNAL, USER, VOLUME, WORKDIR
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

# Ví dụ minh họa
## Tạo images httpd với Dockerfile
- Tạo folder làm việc với Dockerfile
```
cd ~
mkdir build_image && cd build_image
```
- Tạo Dockerfile: `touch Dockerfile` 
	> Filename phải là Dockerfile và không có phần mở rộng)
	- Nội dung của Dockerfile như sau:
	```
	FROM centos:centos7

	LABEL "image-type"="hoa-mv"
	MAINTAINER hoamvm
	
	RUN yum update -y
	RUN yum install httpd -y

	ENV source /var/www/html/

	VOLUME ["/var/log/httpd"]

	COPY index.html ${source}
	COPY start.sh /start.sh

	RUN chmod +x /start.sh
	CMD ["/start.sh"]

	EXPOSE 80
	```
	- Giải thích:
		- FROM centos:centos7: Build image dựa trên image gốc là centos 7.
		- LABEL “image-type”=”huy-test”: Metadata của image có thể có hoặc không.
		- MAINTAINER huytm: Tác giả viết Dockerfile để build image có thể có hoặc không.
		- RUN yum update -y và RUN yum install httpd -y: Thực hiện các command của centos để update và cài đặt httpd
		- ENV source /var/www/html/ : Khai báo một biến môi trường tên là source và có giá trị là /var/www/html/. Biến này sẽ được sử dụng ở bước COPY index.html ${source}
		- VOLUME [“/var/log/httpd”]: Chỉ định một phân vùng trên Docker host mount với container khi chạy. Ở đây mình mount theo dạng volume. Mount folder /var/log/httpd của container với volume nằm tại /var/lib/portal/volume/ của Docker host
		- COPY index.html ${source}: Copy file index.html từ Dockerhost vào đường dẫn biến - được khai báo ở bước trên.
		- COPY start.sh /start.sh: Copy một bash script file vào đường dẫn / để thực hiện một số Linux command khi khởi tạo container từ image này.
		- RUN chmod +x /start.sh: Cho phép quyền thực thi đối với script vừa copy từ bước trên.
		- CMD [“/start.sh”]: Thực thi script khi khởi chạy container từ image này.
		- EXPOSE 80: Chỉ ra rằng container khi khởi chạy từ image này sẽ LISTEN port 80	
	```
# --> CHÚ Ý: Giảm số lượng layer hình thành nên Image
- Giả sử ta tạo image từ Dockerfile:
```
# xây dựng image mới từ image centos:latest (CENTOS 7)
FROM centos:latest

# Cập nhật các gói và cài vào đó HTTPD, HTOP, VIM
RUN yum update -y
RUN yum install httpd httpd-tools -y
RUN yum install epel-release -y \
    && yum update -y \
    && yum install htop -y \
    && yum install vim -y

#Thiết lập thư mục hiện tại
WORKDIR /var/www/html
# Copy tất cả các file trong thư mục hiện tại (.)  vào WORKDIR
ADD . /var/www/html

#Thiết lập khi tạo container từ image sẽ mở cổng 80
# ở mạng mà container nối vào
EXPOSE 80

# Khi chạy container tự động chạy ngay httpd
ENTRYPOINT ["/usr/sbin/httpd"]

#chạy terminate
CMD ["-D", "FOREGROUND"]
```

- Khi hoàn thành build image bằng lệnh `docker build -t i-firstserver:version1 -f Dockerfile .`, ta kiểm tra các image có trong hệ thống bằng lệnh `docker images -a`, ta thu được:
```
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
i-firstserver       version1            6a964f7f5321        About an hour ago   588MB
<noned>             <none>              6a655bf3192b        About an hour ago   588MB
<none>              <none>              bb535a125b19        About an hour ago   588MB
<none>              <none>              e43cbe953b7d        About an hour ago   588MB
<none>              <none>              5f8bda4bcb01        About an hour ago   588MB
<none>              <none>              6d8ae47da227        About an hour ago   588MB
<none>              <none>              bc535a902e02        About an hour ago   411MB
<none>              <none>              ac7b46806e10        About an hour ago   296MB
```
- Như đã thấy, để có image cuối cùng thì Docker cũng đã sinh ra tới 7 image khác, image đầu tiên ac7b46806e10 được kế thừa bới bc535a902e02 cứ như vậy đến cho đến image cuối i-firstserver. Do tính kế thừa, như vậy nên các image cha không thể xóa được hoặc nếu vẫn muốn loại bỏ thì bạn có thể xuất image cuối ra file, rồi xóa image này đi, sau đó nạp image lại từ file. Tuy nhiên một mẹo nhỏ có thể gộp các lớp cha của vào thành một.

- Cố gắng xây dựng Image có ít layer nhất:
	- Gõ lệnh xem lịch sử hình thành image `i-firstserver:version1`:
	```
	IMAGE               CREATED             CREATED BY                                      SIZE                COMMENT
	6a964f7f5321        About an hour ago   /bin/sh -c #(nop)  CMD ["-D" "FOREGROUND"]      0B
	e43cbe953b7d        About an hour ago   /bin/sh -c #(nop)  ENTRYPOINT ["/usr/sbin/ht…   0B
	bb535a125b19        About an hour ago   /bin/sh -c #(nop)  EXPOSE 80                    0B
	6a655bf3192b        About an hour ago   /bin/sh -c #(nop) ADD dir:519c5971b42e7e73b1…   1.49kB
	5f8bda4bcb01        About an hour ago   /bin/sh -c #(nop) WORKDIR /var/www/html         0B
	6d8ae47da227        About an hour ago   /bin/sh -c yum install epel-release -y     &…   177MB
	bc535a902e02        About an hour ago   /bin/sh -c yum install httpd httpd-tools -y     116MB
	ac7b46806e10        About an hour ago   /bin/sh -c yum update -y                        94MB
	9f38484d220f        13 days ago         /bin/sh -c #(nop)  CMD ["/bin/bash"]            0B
	```
	- Hãy nhìn từ dưới lên trên, đó là quá trình hình thành nên Image khi bạn build từ Docker file:
		- Đầu tiên nó tải centos:latest về và chạy nó, lưu thành image 9f38484d220f
		- Tiếp theo chạy lệnh yum update -y cập nhật các package, xong lưu thành image với id ac7b46806e10
		- Cứ như vậy, sau các chỉ thị trong Dockerfile thì một Image lại được lưu lại cho đến Image cuối cùng có tên bạn tạo!
	- Từ đó bạn nhận thấy: Trong Dockerfile có bao nhiêu chỉ thị RUN thì có bấy nhiêu layer được tạo ra, tương tự là ADD, ENTRYPOINT, CMD ... Nên muốn ít layer thì cần viết sao cho ít chỉ thị nhất. Ở ví dụ trên:
		- thay vì có 3 chỉ thị RUN có thể viết thành 1 như vậy 3 layer chỉ còn 1
		- WORKDIR chưa dùng đến bỏ đi (giảm 1 layer)
		- Tham số ENTRYPOINT có thể viết gộp cùng lệnh CMD, thay vì phải dùng thêm CMD (giảm 1 layer).
		```
		FROM centos:latest

		RUN yum update -y \
		    && yum install httpd httpd-tools -y \
		    && yum install epel-release -y \
		    && yum update -y \
		    && yum install htop -y \
		    && yum install vim -y

		ADD . /var/www/html

		EXPOSE 80

		ENTRYPOINT ["/usr/sbin/httpd", "-D", "FOREGROUND"]
		```
		
		- Cuối cùng file Dockerile ở trên vẫn cùng kết quả nhưng sinh ra ít layer. Dù vậy, vẫn còn 3 Image không tên, không tag.

# Chia sẻ dữ liệu giữa Docker Host và Container
Máy Host là hệ thống bạn đang chạy Docker Engine. Một thư mục của máy Host có thể chia sẻ để các Container đọc, lưu dữ liệu

### Chia sẻ dữ liệu giữa Host và Container
Thông tin:
- Thư mục cần chia sẻ dữ liệu trên máy host là: `path_in_host`
- Khi chạy container, thư mục đó được mount - ánh xạ tới `path_in_container` của container
- Để có kết quả đó, tạo / chạy container với tham số thêm vào `-v path_to_data:path_in_container`
- Ví dụ:
```
docker run -it -v /home/sitesdata:/home/data ubuntu
```
- `ubuntu` ở ví dụ trên là tên của image
- Lúc này, dữ liệu trên thư mục `/home/sitesdata/` của máy Host thì trong container có thể truy cập, cập nhật sửa đổi ... thông qua đường dẫn `/home/data`
- Xóa container thì thư mục `/home/sitesdata/` vẫn tồn tại trên máy Host
- 
### Chia sẻ dữ liệu giữa các Container
- Giả sử ta đã tạo một container có tên là `container_first` từ image centOS, trong đó dữ liệu trên thư mục `/home/sitesdata/` của máy Host thì trong `container_first` có thể truy cập, cập nhật sửa đổi ... thông qua đường dẫn `/home/data`
- Ta muốn tạo một container khác có tên `container_second` từ image ubuntu với điều kiện `container_second` này cũng có thể mout tới thư mục `/home/sitesdata/` thông qua đường dẫn `/home/data` như `container_first`, ta dùng lệnh sau:
```
docker run -it --name container_second --volumes-from container_first ubuntu
```

### Quản lý các ổ đĩa với docker volume
- Phần này xem video sẽ dể hiểu hơn: `https://youtu.be/DSP2-ip38Zw?t=423`


# Docker Compose
-  Docker compose sẽ giúp bạn làm việc với Docker một cách hiệu quả hơn, đơn giản hóa các thao tác
- Để dễ hình dùng thì chẳng bạn ứng dụng của bạn đang cần tạo docker cho DB, backend và frontend. Với Dockerfile, bạn sẽ có thể tạo được 1 container chứa tất cả mọi thứ vào trong đó. Tuy nhiên, việc nhét quá nhiều thứ vào Dockerfile sẽ gây ra nhiều vấn đề trong việc build image nếu bạn cần chỉnh sửa (tăng thời gian build chẳng hạn). Ngoài ra, một Dockerfile đảm nhận nhiều nhiệm vụ thì hoàn toàn không tốt chút nào với các principle KISS, SRP. Nếu bạn tách nó ra thành các Dockerfile riêng biệt để tránh các vấn đề trên thì việc chạy từng Dockerfile một cũng không thích hợp nếu như đó là hàng chục hoặc hàng trăm image. Ngoài ra, nếu bạn có một container cần dùng chung (chẳng hạn như DB) hay đơn giản là có thể hoạt động với mọi môi trường như dev, test, prod... thì Dockerfile không hề dễ để thực hiện.
- Những tính năng chính của Compose bao gồm:
	- Thiết lập và cấu hình đa môi trường container hoàn toàn độc lập nhau trên cùng một máy chủ
	- Bảo lưu các phân vùng bộ nhớ khi container được tạo ra
	- Chỉ tạo lại container nào có config thay đổi trong khi vẫn bảo lưu dữ liệu của container
	- Cho phép định nghĩa các biến variables trong file YAML để tùy chỉnh cho các môi trường dev và product.

- Với Compose, bạn sử dụng tệp YAML để định cấu hình các dịch vụ của ứng dụng. Sau đó, với một lệnh duy nhất, bạn tạo và khởi động tất cả các dịch vụ từ cấu hình của mình. Để sử dụng Compose thông thường có ba bước sau:
	- Tạo Dockerfile cho mỗi môi trường container của từng service mình muốn. Dockerfile là bắt buộc để khởi tạo container.
	- Tạo file docker-compose.yml để định nghĩa mối liên kết giữa các containers với nhau.
	- Chạy lệnh docker-compose up để khởi động Compose và chạy toàn bộ ứng dụng.

- Để có thể dùng được docker compose, bạn cần tạo một compose file như docker-compose.yml để thiết lập các container cần cho ứng dụng của bạn
- Để build, run và stop các container, các bạn có thể sử dụng các command sau:
	- `docker-compose build` dùng để build tất cả container được định nghĩa trong compose file. Tuy nhiên, mình hay sử dụng lệnh này để thực hiện build lại service vừa được thay đổi bằng lệnh sau `docker-compose build <servicename>`
	- `docker-compose up` thực hiện tạo và khởi chạy các container. Các bạn có thể xem [ở đây](https://docs.docker.com/engine/reference/commandline/compose_up/) để thêm các options tương ứng với lệnh up. Về cơ bản thì bạn chỉ cần 2 option là `-d` và `--force-recreate`:
		- Với `-d` thì các containers sẽ được chạy dưới dạng background. Detached mode chắc hẳn là không thể thiếu khi khởi chạy bất cứ service nào.
		- Với `--force-recreate` thì bạn sẽ tái tạo lại các containers.
		- Còn nếu chỉ muốn `up` một số services thì các bạn cứ đặt các service muốn chạy đằng sau lệnh `up` là được. Ví dụ như `docker-compose up -d redis sqlserver`
	- `docker-compose down` dùng để dừng các container và xóa hết những gì được tạo từ lệnh `up`. Về cơ bản thì nó sẽ xóa bỏ những container và network được định nghĩa trong compose file.

- Thực thi các lệnh bên trong một dịch vụ đang chạy trong Docker Compose: `docker-compose exec <service name> <command>`. (Không giống lệnh `container exec`, bạn không cần truyền cờ `-it` cho các phiên tương tác, `docker-compose` làm điều đó tự động)

## Example: Cấu trúc cơ bản của file YML trong Compose.
- Giả sử ta có cấu trúc project:
```
app/
   commander/
      Dockerfile
   docker-compose.yml
```
- Bên trong folder `commander` ta có một file Dockerfile như sau để khởi tạo một container chạy redis commander, đây là một service dùng để visualize redis database. Nội dung của Dockerfile:
```
# create a nodejs container with minimum requirements
FROM node:0.12.2

# download and install redis-commander
RUN curl -L https://github.com/joeferner/redis-commander/tarball/v0.3.2 | tar zx
RUN npm install -g redis-commander

# Run this command everytime this container start up
ENTRYPOINT [ "redis-commander" ]
CMD [ "--redis-host", "redis" ]

EXPOSE 8081
```

- Nội dung của Docker-compose.yml:
```
version: '3'
services: 
  backend:
    image: "redis:3"
    restart: always

  frontend: 
    build: commander
    links: 
    - backend:redis  
    ports: 
    - 8081:8081 
    restart: always
```

- File `Compose` trên đây xác định việc khởi tạo 2 services: `backend` và `frontend`.
	- Backend service sử dụng public Redis image từ Docker Hub registry
	- Frontend service:
		- Sử dụng image của `redis-commander` đã được đĩnh nghĩa trong folder `commander`
		- Links với backend service bằng alias redis
		- Kết nối cổng 8081 trên container với cổng 8081 của máy chủ.

- Tiếp theo ta build và run app với Compose bằng lệnh: `docker-compose up`. Câu lệnh `docker-compose up` chính là gộp của hai lệnh sau:
```
$ docker build -t commander commander
$ docker run -d --name frontend -p 8081:8081 --link backend:redis commander
```
- Như vậy, với mỗi service mới được thêm vào hoặc chỉnh sửa, ngoài việc tạo Dockerfile cho service thì chỉ cần thêm vào trong docker-compose.yml, service mới sẽ được liên kết dễ dàng với database/service hiện tại.
- Để kết thúc các services đang chạy, sử dụng lệnh: `docker-compose stop`
- Và để xóa hoàn toàn container và data volume sử dụng bởi Redis container: `docker-compose down --volumes`


















