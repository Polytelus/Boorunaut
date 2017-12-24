# -*- coding: utf-8 -*-
import re
import tempfile
from collections import Counter
from urllib.parse import urlparse

import django
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser, User
from django.test import Client, RequestFactory, TestCase
from django.test.utils import override_settings
from booru.utils import space_splitter
from booru.utils import space_joiner

class UtilitiesTests(TestCase):
    fixtures = []

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

    def test_space_splitter_generates_tags_from_string(self):
        tag_string = "test1 test2 test:test_3 test_4"
        generated_tags = space_splitter(tag_string)
        expected_generated_tags = ["test1", "test2", "test:test_3", "test_4"]
        self.assertEqual(generated_tags, expected_generated_tags)

    def test_space_joiner_turns_tags_into_a_string(self):
        tags = ["test4", "test_5", "test:test6"]
        generated_string = space_joiner(tags)
        expected_generated_string = "test4 test_5 test:test6"
        self.assertEqual(generated_string, expected_generated_string)
