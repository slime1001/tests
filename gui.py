import requests


def read_txt_lines(file_path):
    lines = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = [line.strip() for line in file.readlines()]
        print(f"成功读取文件: {file_path}")
        print(f"共读取到 {len(lines)} 行内容")
        return lines
    except FileNotFoundError:
        print(f"错误: 文件 '{file_path}' 不存在")
        return False
    except UnicodeDecodeError:
        print(f"错误: 文件 '{file_path}' 编码不是utf-8，请尝试其他编码")
    except Exception as e:
        print(f"读取文件时发生错误: {str(e)}")

    return lines

def start_burp(dic_path,url):
    line = read_txt_lines(dic_path)
    for passwd in line:
        response = requests.get(url+passwd)
        if '' in response.text:
            print("该账号密码为:"+passwd)
            break


if __name__ == "__main__":
    url=''
    dictionary_path = 'D:/PythonProject/tests/testpswd.txt'
    line = read_txt_lines(dictionary_path)
    for pswd in line:
        print(pswd)

