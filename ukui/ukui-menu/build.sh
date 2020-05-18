 echo "install build tools"
 sed -i '/metalink/s/$/\&country=cn/g' /etc/yum.repos.d/*.repo
 dnf -y install gcc gcc-c++ make cmake cmake-rpm-macros autoconf  rpm-build qt5-rpm-macros 
 
 echo "install build dependencies"
 dnf install -y $(grep  BuildRequires /root/ukui-menu.spec |awk '{print $2}')
 strip --remove-section=.note.ABI-tag /usr/lib64/libQt5Core.so.5


 echo "build rpm package"
mkdir -p /root/rpmbuild/SOURCES 
cp /root/plugin-path.patch /root/rpmbuild/SOURCES 
rpmbuild -ba /root/ukui-menu.spec