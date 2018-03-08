import paramiko

def test_login():
    host = "ssh.pythonanywhere.com"
    client = paramiko.client.SSHClient()
    client.load_system_host_keys()
    client.connect(host)
    stdin, stdout, stderr = client.exec_command('ls -l')
