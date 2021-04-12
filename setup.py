import setuptools

with open("requirements.txt", "r") as f:
    requirements = f.readlines()


setuptools.setup (
    name='cocktail-wrapper',
    author='clvrk',
    author_email="herufromstatefarm@gmail.com",
    url="https://github.com/clvrk/cocktail-wrapper",
    version='1.0.0',
    packages=['cocktaildb'],
    python_requires=">= 3.6",
    include_package_data=True,
    install_requires=requirements,
    description="An unofficial asynchronous API wrapper for thecocktaildb.com.",
    long_description=None,
    long_description_content_type="text/markdown",
    keywords="api wrapper food cocktails asynchronous library free",
    classifiers = (
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Natural Language :: English",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
    ),
    project_urls = {
        'Funding': 'https://ko-fi.com/foodbot',
        'Support': 'https://discord.gg/csUnYsr',
        'Source': 'https://github.com/clvrk/cocktail-wrapper',
    },
)
