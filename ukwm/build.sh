#!/bin/bash

echo "update packages"
dnf  update -y

echo "build rpm package"
rpmbuild  -ba /root/ukwm.spec   