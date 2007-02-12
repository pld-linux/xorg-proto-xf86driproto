Summary:	XF86DRI protocol and ancillary headers
Summary(pl.UTF-8):   Nagłówki protokołu XF86DRI i pomocnicze
Name:		xorg-proto-xf86driproto
Version:	2.0.3
Release:	2
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/proto/xf86driproto-%{version}.tar.bz2
# Source0-md5:	e4a282cfd708b8892fca4425fee9cd7b
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XF86DRI protocol and ancillary headers.

%description -l pl.UTF-8
Nagłówki protokołu XF86DRI i pomocnicze.

%package devel
Summary:	XF86DRI protocol and ancillary headers
Summary(pl.UTF-8):   Nagłówki protokołu XF86DRI i pomocnicze
Group:		X11/Development/Libraries
Requires:	libdrm-devel
Requires:	xorg-proto-glproto-devel
Requires:	xorg-proto-xproto-devel

%description devel
XF86DRI protocol and ancillary headers.

%description devel -l pl.UTF-8
Nagłówki protokołu XF86DRI i pomocnicze.

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
%doc COPYING ChangeLog
%{_includedir}/GL/internal/dri_interface.h
%dir %{_includedir}/X11/dri
%{_includedir}/X11/dri/*.h
%{_pkgconfigdir}/xf86driproto.pc
