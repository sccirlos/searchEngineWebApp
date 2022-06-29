#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
#import views


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'search_engineUI.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)



if __name__ == '__main__':
    main()
    # # Reading zip file, code segment from Dr. Chen.
    # allHTMLFiles = [name for name in archive.namelist() \
    #          if name.endswith('.html') or name.endswith('.htm')]

    # # Store HTML files into a Dic
    # invertedIndex, documentInformation = traverseHTML(allHTMLFiles)

    # webSearch(invertedIndex, documentInformation)