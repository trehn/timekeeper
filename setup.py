from setuptools import setup


setup(
    name="timekeeper",
    version="0.1.1",
    description="Send runtime measurements of your code to InfluxDB",
    author="Torsten Rehn",
    author_email="torsten@rehn.email",
    license="ISC",
    url="https://github.com/trehn/timekeeper",
    keywords=["profiling", "profile", "metrics", "instrumentation", "measure", "influxdb"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: ISC License (ISCL)",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Monitoring",
    ],
    install_requires=[
        "influxdb >= 2.0.0",
    ],
    py_modules=['timekeeper'],
)
