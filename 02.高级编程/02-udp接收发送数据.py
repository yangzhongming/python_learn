import socket

def main():

    # 1.创建套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    # 2. 接收方的地址
    dest_addr = ("192.168.0.93",8080)
    src_addr = ("192.168.0.93",8081)
    udp_socket.bind(src_addr)

    while True:
        # 3. 从键盘获取数据
        send_data = input("请输入要发送的数据：")

        if send_data == "exit":
            break

        # 使用套接字发送
        udp_socket.sendto(send_data.encode('gbk'),dest_addr)

        # 5. 等待接收对方发送的数据
        recv_data = udp_socket.recvfrom(1024)

        # 6. 显示对方发送的数据
        # 接收到的数据recv_data是一个元组
        # 第1个元素是对方发送的数据
        # 第2个元素是对方的ip和端口
        print(recv_data[0].decode('gbk'))
        print(recv_data[1])

    # 关闭套接字
    udp_socket.close()

if __name__ == '__main__':
    main()
