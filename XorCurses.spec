Summary:	A remake of Xor by Astral Software
Summary(pl.UTF-8):	Remake gry Xor stworzonej przez Astral Software
Name:		XorCurses
Version:	0.0.9
Release:	1
License:	GPL v3+
Group:		Applications/Games
Source0:	http://www.jwm-art.net/art/archive/%{name}-%{version}.tar.bz2
# Source0-md5:	0c989feaef1e253125ee8e15c560cdb8
Patch0:		%{name}-Makefile.patch
URL:		http://www.jwm-art.net/dark.php?p=XorCurses
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The idea of Xor (XorCurses) is to roam around a series of mazes
collecting masks. The first level is simply a matter of finding your
way around and locating the masks, but as you progress through the
levels you are introduced to moving objects such as fish and chickens,
and the bombs.

%description -l pl.UTF-8
Ideą Xor (XorCurses) jest wędrowanie przez szereg labiryntów
zbierając maski. Pierwszy poziom jest łatwy, polega tylko na
szukaniu prawidłowej drogi i zbieraniu masek, ale w miarę
przechodzenia do kolejnych poziomów, gracz nauczy się przesuwania
obiektów takich jak ryby, kurczaki czy bomby.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -std=gnu99 -I/usr/include/ncurses -DDATADIR=\\\"%{_datadir}/%{name}/\\\"" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES NEWS README TODO
%attr(755,root,root) %{_bindir}/xorcurses
%{_datadir}/%{name}
