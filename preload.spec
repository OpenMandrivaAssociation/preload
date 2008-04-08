Name: preload
Version: 0.4
Release: %mkrel 1
Summary: Adaptive readahead daemon
License: GPLv2+
Group: System/Applications
URL: http://preload.sourceforge.net
Source0: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}
BuildRequires: libglib-devel
BuildRequires: help2man
Requires: logrotate
# patches from fedora package
Patch0: preload.init.in.patch
Patch1: preload.logrotate.in.patch
Patch2: preload.cmdline.c.patch
Patch3: preload.conf.in.patch
Patch4: preload.proc.c.patch
Patch5: preload.prophet.c.patch
Patch6: preload.readahead.c.patch
Patch7: preload.readahead.h.patch
Patch8: preload.state.c.patch

%description
preload is an adaptive readahead daemon that prefetches files mapped by
applications from the disk to reduce application startup time. It runs as a
daemon and gathers information about processes running on the system and
shared-objects that they use. This information is saved in a file to keep
across runs of preload.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

%build
# needed for correct localstatedir location 
%define _localstatedir %{_var}
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall

# already as %%doc
rm -f %{buildroot}/%{_docdir}/preload-%{version}/index.txt
rm -f %{buildroot}/%{_docdir}/preload-%{version}/proposal.txt

%clean
rm -rf %{buildroot}

%post
%_post_service preload

%preun
%_preun_service preload

%files
%defattr(-,root,root, -)
%doc README AUTHORS COPYING ChangeLog TODO THANKS NEWS
%doc doc/index.txt doc/proposal.txt
%{_sbindir}/preload
%{_datadir}/man/man8/preload.8*
%{_sysconfdir}/rc.d/init.d/preload
%config(noreplace) %{_sysconfdir}/preload.conf
%config(noreplace) %{_sysconfdir}/sysconfig/preload
%config(noreplace) %{_sysconfdir}/logrotate.d/preload
%attr(0644,root,root) %ghost %config(missingok,noreplace) %{_localstatedir}/log/preload.log
%attr(0644,root,root) %ghost %config(missingok,noreplace) %{_localstatedir}/lib/preload/preload.state
%attr(0755,root,root) %dir %{_localstatedir}/lib/preload

