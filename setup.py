import os
import io
from setuptools import find_packages, setup

with io.open('README.md', encoding='utf-8') as f:
    README = f.read()
try:
    import pypandoc
    README = pypandoc.convert(README, 'rst', 'md')
    README = README.replace('\r', '')
    with io.open('README.rst', mode='w', encoding='utf-8') as f:
        f.write(README)
except (ImportError, OSError):
    print("!!! Can't convert README.md - install pandoc and/or pypandoc.")


with io.open('requirements.txt', encoding='utf8') as f:
    install_requires = [l.strip() for l in f.readlines() if
                        l.strip() and not l.startswith('#')]

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-sql',
    version='1.0',
    packages=find_packages(exclude=['sqlapp.tests']),
    include_package_data=True,
    install_requires=install_requires,
    license='MIT License',
    description='A simple app for executing SQL queries in Django admin panel',
    long_description=README,
    url='https://github.com/luminousmen/django-sql',
    author='Kirill Bobrov',
    author_email='miaplanedo@gmail.com',
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ]
)
