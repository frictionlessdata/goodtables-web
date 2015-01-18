from setuptools import setup, find_packages


setup(
    name='Tabular Validator Web',
    version='0.1.1-alpha',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask==0.10.1',
        'Flask-Babel==0.9',
        'Flask-WTF==0.10.3',
        'Celery==3.1.17',
        'SQLAlchemy==0.9.8',
        'gunicorn==19.1.1',
        'pytz'
    ],
    dependency_links=[
        'git+https://github.com/okfn/tabular-validator.git#egg=tabular_validator'
    ]
)