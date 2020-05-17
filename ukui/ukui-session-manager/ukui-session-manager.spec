# enable download source
%undefine _disable_source_fetch

Name:           ukui-session-manager
Version:        2.0.0
Release:        1%{?dist}
Summary:        Session manager of the UKUI desktop environment


License:        GPLv2+
URL:            https://github.com/ukui/ukui-session-manager
Source0:        https://github.com/ukui/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      x86_64
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  kf5-kidletime-devel
BuildRequires:  qt5-linguist
BuildRequires:  gsettings-qt-devel
BuildRequires:  libXtst-devel
BuildRequires:  libqtxdg-devel
BuildRequires:  systemd-devel

Requires: ukui-themes

Provides: x-session-manager


%description
 This package contains a session that can be started from a display
 manager such as lightdm. It will load all necessary applications for
 a full-featured user session.
 This package contain the session manager component.

%prep
%setup -q

%build
%cmake

%install
%make_install INSTALL_ROOT=%{buildroot}

%files
%{_datadir}/ukui/translations/ukui-session-manager/
%{_datadir}/xsessions/ukui.desktop
%{_datadir}/glib-2.0/schemas/org.ukui.session.gschema.xml
%{_bindir}/ukui-session
%{_bindir}/ukui-session-tools
