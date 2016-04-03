Summary:	Manipulate dm-thin device-mapper target
Name:		thin-provisioning-tools
Version:	0.6.1
Release:	1
License:	GPLv3
Group:		System/Libraries
Url:		https://github.com/jthornber/thin-provisioning-tools
Source0:	https://github.com/jthornber/thin-provisioning-tools/archive/%{name}-%{version}.tar.gz
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(expat)
BuildRequires:	libaio-devel

%description
A suite of tools for manipulating the metadata of the dm-thin
device-mapper target.

%prep
%setup -q
autoreconf -fiv

%build
%configure \
    --with-optimisation=-Os

%make

%install
%makeinstall_std

%files
%doc README.md

