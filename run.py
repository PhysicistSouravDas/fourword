from website import Server

if __name__ == '__main__':
	app = Server().init_server(__name__)
	app.run('0.0.0.0')