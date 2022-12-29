#import xmlrpc Server and RequestHandler
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

#config
from config_server import *

#requestHandler class
class requestHandler(SimpleXMLRPCRequestHandler):
    paths = (BASE_CONFIG_PATH)

#server version
server_version = BASE_VERSION_SERVER
print("Server version: ", server_version)

#create server
server = SimpleXMLRPCServer((BASE_CONFIG_IP_ADDRESS, BASE_CONFIG_PORT),requestHandler=requestHandler)
server.register_introspection_functions()

#version control 
class VersionControl():
    def __init__(self, server_version):
        self.server_version = server_version

    #return check version result
    def version_check(self, client_version):
        if client_version == self.server_version:
            return True
        else:
            return False

    #return server version
    def get_new_version(self):
        return self.server_version

    #return file
    def latest_app(self):
        f = open('segitiga.py', 'r')
        return f.read()

#register function
obj = VersionControl(server_version)
server.register_function(obj.version_check, 'version_check')
server.register_function(obj.get_new_version, 'get_new_version')
server.register_function(obj.latest_app, 'latest_app')

#run server
server.serve_forever()