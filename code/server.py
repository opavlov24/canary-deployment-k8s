from http.server import BaseHTTPRequestHandler, HTTPServer
import os

hostName = "0.0.0.0"
serverPort = 8080

class SimpleResponseServer(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(os.environ.get("SERVICE_RESPONSE", "Hello world"), "utf-8"))


def main():
    webServer = HTTPServer((hostName, serverPort), SimpleResponseServer)

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()

if __name__ == "__main__":
    main()