import flask

app = flask.Flask("app")

htmlpre = "<html><form>"

board = "_________"
htmlsuf = "</form></html>"

sq = "<div style='width=30%;height=30%;border=solid'></div>"

htmlboard = ""
i=0
for square in board:
	htmlboard+=sq
	if i%3==0:
		htmlboard+="<br>"

html = htmlpre+htmlboard+htmlsuf

@app.route("/ui")
def ui():
	return html

app.run("0.0.0.0",8080)
 
