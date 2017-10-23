from django.test import TestCase
from .content_addressable_file import ContentAdressableFile
from unittest.mock import MagicMock
from django.core.files.uploadedfile import SimpleUploadedFile, Memory
from django.core.files import File


class TestModel(TestCase):
    def setUp(self):

