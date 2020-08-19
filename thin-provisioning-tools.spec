%global optflags %{optflags} -Oz

Summary:	Manipulate dm-thin device-mapper target
Name:		thin-provisioning-tools
Version:	0.9.0
Release:	1
License:	GPLv3
Group:		System/Libraries
Url:		https://github.com/jthornber/thin-provisioning-tools
Source0:	https://github.com/jthornber/thin-provisioning-tools/archive/%{name}-%{version}.tar.gz
Source1:	%{name}.rpmlintrc
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(expat)
BuildRequires:	libaio-devel
Requires:	expat

%description
A suite of tools for manipulating the metadata of the dm-thin
device-mapper target.

%prep
%autosetup -p1
printf "%s\n" "%{version}-%{release}" > VERSION
autoreconf -fiv

%build
%configure \
    --with-optimisation="%{optflags}"
 
%make_build V=""

%install
%make_install STRIP="/bin/true"

%files
%doc README.md
%{_sbindir}/*
%{_mandir}/man8/*.8.*
