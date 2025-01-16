import socketserver



htmlpre = "<html><form>"

board = "_________"
htmlsuf = "</form></html>"

sq = "<div style='width:30%;height:30%;border:solid'></div>"

htmlboard = ""
i=0
for square in board:
	htmlboard+=sq
	if i%3==0:
		htmlboard+="<br>"

html = htmlpre+htmlboard+htmlsuf

def ui():
	return html



class echo(socketserver.BaseRequestHandler):
	def handle(self):
		l = len(html)
		self.request.sendall(("HTTP1.0 200 \r\nContent-Length:"+str(l)+"\r\n\r\n"+html).encode("ASCII"))
		self.request.close()
server_address = ('127.0.0.1',8003)
httpd = socketserver.TCPServer(server_address,echo)
httpd.serve_forever()






 
