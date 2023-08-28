import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="serial-logger-niwa", # Replace with your own username
    version="0.0.1",
    author="Gustavo Olivares",
    author_email="gustavo.olivares@niwa.co.nz",
    description="A logger for serial communicating devices",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/niwa/serial_listener_logger",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires = ['pyserial'],
    extras_require = {
        'tests': ['nose >= 1.0']
    }
)