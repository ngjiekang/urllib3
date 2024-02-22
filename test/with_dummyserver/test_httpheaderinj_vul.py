from urllib3.connection import HTTPConnection

conn = http.client.HTTPConnection("localhost", 80)
conn.request(method="GET / HTTP/1.1\r\nHost: abc\r\nRemainder:", url="/index.html")

from flask import Flask, request
app = Flask(__name__)

@app.route("/files/<expression>")
def analyze_file(expression):
  conn = http.client.HTTPConnection("localhost", 80)
  
  conn.request(method=expression, url="/index.html")
  eval(expression)
