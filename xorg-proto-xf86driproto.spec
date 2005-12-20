Summary:	XF86DRI protocol and ancillary headers
Summary(pl):	Nag³ówki protoko³u XF86DRI i pomocnicze
Name:		xorg-proto-xf86driproto
Version:	2.0.2
Release:	0.1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC4/proto/xf86driproto-%{version}.tar.bz2
# Source0-md5:	5c1c51f0603f65d5476e3245dd188b2f
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XF86DRI protocol and ancillary headers.

%description -l pl
Nag³ówki protoko³u XF86DRI i pomocnicze.

%package devel
Summary:	XF86DRI protocol and ancillary headers
Summary(pl):	Nag³ówki protoko³u XF86DRI i pomocnicze
Group:		X11/Development/Libraries
Requires:	libdrm-devel
Requires:	xorg-proto-glproto-devel
Requires:	xorg-proto-xproto-devel

%description devel
XF86DRI protocol and ancillary headers.

%description devel -l pl
Nag³ówki protoko³u XF86DRI i pomocnicze.

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
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc ChangeLog
%{_includedir}/GL/internal/dri_interface.h
%dir %{_includedir}/X11/dri
%{_includedir}/X11/dri/*.h
%{_pkgconfigdir}/xf86driproto.pc
