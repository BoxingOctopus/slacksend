from setuptools import setup

requirements = [
    'requests',
    'click',
    'toml'
]

setup(
    name='slacksend',
    packages=['slacksend'],
    scripts=['slacksend/slacksend'],
    version='0.5.0',
    description='Send Messages to Slack via Incoming Webhook',
    author='Ryan Draga',
    author_email='ryan.draga@icloud.com',
    url='https://github.com/tuxotaku/slacksend',
    download_url='https://github.com/tuxotaku/slacksend/archive/0.5.0.tar.gz',
    keywords=['slack', 'webhook'],
    python_requires='>=3.0',
    install_requires=requirements,
    classifiers=[],
)
