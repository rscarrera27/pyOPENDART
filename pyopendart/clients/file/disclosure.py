from pyopendart.clients.base import ClientBase


class DisclosureFileDownloader(ClientBase):
    def get_document(self, receipt_no: str, save_to: str):
        self.client.download("document", {"rcept_no": receipt_no}, save_to=save_to)
