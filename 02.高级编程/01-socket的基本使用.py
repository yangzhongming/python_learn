import socket

def main():
    # 1. 创建udp套接字
    # Address Family：可以选择 AF_INET（用于 Internet 进程间通信） 或者 AF_UNIX（用于同一台机器进程间通信）,实际工作中常用AF_INET
    # Type：套接字类型，可以是 SOCK_STREAM（流式套接字，主要用于 TCP 协议）或者 SOCK_DGRAM（数据报套接字，主要用于 UDP 协议）
    udp_socket = socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2. 准备接收方的地址
    dest_addr = ('192.168.0.93', 8080)

    # 3. 从键盘获取数据
    send_data = input("请输入要发送的数据:")

    # 4. 发送数据到指定的电脑上
    udp_socket.sendto(send_data.encode('utf-8'), dest_addr)

    # 5. 等待接收对方发送的数据
    recv_data = udp_socket.recvfrom(1024)  # 1024表示本次接收的最大字节数

    # 6. 显示对方发送的数据
    # 接收到的数据recv_data是一个元组
    # 第1个元素是对方发送的数据
    # 第2个元素是对方的ip和端口
    print(recv_data[0].decode('gbk'))
    print(recv_data[1])

    # 7. 关闭套接字
    udp_socket.close()

if __name__ == '__main__':
    main()
