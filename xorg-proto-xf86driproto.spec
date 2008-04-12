Summary:	XF86DRI extension headers
Summary(pl.UTF-8):	Nagłówki rozszerzenia XF86DRI
Name:		xorg-proto-xf86driproto
Version:	2.0.4
Release:	1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/proto/xf86driproto-%{version}.tar.bz2
# Source0-md5:	01470d088da3a8a3deefa8e1f45d69cb
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XF86DRI extension headers.

%description -l pl.UTF-8
Nagłówki rozszerzenia XF86DRI.

%package devel
Summary:	XF86DRI extension headers
Summary(pl.UTF-8):	Nagłówki rozszerzenia XF86DRI
Group:		X11/Development/Libraries
Requires:	libdrm-devel
Requires:	xorg-proto-xproto-devel

%description devel
XF86DRI extension headers.

%description devel -l pl.UTF-8
Nagłówki rozszerzenia XF86DRI.

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
%dir %{_includedir}/X11/dri
%{_includedir}/X11/dri/xf86dri*.h
%{_pkgconfigdir}/xf86driproto.pc
