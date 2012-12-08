%define module	httplib2

Name:		python-httplib2
Summary:	Comprehensive HTTP client library for Python
Version:	0.7.4
Release:	1
Source0:	http://httplib2.googlecode.com/files/%{module}-%{version}.tar.gz
URL:		http://code.google.com/p/httplib2
Group:		System/Libraries
License:	MIT
BuildArch:	noarch
BuildRequires:	python-setuptools
%py_requires -d

%description
A comprehensive HTTP client library that supports many features left
out of other HTTP libraries.

%prep
%setup -q -n %{module}-%{version}

%build
%{__python} setup.py build

%install
PYTHONDONTWRITEBYTECODE= %{__python} setup.py install --root=%{buildroot}

%files
%defattr(-,root,root)
%doc README
%py_sitedir/httplib2-*
%py_sitedir/httplib2/*


%changelog
* Sun Mar 18 2012 Lev Givon <lev@mandriva.org> 0.7.4-1
+ Revision: 785475
- Update to 0.7.4.

* Fri Mar 02 2012 Lev Givon <lev@mandriva.org> 0.7.3-1
+ Revision: 781855
- Update to 0.7.3.

* Wed Nov 30 2011 Alexander Khrukin <akhrukin@mandriva.org> 0.7.2-1
+ Revision: 735796
- cooker fix
- spec file fix in files py-egg removed
- spec file fix
- spec file fix
- version update 0.7.2

* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 0.6.0-3
+ Revision: 667937
- mass rebuild

* Sat Oct 30 2010 Michael Scherer <misc@mandriva.org> 0.6.0-2mdv2011.0
+ Revision: 590615
- rebuild for python 2.7

* Fri Jan 08 2010 Emmanuel Andry <eandry@mandriva.org> 0.6.0-1mdv2010.1
+ Revision: 487795
- New version 0.6.0

* Sat Jan 03 2009 Funda Wang <fwang@mandriva.org> 0.4.0-3mdv2009.1
+ Revision: 323729
- rebuild

* Thu Mar 13 2008 Adam Williamson <awilliamson@mandriva.org> 0.4.0-2mdv2008.1
+ Revision: 187368
- requires python

* Wed Mar 12 2008 Adam Williamson <awilliamson@mandriva.org> 0.4.0-1mdv2008.1
+ Revision: 186995
- import python-httplib2


