import socket

UDP_HOST = 'X.X.X.X'  # Server address
UDP_PORT = 12346            # The UDP server port

# Create a socket for the UDP client
udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send an initial message to the server
udp_client.sendto(b'Clientul UDP s-a conectat!', (UDP_HOST, UDP_PORT))
print("Te-ai conectat ca Client 2. Incepem jocul...")

while True:
    # Wait for the message from the server
    msg, _ = udp_client.recvfrom(1024)
    decoded_msg = msg.decode().strip()

    # Check if the message contains information about the game ending

    # Display the message from the server for the choice
    if "castigat" in decoded_msg.lower() or "remiza" in decoded_msg.lower():
        print(decoded_msg)
        msg, _ = udp_client.recvfrom(1024)
        decoded_msg = msg.decode().strip()

    if "Final:" in decoded_msg:
         print(decoded_msg)
         break

    print(decoded_msg)

    # Enter your choice and send it to the server
    choice = input().strip()
    udp_client.sendto(choice.encode(), (UDP_HOST, UDP_PORT))

    # Wait for the round result from the server
    result_msg, _ = udp_client.recvfrom(1024)
    print(result_msg.decode().strip())

# Close the socket
udp_client.close()
