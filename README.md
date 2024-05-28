# Techworks Best Practices in AI Guide

This repository contains the Techworks Best Practices in AI guide. 

You can find the published version of the guide
[*here*](https://techworkshub.github.io/best-practice-guide/)

## Installing requirements

This guidance is maintained in 
[*Sphinx*](https://www.sphinx-doc.org/en/master/). It currently uses a version
of the [*furo*](https://github.com/pradyunsg/furo/tree/main) theme. Sphinx has
strong integration with Python, which makes installation fairly easy.

Requirements:
* Python 3.9+
* Sphinx
* Furo theme

To install:
* Install [Python](https://realpython.com/installing-python/)

Then:
    pip install -U sphinx

And:
    pip install -U furo

## Building 

To build the guide in html format run the following in a terminal in the root
directory of the repository:

    sphinx-build -b html source build

To build the guide in pdf format:

    sphinx-build -b html source build