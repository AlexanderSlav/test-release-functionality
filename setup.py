from setuptools import setup

packages = ["test_package"]

package_data = {"": ["*"]}

setup_kwargs = {
    "name": "test_package",
    "version": "0.1.0",
    "description": "",
    "long_description": None,
    "author": "alexander.slavutin",
    "author_email": "alexander.slavutin@gmail.com",
    "maintainer": "alexander.slavutin",
    "maintainer_email": "alexander.slavutin@gmail.com",
    "url": None,
    "packages": packages,
    "package_data": package_data,
    "python_requires": ">=3.7,<4.0"
}

setup(**setup_kwargs)