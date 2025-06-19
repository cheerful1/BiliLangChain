import socket

sock = socket.socket()
sock.bind(("127.0.0.1", 8080))
sock.listen(5)

while True:
    conn, addr = sock.accept()  # 阻塞等待客户端连接
    data = conn.recv(1024)
    print("客户端发送的请求信息:\n", data)
    conn.send(b"HTTP/1.1 200 ok\r\n server:yuan \r\n content-type:text/html\r\n\r\n<h1>hello,world</h1>")
    conn.close()
