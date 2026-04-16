import socket
import sys
from datetime import datetime

def scan_ports(target):
    # En liste over de mest almindelige porte, vi vil teste
    # 21: FTP, 22: SSH, 80: HTTP (Web), 443: HTTPS, 3389: RDP (Fjernskrivebord)
    ports_to_scan = [21, 22, 53, 80, 443, 3389]
    
    print("-" * 50)
    print(f"Scanner målet: {target}")
    print(f"Scanning startet kl: {datetime.now().strftime('%H:%M:%S')}")
    print("-" * 50)
    
    try:
        for port in ports_to_scan:
            # Opretter en ny netværks-socket for hver port
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            # Sætter en kort timeout, så vi ikke venter i evigheder på en lukket port
            socket.setdefaulttimeout(1) 
            
            # connect_ex forsøger at forbinde. Den returnerer '0', hvis det lykkes (porten er åben)
            result = s.connect_ex((target, port))
            
            if result == 0:
                print(f"[+] Port {port}:\t ÅBEN")
            else:
                print(f"[-] Port {port}:\t Lukket")
                
            s.close() # Lukker forbindelsen pænt ned igen
            
    except socket.gaierror:
        print("\nFejl: Værtsnavnet kunne ikke findes (tjek din stavning).")
        sys.exit()
    except socket.error:
        print("\nFejl: Kunne ikke oprette forbindelse til serveren.")
        sys.exit()

if __name__ == "__main__":
    print("=== FPB's Simple Port Scanner ===")
    # Beder brugeren om at indtaste en IP (f.eks. sin egen router)
    target_ip = input("Indtast IP-adresse eller domaene (f.eks. 192.168.1.1): ")
    scan_ports(target_ip)