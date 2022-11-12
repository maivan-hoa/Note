In Python, argparse is one of those modules that can help you write more professional and better-looking Python code. This is because argparse makes it easy to write user-friendly command-line interfaces.
- An ArgumentParser object to hold all the information necessary to parse the command line into Python before setting the parser with the parse_args() method.

```python
parser = argparse.ArgumentParser(description='Process some integers.')
```
- Tham số description được sử dụng để cung cấp thông tin mô tả chương trình của bạn
- Ngoài description thì ArgumentParrser còn một số các tham số khác như sau:
  - prog : Tên của chương trình (Mặc định sys.argv[0], đây thường chính là tên file mà bạn lưu code. )
  - usage: Một chuỗi miêu tả cách sử dụng chương trình
  - formatter_class: Một class để tùy chỉnh phần thông tin trợ giúp
  - add_help : Thêm cờ -h/--help cho chương trình để thiện phần thông tin trợ giúp
  - argument_default: Các tham số mặc định truyền vào

```python
# Chẳng hạn ta có chương trình example.py:

import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))


# Kết quả khi chạy python example.py --help:

usage: prog.py [-h] [--sum] N [N ...]

Process some integers.

positional arguments:
 N           an integer for the accumulator

optional arguments:
 -h, --help  show this help message and exit
 --sum       sum the integers (default: find the max)

```

Chức năng của các tham số:
- 


















