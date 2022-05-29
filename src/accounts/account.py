import accounts.v1.gvoice_pb2


class Account:
    def __init__(self, client, number):
        self._client = client
        self._number = number

    def send_text(self, text: str, recipient_number: str):
        self._client.SendSMS(
            accounts.v1.gvoice_pb2.SendSMSRequest(
                gvoice_phone_number=self._number,
                recipient_phone_number=recipient_number,
                message=text,
            )
        )
    
    def get_number(self):
        return self._number
