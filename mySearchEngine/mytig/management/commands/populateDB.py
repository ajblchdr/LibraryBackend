import os, sys
from django.core.management.base import BaseCommand
from mytig.models import Book

sys.path.append('./books/')

#python manage.py migrate --run-syncdb

class Command(BaseCommand):

    def handle(self, *args, **options):
        Book.objects.all().delete()
        print("CURRENT DIR = "+os.getcwd())
        booksFolder = './books/'
        for filename in os.listdir(booksFolder):
            book = open(booksFolder+filename, mode="r", encoding="UTF-8")
            content = book.read()
            lines = content.splitlines()
            title = ''
            author = ''
            language = ''
            releaseDate = ''
            for bookLine in lines:
                line = bookLine.strip()
                if "Title:" in line:
                    title = line.replace("Title: ", "")
                elif"Author:" in line:
                    author = line.replace("Author: ", "")
                elif"Language:" in line:
                    language = line.replace("Language: ", "")
                elif"Release Date:" in line:
                    releaseDate = line.replace("Release Date: ", "")
                    releaseDate = releaseDate.split(" [")[0]
            book = Book.objects.create(
                        title=title,
                        author=author,
                        language=language,
                        releaseDate=releaseDate,
                        content=content,
                )
            print(book.title)
            book.save()