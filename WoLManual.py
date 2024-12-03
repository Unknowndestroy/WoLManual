from wakeonlan import send_magic_packet

# Get the info from user
mac_address = input("Input the MAC Address of Device that will Open: ")
ip_address = input("Input the IP Address of Device that will Open: ")

try:
    # Send magic packet (WOL)
    send_magic_packet(mac_address, ip_address)
    print("WOL signal sent successfully!")
except Exception as e:
    print(f"An error occurred: {e}")
