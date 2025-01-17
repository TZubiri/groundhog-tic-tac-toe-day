import socketserver
import AI1

board = "x___o____"

def boardhtml(board):
	sq = "<div style='width:30%;height:30%;border:solid'></div>"
	htmlpre=  "<html><head>"+\
		"<link rel='stylesheet' href='webui.css'</link>"+\
		"<link rel='preload' href='x.bmp' as='image'>"\
		"<link rel='preload' href='o.bmp' as='image'>"\
		"</head><body><ttt>"
	htmlpost= "</ttt></body></html>"
	linepre= "<my-lin>"
	linepost= "</my-lin>"

	x = "<img class='x' src='x.bmp'></img>"
	o = "<img class='o' src='o.bmp'></img>"

	sq_template = lambda board,sqid,content: "<a href=b"+board+sqid+" class='my-sq'>"+content+"</a>"

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
		inner+=sq_template(board,str(i),content)
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
		inp = self.request.recv(17) #longest and typical request is "GET /b_________1 " 17 chars with the final space
		print(inp)
		if inp[0] != b"G"[0] and inp[3] != b" "[0]:
			self.request.sendall("HTTP1.1 405\r\n".encode("ASCII"))

		def send404(self):
			self.request.sendall("HTTP1.1 404\r\n".encode("ASCII"))

		if inp[4]!=b"/"[0]:
			send404(self)
		space2i = inp[4:].find(b" ")
		if space2i == -1:
			send404(self)
		path = inp[4:4+space2i]
		
		def sendfile(self,bytes,cache=False):
			controlcache = b"\r\nControl-Cache: max-age=604800" if cache==True else b""
			l = len(bytes)
			self.request.sendall(b"HTTP1.1 200 \r\nContent-Length:"+str(l).encode("ASCII")+controlcache+b"\r\n\r\n"+bytes)
		print(path)
		if path == b"/webui.css":
			sendfile(self,css)
		elif path == b"/o.bmp":
			sendfile(self,oimg,cache=True)
		elif path == b"/x.bmp":
			sendfile(self,ximg,cache=True)
		elif path == b"/" or path == b"index" or path == b"/index.html":
			sendfile(self,boardhtml("_________").encode("ASCII"))

		elif path[:2] == b"/b":
			sboard = path[2:-1].decode("ASCII")
			smove = path.decode("ASCII")[-1]
			sboard = AI1.make_move(sboard,int(smove))
			result = AI1.winner(sboard)
			if result == "o":
				sendfile(self,b"<html><p>O wins.</p></html>")
				return
			elif result == "x":
				sendfile(self,b"<html><p>X wins.</p></html>")
				return
			elif result == "tie":
				sendfile(self,b"<html><p>Tie</p></html>")
				return
			sboard = AI1.play_9(sboard)
			result = AI1.winner(sboard)
			if result == "o":
				sendfile(self,b"<html><p>O wins.</p></html>")
				return
			elif result == "x":
				sendfile(self,b"<html><p>X wins.</p></html>")
				return
			elif result == "tie":
				sendfile(self,b"<html><p>Tie</p></html>")
				return

			sendfile(self,boardhtml(sboard).encode("ASCII"))

		else:
			send404(self)
		self.request.close()

server_address = ('127.0.0.1',8003)
httpd = socketserver.TCPServer(server_address,echo)
httpd.serve_forever()






 
