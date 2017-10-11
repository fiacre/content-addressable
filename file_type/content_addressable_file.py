import hashlib
from django.db import models


class ContentAdressableFile(models.Field):
    def __init__(self, file_name, file_contents, *args, **kwargs):
        self.file_contents = file_contents
        self.file_name = file_name
        super().__init__(*args, **kwargs)

    def digest(self, fp, block_size=1048576):
        '''
        @args: fp -- file object
            block_size -- adjust as needed
        '''
        sha256 = hashlib.sha256()
        loc = fp.tell()
        try:
            fp.seek(0)
            for block in iter(lambda: fp.read(block_size), b''):
                if block:
                    sha256.update(block)
                else:
                    break
            return sha256.hexdigest()
        finally:
            fp.seek(loc)
