%define module typing-inspection
%define uname typing_inspection

Name:		python-typing-inspection
Version:	0.4.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/t/%{module}/%{uname}-%{version}.tar.gz
Summary:	Provides tools to inspect type annotations at runtime
URL:		https://pypi.org/project/typing-inspection/
License:	MIT
Group:		Development/Python
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python-hatchling
BuildRequires:	python-typing-extensions >=4.12.0
Requires:	python-typing-extensions >=4.12.0

%description
python-%{module} provides tools to inspect type annotations at runtime.

%prep
%autosetup -p1 -n %{uname}-%{version}

%build
%py_build

%install
%py_install


%files
%{python3_sitelib}/%{uname}-%{version}.dist-info
%{python3_sitelib}/%{uname}/*.py
%{python3_sitelib}/%{uname}/*.pyi
%{python3_sitelib}/%{uname}/*.typed
%{python3_sitelib}/%{uname}/__pycache__/*.cpython-3*.pyc
%doc README.md
%license LICENSE
