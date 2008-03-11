%define fname	httplib2

Name:		python-httplib2
Summary:	Python HTTP library module
Version:	0.4.0
Release:	%{mkrel 1} 
Source0:	http://httplib2.googlecode.com/files/%{fname}-%{version}.tar.gz
URL:		http://code.google.com/p/httplib2
Group:		System/Libraries
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	MIT
BuildArch:	noarch
BuildRequires:	python
BuildRequires:	python-devel
BuildRequires:	python-setuptools

%description
A comprehensive HTTP client library that supports many features left
out of other HTTP libraries.

%prep
%setup -q -n %{fname}-%{version}

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --root=%{buildroot} --compile --optimize=2

%post

%postun

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{py_puresitedir}/%{fname}
%{py_puresitedir}/%{fname}-%{version}-py%{pyver}.egg-info
