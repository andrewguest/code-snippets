from typing import List
from fabric import Connection
from paramiko.ssh_exception import AuthenticationException


"""
    This module allows you to use SSH to connect to a remote computer
        and run commands on it and read files from the remote computer.

    To use (an example):
        from fabric_ssh import RemoteClient
        myconnection = RemoteClient('myServername', 'myUsername', '/home/andrew/.ssh/id_rsa')
        myconnection.execute_commands(['hostname', 'uptime', 'whoami'])
        myconnection.read_file('/root/somefile.txt')

"""


class RemoteClient:
    """ Client to interact with a remote host via SSH """

    def __init__(self, host: str, user: str, ssh_key_filepath: str) -> None:
    	"""Connect to a remote server

        Args:
            host (str): The IP or hostname of the server to connect to.
            user (str): The user to connect to the remote server as.
            ssh_key_filepath (str): Path to an SSH private key to use authenticate to the remote server.
        """
    
        self.host = host
        self.user = user
        self.ssh_key_filepath = ssh_key_filepath
        self.client = None
        self.conn = None

    def _connect(self):
        """ Open connection to remote host """

        if self.conn is None:
            try:
                self.client = Connection(
                    host=self.host,
                    user=self.user,
                    connect_kwargs={
                        "key_filename": [
                            self.ssh_key_filepath,
                        ]
                    },
                )
            except AuthenticationException as error:
                print(f"Authentication error: {error}")
        return self.client

    def execute_commands(self, commands: List[str]):
        """Executes commands on the remote system

        Args:
            commands (List[str]): List of Unix commands as strings
        """

        # if there's not already an active connection, then connect
        if self.conn is None:
            self.conn = self._connect()

        for cmd in commands:
            result = self.conn.run(cmd, hide=True)
            print(f"Command sent: {cmd}")
            print(f"Output: {result.stdout}")
            print(f'Errors: {result.stderr}\n')

    def read_file(self, file_to_read: str):
        """
        If not already connected, then connect to the remote server
            then read each line of the file provided to this function.

        Args:
            file_to_read (str): Filename or full path to a file to
                open and read.
        """

        # if there's not already an active connection, then connect
        if self.conn is None:
            self.conn = self._connect()

        with self.conn as connection, connection.sftp() as sftp:
            with sftp.open(file_to_read) as file:
                for line in file:
                    print(line)

