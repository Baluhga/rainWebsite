#!/usr/bin/env python3
import http.server
import socketserver
import os
import time

PORT = 8000

class DebugHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        start_time = time.time()
        print(f"\n[{time.strftime('%H:%M:%S')}] Request: {self.path}")
        
        result = super().do_GET()
        
        elapsed = time.time() - start_time
        print(f"[{time.strftime('%H:%M:%S')}] Completed in {elapsed:.3f}s")
        
        return result

os.chdir(os.path.dirname(os.path.abspath(__file__)))
print(f"Serving from: {os.getcwd()}")
print(f"Server running at http://localhost:{PORT}")
print("Press Ctrl+C to stop\n")

with socketserver.TCPServer(("", PORT), DebugHandler) as httpd:
    httpd.serve_forever()