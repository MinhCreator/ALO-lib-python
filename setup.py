

import setuptools


with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()
setuptools.setup(
    name='ALO package',
    version='1.0.1',
    description='All in one function you need',
    author='MinhCreator VN',
    author_email='buivonhatminhqwer@gmail.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT License',
    packages=["ALO_func"],
    url="https://github.com/MinhCreator/ALO-lib",
    python_requires = ">=3.10",
    zip_safe = False,
    install_requires=[],
    classifiers=[
        'Development Status :: 3 - released',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ])


