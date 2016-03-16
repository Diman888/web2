def wsgi_application(environ, start_response):
	status = '200 OK'
	headers = [
	('Content-Type', 'text/html')
	]
	stro = '<html><head></head><body><p>Answer:<ol>'
	for key in environ:
		stro=stro + '<li>' + str(key) + '  ===  ' + str(environ[key]) + ' (' + str(type(environ[key])) + ') </li>'
	body = stro + '</ol></body></html>'
	start_response(status, headers)
	return [ body ]
