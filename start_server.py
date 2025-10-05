import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 8080

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

def start_server():
    """Start the HTTP server and open the viewer in browser"""
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    
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
            webbrowser.open(f'http://localhost:{PORT}/viewer.html')
            
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