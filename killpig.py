"""
Usage: %(scriptName)s [port1 port2 ... portN]

This module kill all process runnning on the specified ports
Ports must be passed as parameters
"""

import sys
import psutil

# Check arguments
if len(sys.argv) < 2:
    print(__doc__ % {'scriptName' : sys.argv[0].split("/")[-1]})
    sys.exit(0)

PORTS = sys.argv

# Kill process running on specified ports
for conn in psutil.net_connections("inet4"):
    if str(conn.laddr[1]) in PORTS:
        print('Killing process with PID {} running on port {}'.format(conn.pid, conn.laddr[1]))
        p = psutil.Process(conn.pid)
        p.terminate()
