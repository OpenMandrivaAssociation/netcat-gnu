Name:           netcat
Version:        0.7.1
Release:        %mkrel 4
Epoch:          0
Summary:        Networking utility that manages TCP and UDP connections
License:        GPL
Group:          Networking/Other
URL:            http://netcat.sourceforge.net/
Source0:        http://osdn.dl.sourceforge.net/sourceforge/netcat/netcat-%{version}.tar.bz2
Source1:        http://netcat.sourceforge.net/signatures/md5sums.txt
Source2:        http://netcat.sourceforge.net/signatures/netcat-%{version}.tar.bz2.asc
Requires(post): info-install
Requires(preun): info-install
# FIXME: This should probably use update-alternatives instead
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Netcat is a featured networking utility which reads and writes data across
network connections, using the TCP/IP protocol.

It is designed to be a reliable "back-end" tool that can be used directly or
easily driven by other programs and scripts. At the same time, it is a
feature-rich network debugging and exploration tool, since it can create
almost any kind of connection you would need and has several interesting
built-in capabilities.

%prep
%setup -q

%build
%{configure2_5x}
%{make}

%install
%{__rm} -rf %{buildroot}
%{makeinstall}
%{__rm} %{buildroot}%{_bindir}/nc
#(cd %{buildroot}%{_infodir} && %{__ln_s} netcat.info nc.info)
#(cd %{buildroot}%{_mandir}/man1 && %{__ln_s} netcat.1 nc.1)

%{__rm} doc/drafts/Makefile*

%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%post
%_install_info %{name}

%preun
%_remove_install_info %{name}

%files -f %{name}.lang
%defattr(0644,root,root,0755)
%doc AUTHORS COPYING ChangeLog NEWS README TODO doc/migration doc/drafts
%attr(0755,root,root) %{_bindir}/netcat
#%{_bindir}/nc
%{_infodir}/netcat.info*
#%{_infodir}/nc.info*
%{_mandir}/man1/netcat.1*
#%{_mandir}/man1/nc.1*
