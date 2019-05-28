Summary:	Manipulate dm-thin device-mapper target
Name:		thin-provisioning-tools
Version:	0.8.3
Release:	1
License:	GPLv3
Group:		System/Libraries
Url:		https://github.com/jthornber/thin-provisioning-tools
Source0:	https://github.com/jthornber/thin-provisioning-tools/archive/%{name}-%{version}.tar.gz
Source1:	%{name}.rpmlintrc
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(expat)
BuildRequires:	libaio-devel

%description
A suite of tools for manipulating the metadata of the dm-thin
device-mapper target.

%prep
%autosetup -p1
autoreconf -fiv

%build
export CC=gcc
export CXX=g++

%configure \
    --with-optimisation="-Os"

%make_build

%install
%make_install

%files
%doc README.md
%{_sbindir}/*
%{_mandir}/man8/*.8.*
