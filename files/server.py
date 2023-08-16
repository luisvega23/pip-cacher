import http.server
import socketserver
import os
import subprocess
import logging

PORT = 8000

handler = http.server.SimpleHTTPRequestHandler

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class MyHttpRequestHandler(handler):
    def do_GET(self):
        package = self.path.split("/")[2]
        if package not in os.listdir("simple") and package != "pip":
            logging.info(f"{package} not found, donwloading !")
            subprocess.run(["pypi-mirror", "download", "-d", "downloads", "-b", f"{package}"])
            subprocess.run(["pypi-mirror", "create", "-d", "downloads", "-m", "simple"])
            subprocess.run(["cp", "-r" ,"downloads", "simple", "/pythonCacher/packages/"])
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

handler_object = MyHttpRequestHandler

with socketserver.TCPServer(("", PORT), handler_object) as httpd:
    logging.info(f"Server started at localhost: {PORT}")
    subprocess.run(["cp", "-r" ,"/pythonCacher/packages/downloads", "/pythonCacher/packages/simple", "/pythonCacher"])
    httpd.serve_forever()