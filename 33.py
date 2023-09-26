from re import match
idcard = input()
pattern = r"^[1-9]\d{5}(19|20)\d{2}(0[1-9]|1[0-2])(0[1-9]|[1-2][1-9]|30|31)\d{3}[0-9Xx]$"
if match(pattern,idcard):
    print("合法")
else:
    print("不合法")
