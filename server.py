import http.server
import socketserver
import webbrowser

# Set the port number
PORT = 9500

# Set the handler to manage static files
Handler = http.server.SimpleHTTPRequestHandler

print(f"Serving static files at http://localhost:{PORT}")

# Automatically open your default web browser to the URL
webbrowser.open(f"http://localhost:{PORT}")

# Start the local server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server.")
        httpd.server_close()
