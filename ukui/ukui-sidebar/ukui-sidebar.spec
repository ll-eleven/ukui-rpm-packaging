# enable download source
%undefine _disable_source_fetch

Name:           ukui-sidebar
Version:        1.1.2
Release:        1%{?dist}
Summary:        parallels toolbox for UKUI


License:        GPLv2+
URL:            https://github.com/ukui/ukui-session-manager
Source0:        https://github.com/ukui/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      x86_64
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  glib2-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  dconf-devel
BuildRequires:  gsettings-qt-devel
BuildRequires:  qt5-qtmultimedia-devel

%description
The ukui-sidebar is mainly used in the desktop operating system.
The ukui-sidebar is mainly used in the desktop operating system.
It pops up from the right side of the desktop in the form of a tray,
displaying some application notification messages and some cutting
storage information.

%prep
%setup -q
find . -name "*.pro" | xargs sed -i '/target.path/s/lib/lib64/g' 
%build
  %{qmake_qt5} %_qt5_qmake_flags CONFIG+=enable-by-default  ukui-sidebar.pro
  %make_build

%install
rm -rf $RPM_BUILD_ROOT
%make_install  INSTALL_ROOT=%{buildroot} 

%files
%{_sysconfdir}/xdg/autostart/ukui-sidebar.desktop
%{_bindir}/ukui-sidebar
%{_libdir}/ukui-sidebar
%{_datadir}/ukui-sidebar-notification
