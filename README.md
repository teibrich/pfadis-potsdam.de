# Readme

## Dependencies

    pip install pelican fab fabric==1.14.0
    (cd pelican plugins && git submodule init)
    git submodule update --recursive --remote

or directly do a `git clone --recursive`.

## Serving
To start a local server run

    cd pelican
    fab serve

and in a second terminal

    cd pelican
    fab regenerate

## Publishing

    cd pelican
    fab publish

## Environment

My current environment `pip freeze` is

    asn1crypto==0.24.0
    bcrypt==3.1.4
    beautifulsoup4==4.6.0
    blinker==1.4
    certifi==2018.4.16
    cffi==1.11.5
    chardet==3.0.4
    cryptography==2.2.2
    docutils==0.14
    ecdsa==0.13
    enum34==1.1.6
    fab==1.4.2
    fabric==1.14.0
    feedgenerator==1.9
    idna==2.6
    invoke==1.0.0
    ipaddress==1.0.22
    Jinja2==2.10
    Markdown==2.6.11
    MarkupSafe==1.0
    numpy==1.14.3
    paramiko==2.4.1
    pelican==3.7.1
    pyasn1==0.4.3
    pycparser==2.18
    pycrypto==2.6.1
    Pygments==2.2.0
    PyNaCl==1.2.1
    python-dateutil==2.7.3
    pytz==2018.4
    requests==2.18.4
    six==1.11.0
    smartypants==2.0.1
    typogrify==2.0.7
    Unidecode==1.0.22
    urllib3==1.22
    webassets==0.12.1