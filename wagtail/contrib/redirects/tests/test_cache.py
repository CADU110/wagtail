from django.core.cache import cache
from django.test import TestCase
from unittest.mock import patch

class CachePrefixTest(TestCase):
    def setUp(self):
        self.cache_prefix = 'test_prefix_'
        self.name = 'test_redirect'
        self.full_cache_key = self.cache_prefix + self.name

    @patch('django.core.cache.cache.delete')
    def test_cache_removal_includes_prefix(self, mock_delete):
        cache.set(self.full_cache_key, 'some_value')

        self.assertEqual(cache.get(self.full_cache_key), 'some_value')

        cache.delete(self.full_cache_key)

        mock_delete.assert_called_with(self.full_cache_key)

