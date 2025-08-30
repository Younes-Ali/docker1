import socket # for network

def sort_numbers(a, b, c):
    numbers = [a, b, c]
    numbers.sort()
    return numbers

if __name__ == "__main__":
    print("Enter 3 numbers to sort:")
    x = int(input("First number: "))
    y = int(input("Second number: "))
    z = int(input("Third number: "))

    result = sort_numbers(x, y, z)
    print("Sorted numbers:", result)

    # port part
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("localhost", 8080))  # make code open in port 8080
    s.listen(1)

    while True:
        client_socket, addr = server_socket.accept()
        print("Connection from:", addr)

        # for web
        response_body = f"Sorted numbers: {sort_numbers(3, 1, 2)}"
        response = f"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n{response_body}"
        client_socket.sendall(response.encode())
        conn, addr = s.accept()    # accepting conection  
        conn.close()               # closing conection
