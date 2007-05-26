#
Summary:	Applet to adjust shadow position for composited window managers
Name:		gnome-sunflower-applet
Version:	0.6
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://dekorte.homeip.net/download/sunflower/sunflower_applet-%{version}.tar.gz
# Source0-md5:	f1f7adea69d185ae8c93dbc726c5eb10
URL:		http://dekorte.homeip.net/download/sunflower/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-panel-devel
#BuildRequires:	intltool
#BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

Sunflower Applet changes the shadow on the windows managed by compiz
when the decorator plugin is enabled and with beryl when emerald is
used as the decorator. The shadow on the window moves from left to
right from sunrise to sunset, and stays static from sunset to sunrise,
as if the shadow is being cast by the "sun" moving right to left over
your windows.

After you install it, select the panel you want to add it to, right
click and select "Add to Panel" then scroll thru the list and select
Sunflower. A panel applet should appear and your window shadow may
adjust. Watch it during the day and the shadow should slowly slide
from left to right.

%prep
%setup -q -n sunflower_applet-%{version}

%build
# if ac/am/* rebuilding is necessary, do it in this order and add
# appropriate BuildRequires
#%%{__intltoolize}
#%%{__gettextize}
#%%{__libtoolize}
%{__aclocal}
%{__autoconf}
#%%{__autoheader}
%{__automake}
cp -f /usr/share/automake/config.sub .
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%{_libdir}/bonobo/servers/SunflowerApplet.server
%attr(755,root,root) %{_libdir}/sunflower
%{_pixmapsdir}/sunflower.png
