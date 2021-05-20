Sanpot QuickStart
=================

Simple and smart TCP Honeypot

Installation
---------------

    python3 -m pip install sanpot

Source Code
---------------
https://github.com/sanket9918/TCP-Honeypot

Installation as Debian package
----------------
Get the debian package from github release and run:

    sudo dpkg -i sanpot-1.0.0.deb

Enable service with 
    
    sudo systemctl enable sanpot

Build Config
-----------------
First build the dist using 

    python3 setup.py sdist

Then using the dist build the debian package

    dpkg-deb --build ./deb sanpot-1.0.0.deb <Any version>

Before installation of the program , make sure to remove the service from systemd

    systemctl disable sanpot.service

Install the package using dpkg command

    dpkg -i sanpot-1.0.0.deb 

It will automatically remove previous traces of the installation 

Check the logs at /var/log/sanpot.log


To update the documentation
============================
Install Sphinx
    pip install sphinx

To initialise from the start:
    sphinx quickstart

To build/rebuild the docs :
    cd docs 
    make html 

The format can be changed according to the suitability