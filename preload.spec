Summary:	Adaptive readahead daemon
Name:		preload
Version:	0.6.4
Release:	%mkrel 2
License:	GPLv2+
Group:		System/Base
URL:		http://preload.sourceforge.net
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# (fc) 0.6.3-2mdv start after dm and only in graphical login
Patch0:		preload-0.6.3-prcsys.patch
BuildRequires:	glib2-devel >= 2.14
BuildRequires:	help2man
Requires:	logrotate
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
preload is an adaptive readahead daemon that prefetches files mapped by
applications from the disk to reduce application startup time. It runs as a
daemon and gathers information about processes running on the system and
shared-objects that they use. This information is saved in a file to keep
across runs of preload.

%prep
%setup -q
%patch0 -p1 -b .prcsys

%build
%configure2_5x

#parallel build is broken
%make -j1

%install
rm -rf %{buildroot}
%makeinstall_std

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
%defattr(-,root,root)
%doc README AUTHORS ChangeLog TODO THANKS NEWS
%doc doc/index.txt doc/proposal.txt
%{_sbindir}/preload
%{_datadir}/man/man8/preload.8*
%{_sysconfdir}/rc.d/init.d/preload
%config(noreplace) %{_sysconfdir}/preload.conf
%config(noreplace) %{_sysconfdir}/sysconfig/preload
%config(noreplace) %{_sysconfdir}/logrotate.d/preload
%attr(0644,root,root) %ghost %config(missingok,noreplace) %{_var}/log/preload.log
%attr(0644,root,root) %ghost %config(missingok,noreplace) %{_var}/lib/preload/preload.state
%attr(0755,root,root) %dir %{_var}/lib/preload
