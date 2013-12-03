Name:       cinema
Summary:    Hawaii desktop video player
Version:    0.0.0.20131203.1514656
Release:    1
Group:      Applications/System
License:    BSD
Source0:    cinema-%{version}.tar.bz2
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
#BuildRequires:  desktop-file-utils
Requires:       qt5-qtdeclarative-import-multimedia
#Requires:       qt5-qtmultimedia-plugin-mediaservice-audioengine


%description
Provides video player for Hawaii desktop.


%prep
%setup -q -n cinema


%build
%qmake5 cinema.pro
make %{?jobs:-j%jobs}


%install
rm -rf %{buildroot}
%qmake5_install

#desktop-file-install --delete-original       \
#  --dir %{buildroot}%{_datadir}/applications             \
#   %{buildroot}%{_datadir}/applications/*.desktop


%files
%defattr(-,root,root,-)
%{_bindir}/cinema
%{_libdir}/qt5/qml/cinema/
