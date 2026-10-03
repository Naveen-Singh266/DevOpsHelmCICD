from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        message = """
        <html>
        <body>
            <h1>Hello from Helm + GitHub Actions + AWS EKS!</h1>
            <p>Application deployed successfully.</p>
        </body>
        </html>
        """

        self.wfile.write(message.encode())

server = HTTPServer(("0.0.0.0", 8080), Handler)

print("Application running on port 8080")

server.serve_forever()

