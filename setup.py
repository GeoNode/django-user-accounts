from setuptools import setup, find_packages

import account


setup(
    name="geonode-user-accounts",
    version=account.__version__,
    author="Brian Rosner",
    author_email="brosner@gmail.com",
    description="a Django user account app",
    long_description=open("README.rst").read(),
    license="MIT",
    url="https://github.com/GeoNode/geonode-user-accounts",
    packages=find_packages(),
    install_requires=[

        "django-appconf>=1.0.1",
        "pytz>=2015.6"
    ],
    zip_safe=False,
    package_data={
        "account": [
            "locale/*/LC_MESSAGES/*",
        ],
    },
    tests_requires=[
        "pinax_theme_bootstrap",
    ],
    test_suite="runtests.runtests",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Framework :: Django",
    ],
    include_package_data=True,
)
