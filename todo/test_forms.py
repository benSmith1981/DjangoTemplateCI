from django.test import TestCase
from .forms import ItemForm

# Create your tests here.
class TestItemForm(TestCase):

    def test_itemNameIsRequired(self):
        form = ItemForm({'name':''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required')

    def test_doneFieldIsNotRequired(self):
        form = ItemForm({'name':'Test Todo Item'})
        self.assertTrue(form.is_valid())

    def test_fieldsAreExplicitInFormMetaClass(self):
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ['name', 'done'])