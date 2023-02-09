%if 0%{?fedora}<33||0%{?rhel} >= 8
%undefine __cmake_in_source_build
%endif

Name:           garfieldpp-nightly
Version:        4.0
Release:        2%{?dist}
Summary:        Toolkit for the detailed simulation of particle detectors based on ionisation measurement in gases and semiconductors.

License:        BSD
URL:            https://garfieldpp.web.cern.ch/garfieldpp/
Source:         https://gitlab.cern.ch/garfield/garfieldpp/-/archive/master/garfieldpp-master.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  root
BuildRequires:  root-gdml
BuildRequires:  root-cli
BuildRequires:  gsl-devel
BuildRequires:  cmake
BuildRequires:  geant4-devel
BuildRequires:  gcc-gfortran
BuildRequires:  liburing-devel

Requires:       root
Requires:       root-gdml
Requires:       root-cli
Requires:       gsl
Requires:       liburing
Requires:       geant4-devel

Conflicts:      garfieldpp

%description
Garfield++ is a toolkit for the detailed simulation of particle detectors based
on ionisation measurement in gases and semiconductors. The main area of
application is currently in micropattern gaseous detectors. Garfield++ shares
functionality with the Garfield program. The main differences are the more
up-to-date treatment of electron transport, the possibility to simulate silicon
sensors, and the user interface, which is based on ROOT.

%prep
%autosetup -p1 -n garfieldpp-master

%build
%cmake   -DWITH_EXAMPLES=OFF
%cmake_build

%install
%cmake_install

mkdir -p %{buildroot}%{_sysconfdir}/profile.d

cat > %{buildroot}%{_sysconfdir}/profile.d/%{name}.sh <<EOF
pushd %{_datadir}/Garfield/ >/dev/null; . ./setupGarfield.sh; popd >/dev/null
EOF

cat > %{buildroot}%{_sysconfdir}/profile.d/%{name}.csh <<EOF
pushd %{_datadir}/ >/dev/null; . ./setupGarfield.csh; popd >/dev/null
EOF

%ldconfig_scriptlets

%files
%defattr(-,root,root,-)
%{_libdir}/libGarfield*
%{_libdir}/libmagboltz*
%{_includedir}/Garfield
%{_datadir}/Garfield
%{_datadir}/Heed
%{_sysconfdir}/profile.d/%{name}.sh
%{_sysconfdir}/profile.d/%{name}.csh

%changelog
* Sat Feb 4 11:05:00 CST 2023 Haoxuan Guo <kuohaoxuan@outlook.com> - 4.0-1
- Initial RPM release

* Thu Feb 9 14:01:00 CST 2023 Haoxuan Guo <kuohaoxuan@outlook.com> - 4.0-2
- Add conflicts: garfieldpp
