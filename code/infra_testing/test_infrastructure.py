import paramiko
import private

client = None

def setup_module(module):
    global client
    client = paramiko.client.SSHClient()
    client.load_system_host_keys()
    client.connect(private.host, username=private.user, password=private.password)

def teardown_module(module):
    global client
    if client:
        client.close()
    client = None

def test_login():
    global client
    stdin, stdout, stderr = client.exec_command('whoami')
    stdout = stdout.read().decode().strip()
    assert stdout==private.user
    print(stdout)

def test_python_installed():
    stdin, stdout, stderr = client.exec_command('python3 --version')
    stdout = stdout.read().decode().strip()
    assert "Python 3" in stdout
    print(stdout)    

def test_pip_installed():
    global client
    stdin, stdout, stderr = client.exec_command('pip3 --version')
    stdout = stdout.read().decode().strip()
    assert "pip" in stdout
    assert " 9." in stdout
    print(stdout)
    
