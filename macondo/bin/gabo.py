from argparse import ArgumentParser
from django.core.management import ManagementUtility
import macondo
import os


parser = ArgumentParser()
subparsers = parser.add_subparsers()


class Gabo:

    def __init__(self):
        start_parser = subparsers.add_parser('start')
        start_parser.add_argument('project_name')
        start_parser.set_defaults(func=self.start)
        publish_parser = subparsers.add_parser('publish')
        publish_parser.add_argument('document')
        publish_parser.set_defaults(func=self.start)

    def start(self, args):
        project_name = args.project_name
        print('Gabo is starting {0}...'.format(project_name))
        path = os.path.dirname(macondo.__file__)
        macondo_project_path = os.path.join(path, 'macondo_project')

        django_args = [
            'django-admin.py',
            'startproject',
            '--template={0}'.format(macondo_project_path),
            project_name
        ]

        django_management = ManagementUtility(django_args)
        django_management.execute()

    def publish(self, args):
        print('Gabo is publishing {0}...'.format(args.document))


def main():
    Gabo()
    args = parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    main()
