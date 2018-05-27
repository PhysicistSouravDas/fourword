from website import Server

if __name__ == '__main__':
	app = Server().init_server()
	app.run('0.0.0.0')