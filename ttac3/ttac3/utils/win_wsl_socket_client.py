import socket

def send_msg(msg):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('127.0.0.1', 50008))
        s.sendall(msg)

        while True: # stay until message accepted
            data = s.recv(1024)
            if (data is not None):
                break

        return repr(data)

if __name__ == '__main__':

    print(send_msg(b"xc = XselController()"))
    print(send_msg(b"xc.open_position_editor()"))
    print(send_msg(b"xc.on_servo_motor()"))
    print(send_msg(b"xc.move_to_x_y_z(100, 100, 50)"))
    print(send_msg(b"xc.move_to_home_position()"))
    print(send_msg(b"close_server"))