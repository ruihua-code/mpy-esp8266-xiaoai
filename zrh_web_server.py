import socket
from zrh_storage import write_config
import machine
import gc
import time

text_plain = b'HTTP/1.0 200 OK\r\nContent-type: text/plain;charset=utf-8\r\n\r\n'
text_html = b'HTTP/1.0 200 OK\r\nContent-type: text/html;charset=utf-8\r\n\r\n'
application_json = b'HTTP/1.0 200 OK\r\nContent-type: application/json;charset=utf-8\r\n\r\n'


def parse_query_string(query_string):
    params = query_string.split('&')
    parsed_params = {param.split('=')[0]: param.split('=')[
        1] for param in params}
    return parsed_params


def handle_request(client, ap):
    request = client.recv(4096).decode('utf-8')
    request_lines = request.split('\r\n')

    method, full_path, _ = request_lines[0].split()

    # if api_path != '/setWifi':
    #     client.send(text_plain)
    #     client.send('错误请求')
    #     client.close()
    # 解析路径和查询字符串
    if '?' in full_path:
        path, query_string = full_path.split('?', 1)
        get_params = parse_query_string(query_string)
        # 有参数的请求在这里处理
        if path == '/setWifi':
            write_config(get_params['ssid'], get_params['password'])
            client.send(text_plain)
            client.send('配置成功，正在重启设备')
            client.close()
            time.sleep(3)
            ap.active(False)
            machine.reset()

    else:
        # 无参数的请求在这里处理
        path = full_path
        get_params = {}

    print("GET parameters:", get_params)


# 启动socket TCP Server
def do_socket_start(ap):
    gc.collect()
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.bind(('0.0.0.0', 80))
    my_socket.listen(5)
    while True:
        print("socket running...")
        client_socket, _ = my_socket.accept()
        handle_request(client_socket, ap)
        client_socket.close()
