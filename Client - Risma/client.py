#import xmlrpc Client
import xmlrpc.client

#import config
from config_client import *

#create server
server = xmlrpc.client.ServerProxy(BASE_CONFIG_URL)

#client version
client_version = BASE_VERSION_CLIENT

#show each version
print("Checking...")

#check server version and  client version
if server.version_check(client_version):
    print("You have the latest update")
else:
    print("A new release of segitiga available: ",client_version, "->", server.get_new_version())
    print("To update, run: --sayamaukak segitiga")
    input = input()
    if input == "--sayamaukak segitiga":
        client_version = server.get_new_version()
        print("Updating...")
        lines = [f"BASE_CONFIG_IP_ADDRESS = '26.179.107.27'", f'BASE_CONFIG_PORT = 1234', f"BASE_CONFIG_URL = 'http://26.179.107.27:1234'", f"BASE_CONFIG_PATH = '/RPC2'", f"BASE_VERSION_CLIENT = {client_version}"]
        with open('config_client.py', 'w') as f:
            for line in lines:
                f.write(line)
                f.write('\n')
        with open('segitiga.py', 'w') as app:
            app.write('')
        with open('segitiga.py', 'a') as app:
            for line in server.latest_app():
                app.write(line)
        print("Download success")
        print("You have the latest update, version: ", client_version)
    else:
        print("'",input,"' is not recognized as an internal or external command, operable program or batch file.")

