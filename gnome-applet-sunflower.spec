Summary:	Applet to adjust shadow position for composited window managers
Summary(pl.UTF-8):	Aplet regulujący położenie cienia dla składających zarządców okien
Name:		gnome-applet-sunflower
Version:	0.7.1
Release:	1
License:	GPL v2
Group:		X11/Applications
#Source0-Download: http://dekorte.homeip.net/download/download.php#sunflower
Source0:	http://dekorte.homeip.net/download/sunflower/sunflower_applet-%{version}.tar.gz
# Source0-md5:	11f0387730991d937c54a2dfc508f757
URL:		http://dekorte.homeip.net/download/sunflower/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	gnome-panel-devel >= 2.0
BuildRequires:	pkgconfig
Obsoletes:	gnome-sunflower-applet
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

%description -l pl.UTF-8
Sunflower Applet zmienia cienie na okienkach zarządzanych przez
compiza kiedy wtyczka dekoratora jest włączona oraz przez beryla kiedy
emerald jest używany jako dekorator. Cień na okienkach przesuwa się od
lewej do prawej od wschodu do zachodu słońca, a pozostaje stały od
zachodu do wschodu, tak jakby cień był rzucany przez "słońce"
przesuwające się z prawej do lewej ponad okienkami.

Po zainstalowaniu należy wybrać panel gdzie dodać aplet, kliknąć
prawym klawiszem myszy i wybrać "Dodaj do panelu", a następnie
przewinąć listę i wybrać Sunflower. Aplet panelu powinien się pojawić,
a cienie okienek będą mogły się zmieniać. W czasie dnia powinno być
widać cienie powoli przesuwające się od lewej do prawej.

%prep
%setup -q -n sunflower_applet-%{version}

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

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/sunflower
%{_libdir}/bonobo/servers/SunflowerApplet.server
%{_pixmapsdir}/*.png
