Summary:	Adaptive readahead daemon
Name:		preload
Version:	0.6.4
Release:	7
License:	GPLv2+
Group:		System/Base
URL:		http://preload.sourceforge.net
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# (fc) 0.6.3-2mdv start after dm and only in graphical login
Patch0:		preload-0.6.3-prcsys.patch
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	help2man
Requires:	logrotate

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
%makeinstall_std

# already as %%doc
rm -f %{buildroot}/%{_docdir}/preload-%{version}/index.txt
rm -f %{buildroot}/%{_docdir}/preload-%{version}/proposal.txt

%post
%_post_service preload

%preun
%_preun_service preload

%files
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


%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 0.6.4-4mdv2011.0
+ Revision: 667821
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.6.4-3mdv2011.0
+ Revision: 607206
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.6.4-2mdv2010.1
+ Revision: 523706
- rebuilt for 2010.1

* Sun May 24 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.4-1mdv2010.0
+ Revision: 379216
- update to new version 0.6.4
- drop patches 1, 2, 3 and 4, as they were merged by upstream

* Fri Feb 06 2009 Frederic Crozat <fcrozat@mandriva.com> 0.6.3-4mdv2009.1
+ Revision: 338033
- Patch1 (SVN): fix crahs with --nice
- Patch2 (SVN): clearify default config
- Patch3 (SVN): use glib 2.14 features
- Patch4 (SVN): fix default umask

* Fri Sep 26 2008 Frederic Crozat <fcrozat@mandriva.com> 0.6.3-3mdv2009.0
+ Revision: 288665
- update patch0 to fix default runlevel and not start if readahead-collector is running

* Wed Sep 24 2008 Frederic Crozat <fcrozat@mandriva.com> 0.6.3-2mdv2009.0
+ Revision: 287908
- Remove patch10, not needed on Mandriva
- Patch0: start after dm and only in graphical login

* Fri Aug 22 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.3-1mdv2009.0
+ Revision: 275164
- drop all patches, they were merged upstream
- Patch10: start preload service as a last one
- do not define localstatedir
- update to new version 0.6.3

* Mon Jul 28 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4-2mdv2009.0
+ Revision: 250751
- don't use parallel build
- fix buildrequires
- spec file clean
- do not package COPYING file

  + Ademar de Souza Reis Jr <ademar@mandriva.com.br>
    - add preload-use-ionice.patch, which makes preload
      run under 'ionice -c 3' (Idle priority for the
      I/O scheduler).
    - import preload


