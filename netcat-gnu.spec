%define real_name netcat

Name:           netcat-gnu
Version:        0.7.1
Release:        12
Epoch:          0
Summary:        Networking utility that manages TCP and UDP connections
License:        GPL
Group:          Networking/Other
URL:            http://netcat.sourceforge.net/
Source0:        http://osdn.dl.sourceforge.net/sourceforge/netcat/netcat-%{version}.tar.bz2
Source1:        http://netcat.sourceforge.net/signatures/md5sums.txt
Source2:        http://netcat.sourceforge.net/signatures/netcat-%{version}.tar.bz2.asc
Obsoletes:      netcat <= 0.7.1-4mdv
Provides:       netcat = 1.0
Conflicts:      netcat-traditional
Conflicts:      netcat-openbsd

%description
Netcat is a featured networking utility which reads and writes data across
network connections, using the TCP/IP protocol.

It is designed to be a reliable "back-end" tool that can be used directly or
easily driven by other programs and scripts. At the same time, it is a
feature-rich network debugging and exploration tool, since it can create
almost any kind of connection you would need and has several interesting
built-in capabilities.

%prep
%setup -q -n %{real_name}-%{version}

%build
%{configure2_5x}
%{make}

%install
%{makeinstall}
(cd %{buildroot}%{_infodir} && %{__ln_s} netcat.info nc.info)
(cd %{buildroot}%{_mandir}/man1 && %{__ln_s} netcat.1 nc.1)

%{__rm} doc/drafts/Makefile*

%find_lang %{real_name}

%files -f %{real_name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README TODO doc/migration doc/drafts
%{_bindir}/netcat
%{_bindir}/nc
%{_infodir}/netcat.info*
%{_infodir}/nc.info*
%{_mandir}/man1/netcat.1*
%{_mandir}/man1/nc.1*


%changelog
* Sat Dec 11 2010 Oden Eriksson <oeriksson@mandriva.com> 0:0.7.1-8mdv2011.0
+ Revision: 620486
- the mass rebuild of 2010.0 packages

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 0:0.7.1-7mdv2010.0
+ Revision: 440306
- rebuild

* Wed Jan 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0:0.7.1-6mdv2009.1
+ Revision: 332127
- provides a versionned netcat virtual package

* Mon Jan 19 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0:0.7.1-5mdv2009.1
+ Revision: 331438
- package renaming
- provides netcat virtual package
- package renaming

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 0:0.7.1-4mdv2009.0
+ Revision: 253761
- rebuild

* Thu Jan 03 2008 Olivier Blin <oblin@mandriva.com> 0:0.7.1-2mdv2008.1
+ Revision: 140994
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Apr 19 2007 David Walluck <walluck@mandriva.org> 0:0.7.1-2mdv2008.0
+ Revision: 15160
- bump release
- use only netcat, not nc

* Thu Apr 19 2007 David Walluck <walluck@mandriva.org> 0:0.7.1-1mdv2008.0
+ Revision: 15148
- Import netcat

