"""
Simple HTTP server to serve DZI t    print(f"🚀 Starting HTTP server on port {PORT}...")
    print(f"📁 Serving files from: {script_dir}")
    print(f"🌐 Available Viewers:")
    print(f"   📷 Gallery View: http://localhost:{PORT}/gallery-viewer.html")
    print(f"   🎯 Selector View: http://localhost:{PORT}/selector-viewer.html") 
    print(f"   📑 Tab View: http://localhost:{PORT}/tab-viewer.html")
    print(f"   📰 Original: http://localhost:{PORT}/viewer.html")
    print("🔧 Press Ctrl+C to stop the server")
    print("-" * 50)locally
Run this script and then open http://localhost:8000/viewer.html
"""

import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 8080

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS headers to allow local access
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

def start_server():
    """Start the HTTP server and open the viewer in browser"""
    
    # Change to the script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    # Check if required files exist
    if not os.path.exists('img/test.dzi'):
        print("Error: test.dzi file not found!")
        print("Please make sure you have generated the DZI tiles first.")
        return
    
    if not os.path.exists('viewer.html'):
        print("Error: viewer.html file not found!")
        return
    
    print(f"Starting HTTP server on port {PORT}...")
    print(f"Serving files from: {script_dir}")
    print(f"Viewer URL: http://localhost:{PORT}/viewer.html")
    print("Press Ctrl+C to stop the server")
    print("-" * 50)
    
    try:
        with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
            # Open browser automatically - default to gallery view
            webbrowser.open(f'http://localhost:{PORT}/gallery-viewer.html')
            
            print(f"Server running at http://localhost:{PORT}/")
            for file in os.listdir('.'):
                if os.path.isfile(file):
                    print(f"   - {file}")
            print("-" * 50)
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\nServer stopped by user")
    except OSError as e:
        print(f"Error starting server: {e}")
        print(f"Try using a different port or check if port {PORT} is already in use")

if __name__ == "__main__":
    start_server()