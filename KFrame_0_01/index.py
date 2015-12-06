def application(environ, start_response):
  #Simple application object
  status = '200 OK'
  response_headers[('Contect-type', 'text/plain')]
  start_response(status, response_headers)
  return ['Hello, World!\n']

