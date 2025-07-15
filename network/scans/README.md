## 🌐 Escaneos de red – `network/scans`

Esta carpeta contiene scripts para realizar tareas básicas de escaneo de red sin depender de herramientas externas como `nmap`. Son útiles en entornos de pentesting con restricciones o para crear soluciones personalizadas.

### 📂 Scripts disponibles

- `scan_hosts.sh`  
  Escanea una red local para detectar hosts activos mediante `ping`.

- `scan_ports.sh`  
  Realiza escaneo de puertos TCP en un host específico usando `/dev/tcp`.

- `scan_arp.py`  
  Detecta dispositivos en la red local mediante ARP scanning usando `Scapy`.

---

### 📦 Dependencias

✅ **Bash scripts**  
No requieren herramientas externas.

🐍 **Python scripts**  
- [`scapy`](https://pypi.org/project/scapy/) – Necesario para ejecutar `scan_arp.py`  
  ```bash
  pip install scapy

