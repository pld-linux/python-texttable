#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
# python3 not currently supported upstream
%bcond_with	python3 # CPython 3.x module

%define 	module	texttable
Summary:	Python module to generate a formatted text table, using ASCII characters
Name:		python-%{module}
Version:	0.8.4
Release:	1
License:	LGPL v2+
Group:		Development/Libraries
Source0:	https://pypi.python.org/packages/source/t/texttable/texttable-%{version}.tar.gz
# Source0-md5:	6335edbe1bb4edacce7c2f76195f6212
Patch0:		remove-main-from-lib.patch
URL:		https://pypi.python.org/pypi/texttable/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python3}
BuildRequires:	python-2to3
BuildRequires:	python3-setuptools
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python module to generate a formatted text table, using ASCII
characters

%package -n python3-%{module}
Summary:	Python module to generate a formatted text table, using ASCII characters
Group:		Development/Languages

%description -n python3-%{module}
Python module to generate a formatted text table, using ASCII
characters

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1

%if %{with python3}
rm -rf py3
cp -a . py3
2to3 --write --nobackups py3
%endif

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
cd py3
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if %{with python2}
%py_install
%endif

%if %{with python3}
cd py3
%py3_install
%endif

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc PKG-INFO
%{py_sitescriptdir}/texttable*
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc PKG-INFO
%{py3_sitescriptdir}/texttable*
%endif

%clean
rm -rf $RPM_BUILD_ROOT
