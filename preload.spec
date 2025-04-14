Summary:	Adaptive readahead daemon
Name:		preload
Version:	0.6.4
Release:	19
License:	GPLv2+
Group:		System/Base
Url:		https://preload.sourceforge.net
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:	%{name}.service
BuildRequires:	help2man
BuildRequires:	pkgconfig(glib-2.0)
Requires:	logrotate

BuildSystem:	autotools

%patchlist
# (fc) 0.6.3-2mdv start after dm and only in graphical login
preload-0.6.3-prcsys.patch

%description
preload is an adaptive readahead daemon that prefetches files mapped by
applications from the disk to reduce application startup time. It runs as a
daemon and gathers information about processes running on the system and
shared-objects that they use. This information is saved in a file to keep
across runs of preload.


%files
%license COPYING
%doc README AUTHORS COPYING ChangeLog TODO THANKS NEWS
%doc doc/index.txt doc/proposal.txt
%{_bindir}/preload
%{_datadir}/man/man8/preload.8.*
%{_unitdir}/%{name}.service
%config(noreplace) %{_sysconfdir}/preload.conf
%config(noreplace) %{_sysconfdir}/sysconfig/preload
%config(noreplace) %{_sysconfdir}/logrotate.d/preload
%attr(0644,root,root) %ghost %config(missingok,noreplace) %{_localstatedir}/log/preload.log
%attr(0644,root,root) %ghost %config(missingok,noreplace) %{_localstatedir}/lib/preload/preload.state
%attr(0755,root,root) %dir %{_localstatedir}/lib/preload

#----------------------------------------------------------------------

%prep
%autosetup -p1

%build
%configure

#parallel build is broken
%make_build

%install
%make_install

# systemd unit
install -Dm644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service

# already as %%doc
rm -rf %{buildroot}%{_docdir}/*
rm -rf %{buildroot}%{_sysconfdir}/rc.d

