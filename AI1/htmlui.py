import socketserver
import AI1

board = "x___o____"

def boardhtml(board):
	result = AI1.winner(board)
	sq = "<div style='width:30%;height:30%;border:solid'></div>"
	htmlpost= "</ttt></body></html>"
	linepre= "<my-lin>"
	linepost= "</my-lin>"

	x = "<img class='x' src='x.bmp'></img>"
	o = "<img class='o' src='o.bmp'></img>"

	if result == "o":
		resulthtml = "<p style='size:32'>O wins</p>"
	elif result == "x":
		resulthtml = "<p style='size:32'>X wins</p>"
	elif result == "tie":
		resulthtml = "<p style='size:32'>TIE!</p>"
	else:
		resulthtml = ""

	if result == "":
		disabled = False
	else:
		disabled = True

	htmlpre=  "<html><head>"+\
		"<link rel='stylesheet' href='webui.css'</link>"+\
		"<link rel='preload' href='x.bmp' as='image'>"\
		"<link rel='preload' href='o.bmp' as='image'>"\
		"</head><body>"+resulthtml+"<ttt>"

	def sq_template(board,sqid,content,disabled):
		if disabled:
			href =''
		else:
			href=" href='b"+board+sqid+"'"
		return "<a"+href+" class='my-sq'>"+content+"</a>"

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
		inner+=sq_template(board,str(i),content,disabled)
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
			controlcache = b"\r\nCache-Control:max-age=31536000,immutable" if cache==True else b""
			l = len(bytes)
			self.request.sendall(b"HTTP1.1 200 \r\nContent-Length:"+str(l).encode("ASCII")+controlcache+b"\r\n\r\n"+bytes)
			self.request.close()
		print(path)
		if path == b"/webui.css":
			sendfile(self,css)
		elif path == b"/o.bmp":
			sendfile(self,oimg,cache=True)
		elif path == b"/x.bmp":
			sendfile(self,ximg,cache=True)
		elif path == b"/" or path == b"index" or path == b"/index.html":
			sendfile(self,boardhtml("_________").encode("ASCII"),cache=True)

		elif path[:2] == b"/b":
			sboard = path[2:-1].decode("ASCII")
			smove = path.decode("ASCII")[-1]
			sboard = AI1.make_move(sboard,int(smove))
			if AI1.winner(sboard):
				sendfile(self,boardhtml(sboard).encode("ASCII"))
				self.request.close()
				return
			sboard = AI1.play_9(sboard)

			sendfile(self,boardhtml(sboard).encode("ASCII"))
		else:
			send404(self)
		self.request.close()

server_address = ('127.0.0.1',8000)
httpd = socketserver.TCPServer(server_address,echo)
httpd.serve_forever()






 
