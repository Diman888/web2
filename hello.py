def wsgi_application(environ, start_response):
	status = '200 OK'
	headers = [
	('Content-Type', 'text/plain')
	]
	temp=str(environ['QUERY_STRING'])
	stro = str()
	for i in temp:
		if i == '&':
			stro = stro + '\r\n'
		else:
			stro = stro + i
	body = stro
	start_response(status, headers)
	return [ body ]
