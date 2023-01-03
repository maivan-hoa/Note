https://towardsdatascience.com/understanding-python-imports-init-py-and-pythonpath-once-and-for-all-4c5249ab6355

`Module`: A single python script.

`Package`: A collection of modules.

- import abc: abc can be a package or a module.
- from abc import xyz: xyz can be a module, subpackage, or object, such as a class or function.

## Absolute Imports
- An absolute import specifies the resource to be imported using its full path from the project’s root folder.
- Example:
```
from package1 import module1
from package1.module2 import function1
from package2 import class1
from package2.subpackage1.module5 import function2
```

## Relative Imports
- A relative import specifies the resource to be imported relative to the current location
- Example:
```
from .some_module import some_class
from ..some_package import some_function
from . import some_class
```
- A single dot means that the module or package referenced is in the same directory as the current location. Two dots mean that it is in the parent directory of the current location—that is, the directory above. Three dots mean that it is in the grandparent directory, and so on. This will probably be familiar to you if you use a Unix-like operating system!

## Import
- Khi sử dụng `import`: giả sử ta `import B` trong file `A.py`, python interpreter sẽ cố gắng tìm kiếm B trong `sys.path`. `sys.path` là một list các đường dẫn đến các thư mục lưu trữ các module và thư viện chuẩn của Python. (standard library imports (Python’s built-in modules), related third party imports (modules that are installed and do not belong to the current application), local application imports (modules that belong to the current application))
- Ta có thể in ra sys.path bắng cách:
```
import sys
print(sys.path)
```
- Ta có thể thấy, phần tử đầu tiên trong mảng `sys.path` là đường dẫn đến thư mục chứa file A.py. (Đầu ra của sys.path luôn chứa thư mục hiện tại ở vị trí index 0. Thư mục hiện tại là **thư mục chứa tập lệnh đang chạy**)

**--> Khi sử dụng import, cả file bị import và file gọi import phải nằm trong cùng một thư mục**

- Giả sử ta có cấu trúc thư mục:
```
--utils
  |  |---__init__.py
  |  |---A.py (trong file này có hàm a())
  |
  example.py
```

- Muốn sử dụng hàm a() trong example.py, ta phải import như sau:
```
import utils.A
res = utils.A.a()
```
- Hoặc để ngắn gọn hơn, ta sử dụng `sys.path.append` trong file example.py

```
import os
import sys
fpath = os.path.join(os.path.dirname(__file__), 'utils')
sys.path.append(fpath)

import A

res = A.a()
```

- sys.path chỉ là một list
- os.path.dirname(__file__) returns the absolute path to the current working directory
- Sử dụng sys.path.append để thêm đường dẫn đến module A cần tìm kiếm

## __init__.py
- Nếu ta có đoạn code trong file example.py
```
import utils

res = utils.A.a()
```
--> đoạn code này sẽ gây ra lỗi bởi interpreter không biết utils là package

- Ta có thể xử lý trường hợp này bằng cách sử dụng file __init__.py với nội dung:
```
from .A import a
```
hoặc
```
from utils.A import a
```
- Sau đó, trong file example.py, ta có thể sử dụng code:
```
import utils

res = utils.a()
```















