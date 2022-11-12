In Python, `argparse` is one of those modules that can help you write more professional and better-looking Python code. This is because `argparse` makes it easy to write user-friendly command-line interfaces.
- An `ArgumentParser` object to hold all the information necessary to parse the command line into Python before setting the parser with the `parse_args()` method.

```python
parser = argparse.ArgumentParser(description='Process some integers.')
```
- Tham số `description` được sử dụng để cung cấp thông tin mô tả chương trình của bạn
- Ngoài `description` thì `ArgumentParrser` còn một số các tham số khác như sau:
  - `prog` : Tên của chương trình (Mặc định `sys.argv[0]`, đây thường chính là tên file mà bạn lưu code. )
  - `usage`: Một chuỗi miêu tả cách sử dụng chương trình
  - `formatter_class`: Một class để tùy chỉnh phần thông tin trợ giúp
  - `add_help` : Thêm cờ -h/--help cho chương trình để thiện phần thông tin trợ giúp
  - `argument_default`: Các tham số mặc định truyền vào

Ví dụ 1:
```python
import argparse
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-n", "--name", required=True,
	help="name of the user")
args = vars(ap.parse_args())
print("Hi there {}, it's nice to meet you!".format(args["name"]))
```
- we add our only argument, --name . We must specify both shorthand (-n) and longhand versions (--name) where either flag could be used in the command line. This is a required argument as is noted by required=True


Ví dụ 2: ta có chương trình `example.py`:
```python

import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))
```

Kết quả khi chạy `python example.py --help`:
```
usage: prog.py [-h] [--sum] N [N ...]

Process some integers.

positional arguments:
 N           an integer for the accumulator

optional arguments:
 -h, --help  show this help message and exit
 --sum       sum the integers (default: find the max)

```

**Chức năng của các tham số:**
- `metavar`: Tên của tham số khi được ghi trong các phần thông tin trợ giúp (ở trong ví dụ là các đoạn `usage: prog.py [-h] [--sum] N [N ...]` và `positional arguments: N an integer for the accumulator`
- `type` : Kiểu dữ liệu mà tham số truyền vào sẽ được ép thành (ở trong ví dụ là kiểu int)
- `help`: Phần thông tin trợ giúp
- `dest`: Tên của thuộc tính mà sẽ được thêm vào biến được trả về bởi `parse_args()`. `dest` ở trong ví dụ là `accumulate`, và bạn có thể thấy thuộc tính này được gọi sau này.
- `default`: Giá trị mặc định trả về nếu không có đối số/argument được truyền vào từ CLI.
- `const`: Một hằng giá trị, không được truyền vào từ CLI nhưng vẫn được lưu bên trong để 1 số hàm bên trong sử dụng, nhất là hàm `action`

Trong hàm `add_argument`, có 2 tham số đặc biệt cần lưu ý là `nargs` và `action`:
- `action`: Mỗi tham số truyền vào CLI sẽ được lớp `ArgumentParser` đính với 1 `action` , tức là một hành động duy nhất. Tham số này sẽ định nghĩa cách các tham số truyền vào từ CLI được xử lý. Hành động này có nhiều kiểu như sau:
  - `'store'`: hành động này sẽ lưu giá trị truyền vào. Đây là hành động mặc định
  - `'store_const'`: hành động này sẽ lưu trữ giá trị được định nghĩa bởi từ khóa `const`. Như ở ví dụ trên, `const` đang truyền vào hàm `sum`. Biến này thường được dùng với các tham số dạng cờ. Ví dụ:
  ```python
  parser = argparse.ArgumentParser()
  parser.add_argument('--foo', action='store_const', const=42)
  parser.parse_args(['--foo'])
  Namespace(foo=42)
  ```
  - `'store_true'` (`'store_false'`) : đây là dạng đặc biệt của `action 'store_const'`, chuyên dùng để lưu các biến `True` (`False`), và đồng thời tạo các giá trị mặc định `False` (`True`) nếu không được chỉ định.
  - `'count'`: Đếm số lần một keyword argument xảy ra
  - `'extend'`: Lưu 1 list, thêm các tham số truyền vào sau vào list đó.

- `nargs`: Như đã nói ở trên thì mỗi tham số truyền vào CLI sẽ được lớp `ArgumentParser` đính với 1 action. Tham số `nargs` có thể đính một số lượng các tham số khác nhau với 1 action. Các giá trị của `nargs` như sau:
  - '*': Tất cả các tham số truyền vào từ CLI được gom lại vào 1 list
  - '+': Giống như'*'. Nhưng yêu cầu ít nhất một giá trị, sẽ trả ra 1 tin nhắn lỗi nếu không có tham số nào được truyền vào. Đây là giá trị được sử dụng ở ví dụ.
  - 'N': Một số nguyên N các tham số truyền vaò từ CLI sẽ được gom vào một list
  - '?': Sẽ chỉ có 1 tham số truyền vào từ CLI được xử lý. Nếu không có tham số nào thì giá trị từ tham số default sẽ được sử dụng.

Hàm `parse_args()` biến các tham số được gửi vào từ CLI thành các thuộc tính của 1 object và trả về object đó. 

Ví dụ 3:
```python
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')
```
--> Thêm tham số `--sum`, được lưu vào thuộc tính `accumulate`, được dùng để tạo ra 1 hàm trả về tổng của các tham số truyền vào, hoặc nếu không có tham số `--sum` được truyền vào sẽ mặc định trả về giá trị lớn nhất.


# Một số ví dụ và chú ý minh họa

## Ví dụ 4: Nếu ta có đoạn khai báo:
```python
# abbrev_example.py
import argparse

my_parser = argparse.ArgumentParser()
my_parser.add_argument('--input', action='store', type=int, required=True)
my_parser.add_argument('--id', action='store', type=int)

args = my_parser.parse_args()

print(args.input)
```

Ta hoàn toàn có thể gọi thông qua viết tắt: 
```python
$ python abbrev_example.py --input 42
42

$ python abbrev_example.py --inpu 42
42

$ python abbrev_example.py --inp 42
42

$ python abbrev_example.py --in 42
42
```
Tuy nhiên, nếu ta gọi `--i 42` thì sẽ gây ra lỗi, vì chương trình sẽ không biết gán cho input hay id
Nếu muốn người dùng phải nhập argument đầy đủ, không được viết tắt, ta khai báo như sau:
 ```python
 # abbrev_example.py
import argparse

my_parser = argparse.ArgumentParser(allow_abbrev=False)
my_parser.add_argument('--input', action='store', type=int, required=True)

args = my_parser.parse_args()

print(args.input)
 ```

## Chú ý 5: 
- Có hai loại argument là: `Positional arguments` và `Optional argument`, trong đó:
	- `Positional arguments` bắt buộc cần để chương trình hoạt động
	- `Optional argument` không bắt buộc
- Syntactically, the difference between positional and optional arguments is that optional arguments start with - or --, while positional arguments don’t.

## Ví dụ 6:
- Ta có chương trình:
```python
# actions_example.py
import argparse

my_parser = argparse.ArgumentParser()
my_parser.version = '1.0'
my_parser.add_argument('-a', action='store')
my_parser.add_argument('-b', action='store_const', const=42)
my_parser.add_argument('-c', action='store_true')
my_parser.add_argument('-d', action='store_false')
my_parser.add_argument('-e', action='append')
my_parser.add_argument('-f', action='append_const', const=42)
my_parser.add_argument('-g', action='count')
my_parser.add_argument('-i', action='help')
my_parser.add_argument('-j', action='version')

args = my_parser.parse_args()

print(vars(args))
```

- Trong ví dụ trên, nếu không có argument nào được chỉ định, chúng sẽ nhận giá trị `None`, ngoại trừ các argument c và d có action lần lượt là `store_true` và `store_false` sẽ nhận giá trị mặc định là `False` và `True`
```python
$ python actions_example.py
{'a': None, 'b': None, 'c': False, 'd': True, 'e': None, 'f': None, 'g': None}
```

- action `store` chỉ đơn giản lưu giá trị truyền vào mà không xem xét thêm gì
```python
$ python actions_example.py -a 42
{'a': '42', 'b': None, 'c': False, 'd': True, 'e': None, 'f': None, 'g': None}

$ python actions_example.py -a "test"
{'a': 'test', 'b': None, 'c': False, 'd': True, 'e': None, 'f': None, 'g': None}
```

- `store_const` sẽ lấy giá trị được định nghĩa trong const nếu argument được chỉ định
```python
$ python actions_example.py -b
{'a': None, 'b': 42, 'c': False, 'd': True, 'e': None, 'f': None, 'g': None}
```

- `store_true` sẽ lấy giá trị True nếu argument được chỉ định và lấy giá trị Fasle nếu argument không được chỉ định. `store_false` có hành vi ngược lại
```python
$ python actions_example.py
{'a': None, 'b': None, 'c': False, 'd': True, 'e': None, 'f': None, 'g': None}
$ python actions_example.py -c
{'a': None, 'b': None, 'c': True, 'd': True, 'e': None, 'f': None, 'g': None}
$ python actions_example.py -d
{'a': None, 'b': None, 'c': False, 'd': False, 'e': None, 'f': None, 'g': None}
```

- `append` tạo list tất cả giá trị được truyền vào
```python
$ python actions_example.py -e me -e you -e us
{'a': None, 'b': None, 'c': False, 'd': True, 'e': ['me', 'you', 'us'], 'f': None, 'g': None}
```

- `append_const` tương tự như `append`, nhưng luôn append cùng một hằng số
```python
$ python actions_example.py -f -f
{'a': None, 'b': None, 'c': False, 'd': True, 'e': None, 'f': [42, 42], 'g': None}
```

- `count` đếm bao nhiêu lần argument được truyền vào
```python
$ python actions_example.py -ggg
{'a': None, 'b': None, 'c': False, 'd': True, 'e': None, 'f': None, 'g': 3}
$ python actions_example.py -ggggg
{'a': None, 'b': None, 'c': False, 'd': True, 'e': None, 'f': None, 'g': 5}
```

## Ví dụ 7
- Python argparse library creating a domain of allowed values for specific arguments. You can do this by providing a list of accepted values while adding the new option:
```python
# choices_ex.py
import argparse

my_parser = argparse.ArgumentParser()
my_parser.add_argument('-a', action='store', choices=['head', 'tail'])

args = my_parser.parse_args()
```

```python
# choices_ex.py
import argparse

my_parser = argparse.ArgumentParser()
my_parser.add_argument('-a', action='store', type=int, choices=range(1, 5))

args = my_parser.parse_args()

print(vars(args))
```
- In this case, the value provided on the command line will be automatically checked against the range defined:
```python
$ python choices_ex.py -a 4
{'a': 4}

$ python choices_ex.py -a 40
usage: choices_ex.py [-h] [-a {1,2,3,4}]
choices_ex.py: error: argument -a: invalid choice: 40 (choose from 1, 2, 3, 4)
```
--> If the input number is outside the defined range, then you’ll get an error message.


## Ví dụ 8
- `nargs=N`:
```python
# nargs_example.py
import argparse

my_parser = argparse.ArgumentParser()
my_parser.add_argument('--input', action='store', type=int, nargs=3)
my_parser.add_argument('--output', action='store', type=int)

args = my_parser.parse_args()

print(args)
```
```python
$ python nargs_example.py --input 42
usage: nargs_example.py [-h] [--input INPUT INPUT INPUT] [--output OUTPUT]
nargs_example.py: error: argument --input: expected 3 arguments

$ python nargs_example.py --input 42 42 42 --output 0
Namespace(input=[42, 42, 42], output=0)
```


- `nargs='*'`:
```python
# nargs_example.py
import argparse

my_parser = argparse.ArgumentParser()
my_parser.add_argument('--input', action='store', type=int, nargs='*')
my_parser.add_argument('--output', action='store', type=int)

args = my_parser.parse_args()

print(args)
```
```python
$ python nargs_example.py --input 1 2 3 4 5 6 7 --output 0
Namespace(input=[1, 2, 3, 4, 5, 6, 7], output=0)
```
























