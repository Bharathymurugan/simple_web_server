
from http.server import HTTPServer,BaseHTTPRequestHandler
content ='''<html>
<html>
    <head>
        <title> TCP/IP PROTOCOL SUITE</title>
        <style>
            table{
                border-collapse: collapse;
                width:60%;
                height: 60%;
                
            }
            th,td{
                border:1px solid black;
                background-color: beige;
                font-size: x-large;
            }
        </style>
    </head>

    <BODY style= "background-color: #D7B377;">
        <p style="font-family: algerian;color: MAROON; font-size: xx-large; text-align:center"> TCP/IP PROTOCOL SUITE</p>
        <table align="center">
            <tr > 
                <th style="background-color: #E29578; "> TCP/IP MODEL</th>
                <th style="background-color: #E29578; "> TCP/IP PROTOCOL SUITE</th>
            </tr>
            <tr>
                <td> Application layer </td>
                <td> HTTP, FTP, TFTP, DNS, DHCP, SMTP, Telnet, SSH</td>
            </tr>
            <tr>
                <td>Transport layer</td>
                <td>TCP, UDP</td>
            </tr>
            <tr>
                <td>Internet layer</td>
                <td>IP</td>
            </tr>
            <tr>
                <td>Network interface card</td>
                <td>Ethernet, Token ring, Frame relay, ATM</td>
            </tr>
        </table>
    </BODY>
</html>
</html>'''
class Myserver(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200)
        self.send_header("content-type","text/html")
        self.end_headers()
        self.wfile.write(content.encode())
print("This is my webserver")
server_address=('',8000)
httpd = HTTPServer(server_address,Myserver)
httpd.serve_forever()
