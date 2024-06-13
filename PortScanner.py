import socket

def port_scan(host, port):
    try:
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        s.settimeout(1)
        
        result = s.connect_ex((host, port))
        
        if result == 0:
            print(f"Port {port}: Open")
        else:
            print(f"Port {port}: Closed")
        
        s.close()
    
    except KeyboardInterrupt:
        print("\nExiting program.")
        exit()
    
    except socket.error:
        print("Couldn't connect to server.")
        exit()

def main():
    host = "localhost"
    
    ports = [21, 22, 80, 443, 8080]
    
    print(f"Scanning ports on {host}...")
    
    for port in ports:
        port_scan(host, port)

if __name__ == "__main__":
    main()
