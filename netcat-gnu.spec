%define real_name netcat

Summary:	Networking utility that manages TCP and UDP connections
Name:		netcat-gnu
Version:	0.7.1
Release:	15
License:	GPLv2
Group:		Networking/Other
Url:		http://netcat.sourceforge.net/
Source0:	http://osdn.dl.sourceforge.net/sourceforge/netcat/netcat-%{version}.tar.bz2
Source1:	http://netcat.sourceforge.net/signatures/md5sums.txt
Source2:	http://netcat.sourceforge.net/signatures/netcat-%{version}.tar.bz2.asc
Provides:	netcat = 1.0
Conflicts:	netcat-traditional
Conflicts:	netcat-openbsd

%description
Netcat is a featured networking utility which reads and writes data across
network connections, using the TCP/IP protocol.

It is designed to be a reliable "back-end" tool that can be used directly or
easily driven by other programs and scripts. At the same time, it is a
feature-rich network debugging and exploration tool, since it can create
almost any kind of connection you would need and has several interesting
built-in capabilities.

%prep
%setup -qn %{real_name}-%{version}

%build
%configure2_5x
%make

%install
%makeinstall_std
(cd %{buildroot}%{_infodir} && ln -s netcat.info nc.info)
(cd %{buildroot}%{_mandir}/man1 && ln -s netcat.1 nc.1)

rm -f doc/drafts/Makefile*

%find_lang %{real_name}

%files -f %{real_name}.lang
%doc AUTHORS COPYING ChangeLog NEWS README TODO doc/migration doc/drafts
%{_bindir}/netcat
%{_bindir}/nc
%{_infodir}/netcat.info*
%{_infodir}/nc.info*
%{_mandir}/man1/netcat.1*
%{_mandir}/man1/nc.1*

