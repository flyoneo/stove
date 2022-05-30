import grpc

from accounts.account import Account
import accounts.v1.gvoice_pb2
import accounts.v1.gvoice_pb2_grpc


class AccountStore:
    """Manages the GVoice accounts registered with GVMS.
    """

    def __init__(self, hostname, port):
        """Constructor.

        Args:
            hostname (str): the hostname for GVMS.
            port (int): the port for GVMS.
        """
        channel = grpc.insecure_channel(f'{hostname}:{port}')
        self._client = accounts.v1.gvoice_pb2_grpc.GVoiceStub(channel)
        self._accounts = {}
        self.sync_accounts()

    def sync_accounts(self):
        """Setups the internal account store from the GVoice accounts registered
        with GVMS.
        """
        self._accounts.clear()
        numbers = self._get_numbers()
        for number in numbers:
            self._accounts[number] = Account(self._client, number)

    def get_account(self, number):
        """Fetches a given GVoice account via its numbers.

        Args:
            number (str): the number of the GVMS account.

        Raises:
            ValueError: raised if no GVoice accounts exists for the given number.

        Returns:
            accounts.account.Account: the GVoice account.
        """
        if number not in self._accounts:
            raise ValueError(f'No account exists for number {number}.')

        return self._accounts[number]

    def get_accounts(self):
        """Gets all of the GVoice accounts registered with GVMS.

        Returns:
            list(accounts.account.Account): a list of all of the GVoice accounts.
        """
        return list(self._accounts.values())

    def _get_numbers(self):
        """Fetches all of the GVoice numbers registered with GVMS.

        Raises:
            RuntimeError: raised if the call to GVMS failed.
        Returns:
            list(str): a list of gvoice numbers
        """
        resp = self._client.GetGVoiceNumbers(
            accounts.v1.gvoice_pb2.FetchGVoiceNumbersRequest()
        )
        if not resp.success:
            raise RuntimeError('Unable to fetch GVoice numbers from GVMS.')

        return resp.gvoice_phone_numbers
