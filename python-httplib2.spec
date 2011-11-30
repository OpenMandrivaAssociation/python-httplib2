%define fname	httplib2

Name:		python-httplib2
Summary:	Python HTTP library module
Version:	0.7.2
Release:	1
Source0:	http://httplib2.googlecode.com/files/%{fname}-%{version}.tar.gz
URL:		http://code.google.com/p/httplib2
Group:		System/Libraries
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	MIT
BuildArch:	noarch
BuildRequires:	python-setuptools
%py_requires -d

%description
A comprehensive HTTP client library that supports many features left
out of other HTTP libraries.

%prep
%setup -q -n %{fname}-%{version}

%build
%{__python} setup.py build
export PYTHONPATH="%{buildroot}%{_libdir}/python%{pyver}/site-packages"

%install
%{__python} setup.py install --root=%{buildroot}

%files
%defattr(-,root,root)
	%doc README
%{py_puresitedir}/%{fname}
%{py_puresitedir}/%{fname}-%{version}-py%{pyver}.egg-info
