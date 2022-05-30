import accounts.v1.gvoice_pb2


class Account:
    """Representation of a GVoice account.
    """

    def __init__(self, client, number):
        """Constructor.

        Args:
            client (accounts.v1.gvoice_pb2_grpc.GVoiceStub): a connection to GVMS.
            number (str): the phone number belonging to the GVoice account.
        """
        self._client = client
        self._number = number

    def send_text(self, text: str, recipient_number: str):
        """Sends a given text to a recipient.

        Args:
            text (str): the message to send.
            recipient_number (str): the recipient of the text message.
        """
        self._client.SendSMS(
            accounts.v1.gvoice_pb2.SendSMSRequest(
                gvoice_phone_number=self._number,
                recipient_phone_number=recipient_number,
                message=text,
            )
        )

    def get_number(self):
        """Retrieve the underlying phone number for the GVoice account.

        Returns:
            str: the phone number.
        """
        return self._number
