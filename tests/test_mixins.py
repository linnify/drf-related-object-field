from django.test import TestCase, RequestFactory

from . import models, serializers


class TestRelatedObjectFieldMixin(TestCase):
    """
    Test the related object field mixin.
    """

    def test_returns_nested_object_many_to_one(self):
        """
        Test if the mixin actually returns the child
        object as rendered by the serializer in a many-to-one relationship.
        :return:
        """
        rf = RequestFactory()
        request = rf.get("/books/1")
        author = models.Author.objects.create(name="John Doe")
        book = models.Book.objects.create(title="Book", year=2010, author=author)

        book_serializer = serializers.BookSerializer(
            instance=book, context={"request": request}
        )

        book_data = book_serializer.data

        self.assertEqual(
            book_data["author"],
            {
                "id": author.pk,
                "name": author.name,
            }
        )

    def test_returns_nested_object_one_to_many(self):
        """
        Test if the mixin actually returns the child
        objects as rendered by the serializer in a one-to-many relationship.
        :return:
        """
        rf = RequestFactory()
        request = rf.get("/authors")
        author = models.Author.objects.create(name="John Doe")
        book1 = models.Book.objects.create(
            title="Title 1", year=2010, author=author
        )
        book2 = models.Book.objects.create(
            title="Title 2", year=2011, author=author
        )
        book3 = models.Book.objects.create(
            title="Title 3", year=2012, author=author
        )

        author_serializer = serializers.AuthorSerializer(
            instance=author, context={"request": request}
        )

        author_data = author_serializer.data

        self.assertTrue(isinstance(author_data["books"], list))
        self.assertEqual(len(author_data["books"]), 3)

        for book_data in author_data["books"]:
            self.assertTrue("title" in book_data.keys())

    def test_creates_nested_object_many_to_one(self):
        """
        Test if the serializer creates an object given
        an existing foreign key ID.
        :return:
        """
        rf = RequestFactory()
        request = rf.post("/books")
        author = models.Author.objects.create(name="John Doe")

        book_data = {
            "title": "Test",
            "year": 2020,
            "author": author.pk,
        }

        book_serializer = serializers.BookSerializer(
            data=book_data, context={"request": request}
        )
        self.assertTrue(book_serializer.is_valid())

        book_serializer.save()

        book = book_serializer.instance

        self.assertEqual(book.title, "Test")
        self.assertEqual(book.year, 2020)
        self.assertEqual(book.author.pk, author.pk)

    def test_updates_nested_object_many_to_one(self):
        """
        Tests if the serializer updates an existing object
        given an existing pk of a related object.
        :return:
        """
        rf = RequestFactory()
        request = rf.put("/books/1")
        initial_author = models.Author.objects.create(name="John Doe")
        updated_author = models.Author.objects.create(name="Bill McDonald")
        book = models.Book.objects.create(
            title="Test", year=2019, author=initial_author
        )

        book_data = {
            "title": "New title",
            "year": 2020,
            "author": updated_author.pk
        }

        book_serializer = serializers.BookSerializer(
            instance=book, data=book_data, context={"request": request}
        )
        self.assertTrue(book_serializer.is_valid())

        book_serializer.save()

        updated_book = book_serializer.instance

        self.assertEqual(updated_book.pk, book.pk)
        self.assertEqual(updated_book.title, "New title")
        self.assertEqual(updated_book.year, 2020)
        self.assertEqual(updated_book.author.pk, updated_author.pk)
