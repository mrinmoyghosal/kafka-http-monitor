import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='kafka-http-monitor',
    version='0.1.0',
    packages=setuptools.find_packages(exclude=["tests"]),
    include_package_data=True,
    python_requires=">=3.9",
    install_requires=[
        'confluent-kafka>=1.5.0',
        'postgres>=3.0.0',
        'APScheduler>=3.6.3',
        'aiohttp>=3.7.2'
    ],
    entry_points={
        'console_scripts': [
            'start_producer = service.start_producer:main',
            'start_consumer = service.start_consumer:main'
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Kafka',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.9',
    ],
)
