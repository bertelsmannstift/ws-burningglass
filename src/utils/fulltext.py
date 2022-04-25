import json
from pathlib import Path

from utils.sftp_controller import Controller


class Fulltext_Textkernel:
    def __init__(self) -> None:
        self.sftp_controller = Controller()

    def get_file(self, id, published_at):
        return self.sftp_controller.get_file(id, published_at)


class Fulltext_BurningGlass:
    def __init__(self) -> None:
        self.path = Path('../../volltexte/burningglass/2021')

    def get_file(self, general_id):
        filepath = self.path / f'{general_id}.json'

        with filepath.open() as reader:
            obj = json.load(reader)
        return obj
