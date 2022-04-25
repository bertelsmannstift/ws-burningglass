import json
import logging
from pathlib import Path, PurePosixPath
from uuid import UUID

import paramiko
from pandas import Timestamp

from utils.settings import settings

logger = logging.getLogger(__name__)


class Controller:
    def __init__(
        self
    ):
        self._transport = paramiko.Transport((settings.SSH_HOST))
        self._sftp = None

    def __del__(self):
        self.close_sftp()
        logger.info('shutdown')

    def open_sftp(self):
        private_key = paramiko.Ed25519Key.from_private_key_file(
            settings.SSH_PRIVATE_KEY_FILE_PATH, password=settings.SSH_PRIVATE_KEY_FILE_PASSWORD)
        self._transport.connect(
            username=settings.SSH_USER, pkey=private_key)
        self._sftp = paramiko.SFTPClient.from_transport(self._transport)

    def close_sftp(self):
        self._transport.close()

    def get_file(self, id: str, published_at: Timestamp):
        filename = f'{UUID(id).hex}.json'
        path = Path(
            f'{settings.SSH_DIR}/{published_at.date().isoformat()}/{filename}')
        local_path = Path(Path.cwd(), f'{settings.SSH_DIR_LOCAL}', path)
        # Create parent folder locally, if it does not exist
        if local_path.exists():
            with local_path.open() as reader:
                obj = json.load(reader)
            return obj
        if not local_path.parent.exists():
            local_path.parent.mkdir(parents=True, exist_ok=True)

        # get the file from remote
        # PurePosixPath is used, as the remote system is a unix system. This is needed, so this snippet can be run from Windows environment
        try:
            if self._sftp is None:
                self.open_sftp()
                logger.info('opened sftp connection')
            self._sftp.get(str(PurePosixPath(path)), str(local_path))
            with local_path.open() as reader:
                obj = json.load(reader)
            return obj
        except Exception as e:
            logger.error(e)
            return
