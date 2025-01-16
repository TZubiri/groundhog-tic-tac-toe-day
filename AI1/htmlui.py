import socketserver

board = "x___o____"

def boardhtml(board):
	sq = "<div style='width:30%;height:30%;border:solid'></div>"
	htmlpre=  "<html><head><link rel='stylesheet' href='webui.css'</link></head><body><ttt>"
	htmlpost= "</ttt></body></html>"
	linepre= "<my-lin>"
	linepost= "</my-lin>"

	x = "<img class='x' src='x.bmp'></img>"
	o = "<img class='o' src='o.bmp'></img>"

	sq_template = lambda sqid,content: "<a href="+sqid+" class='my-sq'>"+content+"</a>"

	inner = ""
	i=0
	for square in board:
		if i%3==0:
			inner+="<my-lin>"
		if square == 'x':
			content = x
		elif square == 'o':
			content = o
		else:
			content = ""
		inner+=sq_template(str(i),content)
		if i%3==2:
			inner+="</my-lin>"
		i+=1
	return htmlpre+inner+htmlpost





f = open("webui.css","rb")
css = f.read()
f.close()

f = open("x.bmp","rb")
ximg = f.read()
f.close()

f = open("o.bmp","rb")
oimg = f.read()
f.close()


class echo(socketserver.BaseRequestHandler):
	def handle(self):
		inp = self.request.recv(16) #longest relevant request is "GET /0123456789", we get an extra character for posts, or a final separator
		print(inp)
		if inp[0] != b"G"[0] and inp[3] != b" "[0]:
			self.request.sendall("HTTP1.0 405\r\n".encode("ASCII"))

		def send404(self):
			self.request.sendall("HTTP1.0 404\r\n".encode("ASCII"))

		if inp[4]!=b"/"[0]:
			send404(self)
		space2i = inp[4:].find(b" ")
		if space2i == -1:
			send404(self)
		path = inp[4:4+space2i]
		
		def sendfile(self,bytes):
			l = len(bytes)
			self.request.sendall(b"HTTP1.0 200 \r\nContent-Length:"+str(l).encode("ASCII")+b"\r\n\r\n"+bytes)
		print(path)
		if path == b"/webui.css":
			sendfile(self,css)
		elif path == b"/o.bmp":
			sendfile(self,oimg)
		elif path == b"/x.bmp":
			sendfile(self,ximg)
		elif path == b"/" or path[0:2] == b"/b" or path == b"/index" or path == b"/index.html":
			nboard = ["_"]*9
			turn = True
			for move in path[2:].decode("ASCII"):
				i = int(move)
				nboard[i]= "o" if turn else "x"
				
			board = "".join(nboard)
			sendfile(self,boardhtml(board).encode("ASCII"))
		else:
			send404(self)
		self.request.close()

server_address = ('127.0.0.1',8001)
httpd = socketserver.TCPServer(server_address,echo)
httpd.serve_forever()






 
