import http.server
import socketserver
import pyqrcode
import png
import os
import socket
import webbrowser

# Assign a port number and specify the user's name
PORT = 8080
USER_NAME = "shubham"

# Obtain the IP address of the PC and convert it into a QR code
def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

IP_ADDRESS = get_ip_address()
url = f"http://{IP_ADDRESS}:{PORT}"
qr_code = pyqrcode.create(url)
qr_code.png('qr_code.png', scale=8)

# Generate the index.html file dynamically
def generate_index_html():
    files = os.listdir('.')
    links = ""
    for file in files:
        if os.path.isfile(file):
            links += f'<li><a href="{file}">{file}</a></li>\n'

    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>File Sharing App</title>
</head>
<body>
    <h1>Welcome to the File Sharing App</h1>
    <p>Here are the files available for download:</p>
    <ul>
        {links}
    </ul>
</body>
</html>"""
    
    with open('index.html', 'w') as f:
        f.write(html_content)

generate_index_html()

# Display the QR code in a web browser for easy access
webbrowser.open('qr_code.png')

# Create an HTTP request handler to handle file sharing
class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        print(f"Serving file: {self.path}")
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

# Implement file sharing functionality by serving files over HTTP
with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
