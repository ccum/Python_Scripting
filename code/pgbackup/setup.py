from setuptools import setup, find_packages

with open('README.rst', 'r') as f:
    readme = f.read()

setup(
    name = 'pgbackup',
    version = '0.1.0',
    descripcion = 'Databases backup locally or to AWS S3',
    long_description = readme,
    author = 'Cesar cueva',
    author_email = 'cueva1487@gmail.com',
    packages = find_packages('src'),
    packages_dir ={'': 'src'},
    install_requires = ['boto3'],
    entry_points={
        'console_scripts': [
            'pgbackup=pgbackup.cli:main',
        ]
    }
)