# https://pymotw.com/2/BaseHTTPServer/

from BaseHTTPServer import BaseHTTPRequestHandler
import urlparse
import os

class GetHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        parsed_path = urlparse.urlparse(self.path)
        videoURLText = parsed_path.query
        videoURLText = videoURLText.split('=')
        if (len(videoURLText) > 1):
            file = open('myfile', 'w')
            videoURLText.remove(videoURLText[0])
            videoURLText = ''.join(videoURLText)
            file.write(videoURLText)
            print videoURLText
            file.close()
        
        # print os.getcwd()
        message_parts = [
                'CLIENT VALUES:',
                'client_address=%s (%s)' % (self.client_address,
                                            self.address_string()),
                'command=%s' % self.command,
                'path=%s' % self.path,
                'real path=%s' % parsed_path.path,
                'query=%s' % parsed_path.query,
                'request_version=%s' % self.request_version,
                '',
                'SERVER VALUES:',
                'server_version=%s' % self.server_version,
                'sys_version=%s' % self.sys_version,
                'protocol_version=%s' % self.protocol_version,
                '',
                'HEADERS RECEIVED:',
                ]
        for name, value in sorted(self.headers.items()):
            message_parts.append('%s=%s' % (name, value.rstrip()))
        message_parts.append('')
        message = '\r\n'.join(message_parts)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(message)
        return

if __name__ == '__main__':
    try:
        from BaseHTTPServer import HTTPServer
        server = HTTPServer(('localhost', 8080), GetHandler)
        print 'Starting server, use <Ctrl-C> to stop'
        server.serve_forever()
    except KeyboardInterrupt:
        exit (0)