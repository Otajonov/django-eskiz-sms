from setuptools import find_packages, setup


__version__ = "0.1.6"

f = open("README.rst")
readme = f.read()
f.close()


setup(
    name="django-eskiz-sms",
    version=__version__,
    description=(
        "Djangoda Eskiz.Uz API orqali SMS yuborish uchun eng mukammal paket"
    ),
    long_description=readme,
    author="Ro'zmat Otajonov",
    author_email="hello@tijorat.org",
    maintainer="Ro'zmat Otajonov",
    maintainer_email="hello@tijorat.org",
    url="https://github.com/Otajonov/django-eskiz-sms",
    packages=find_packages(exclude=["tests*"]),
    
    project_urls={
        "Yordam": "https://t.me/RozmatOtajonov",
        "GitHub Soure Code": "https://github.com/Otajonov/django-eskiz-sms",
    },
    
    include_package_data=True,
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.0",
        "Framework :: Django :: 4.1",
        "Framework :: Django :: 4.2",
        "Framework :: Django :: 5.0",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    zip_safe=False,
    python_requires=">=3.7",
    install_requires=[
        "Django>=3.2",
        "requests",
    ],
)
