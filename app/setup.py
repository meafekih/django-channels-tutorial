from setuptools import setup, find_packages

setup(
    name='my-django-crm',
    version='0.1.0',
    description='A Django CRM application',
    packages=find_packages(),
    install_requires=[
        'Django>=3.0',
    ],
    python_requires='>=3.6',
)
