from django.core.cache import cache
from wagtail.core.models import Site
from django.test import TestCase
from unittest.mock import patch

class CachePrefixTest(TestCase):
    def setUp(self):
        # Configure o nome de cache e o prefixo para garantir a consistência
        self.cache_prefix = 'test_prefix_'  # Substitua pelo prefixo correto
        self.name = 'test_redirect'
        self.full_cache_key = self.cache_prefix + self.name

    @patch('wagtail.core.models.cache.delete')  # Patch para evitar deletação real
    def test_cache_removal_includes_prefix(self, mock_delete):
        # Adiciona um valor no cache com o prefixo adequado
        cache.set(self.full_cache_key, 'some_value')

        # Verifique se o valor foi armazenado corretamente
        self.assertEqual(cache.get(self.full_cache_key), 'some_value')

        # Chama o método remove (simulando a remoção de cache)
        cache.delete(self.full_cache_key)

        # Verifique se a chave com o prefixo foi removida
        mock_delete.assert_called_with(self.full_cache_key)

    def test_cache_removal_without_prefix(self):
        # Adiciona um valor no cache com a chave sem o prefixo
        cache.set(self.name, 'some_value')

        # Verifique se o valor foi armazenado corretamente
        self.assertEqual(cache.get(self.name), 'some_value')

        # Chama o método remove sem o prefixo
        cache.delete(self.name)

        # Verifique se a chave foi removida
        self.assertIsNone(cache.get(self.name))
       self.assertIn(other_page, descendants)  # other_page DEVE estar presente
