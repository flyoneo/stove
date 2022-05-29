import grpc

from accounts.account import Account
import accounts.v1.gvoice_pb2
import accounts.v1.gvoice_pb2_grpc


class AccountStore:
    def __init__(self, hostname, port):
        channel = grpc.insecure_channel(f'{hostname}:{port}')
        self._client = accounts.v1.gvoice_pb2_grpc.GVoiceStub(channel)
        self._accounts = {}

    def setup(self):
        numbers = self.get_numbers()
        for number in numbers:
            self._accounts[number] = Account(self._client, number)

    def get_account(self, number):
        if number not in self._accounts:
            raise ValueError(f'No account exists for number {number}.')

        return self._accounts[number]

    def get_accounts(self):
        return list(self._accounts.values())

    def get_numbers(self):
        resp = self._client.GetGVoiceNumbers(
            accounts.v1.gvoice_pb2.FetchGVoiceNumbersRequest()
        )
        if not resp.success:
            raise ValueError('Unable to fetch GVoice numbers from GVMS.')

        return resp.gvoice_phone_numbers
