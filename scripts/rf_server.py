from robotremoteserver import RobotRemoteServer
from keyboardDevice import keyboardDevice

server = RobotRemoteServer(keyboardDevice(), host='', port=8270,
                           port_file='/tmp/remote-port.txt', serve=False)
server.serve()