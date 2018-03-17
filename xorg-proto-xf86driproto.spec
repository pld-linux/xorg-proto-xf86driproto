# NOTE: now maintained in xorg-proto-xorgproto.spec
Summary:	XF86DRI extension headers
Summary(pl.UTF-8):	Pliki nagłówkowe rozszerzenia XF86DRI
Name:		xorg-proto-xf86driproto
Version:	2.1.1
Release:	2.1
License:	MIT
Group:		X11/Development/Libraries
Source0:	https://xorg.freedesktop.org/releases/individual/proto/xf86driproto-%{version}.tar.bz2
# Source0-md5:	1d716d0dac3b664e5ee20c69d34bc10e
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros >= 1.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XF86DRI (XFree86 Direct Rendering Infrastructure) extension defines a
protocol to allow user applications to access the video hardware
without requiring data to be passed through the X server.

%description -l pl.UTF-8
Rozszerzenie XF86DRI (XFree86 Direct Rendering Infrastructure)
definiuje protokół pozwalający aplikacjom użytkownika na dostęp do
sprzętu wyświetlającego obraz bez potrzeby przekazywania danych
poprzez serwer X.

%package devel
Summary:	XF86DRI extension headers
Summary(pl.UTF-8):	Pliki nagłówkowe rozszerzenia XF86DRI
Group:		X11/Development/Libraries
Requires:	libdrm-devel
Requires:	xorg-proto-xproto-devel

%description devel
XF86DRI (XFree86 Direct Rendering Infrastructure) extension defines a
protocol to allow user applications to access the video hardware
without requiring data to be passed through the X server.

%description devel -l pl.UTF-8
Rozszerzenie XF86DRI (XFree86 Direct Rendering Infrastructure)
definiuje protokół pozwalający aplikacjom użytkownika na dostęp do
sprzętu wyświetlającego obraz bez potrzeby przekazywania danych
poprzez serwer X.

%prep
%setup -q -n xf86driproto-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%dir %{_includedir}/X11/dri
%{_includedir}/X11/dri/xf86dri*.h
%{_pkgconfigdir}/xf86driproto.pc
