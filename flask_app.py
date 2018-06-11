from webapp import Server
app = Server().init_server()

if __name__ == '__main__':
	app.run('0.0.0.0')