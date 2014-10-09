# based on PLD Linux spec git://git.pld-linux.org/packages/iasl.git
Summary:	ACPI CA for Linux
Name:		iasl
Version:	20140926
Release:	1
License:	distributable (http://acpica.org/downloads/unix_source_code.php)
Group:		Applications/System
Source0:	http://acpica.org/sites/acpica/files/acpica-unix-%{version}.tar.gz
# Source0-md5:	47496f7abe1a73f5911a1e0d304bb246
URL:		http://acpica.org
BuildRequires:	bison
BuildRequires:	flex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ACPI CA contains iasl, an ASL compiler/decompiler. It compiles ASL
(ACPI Source Language) into AML (ACPI Machine Language). This AML is
suitable for inclusion as a DSDT in system firmware. It also can
disassemble AML, for debugging purposes.

%prep
%setup -qn acpica-unix-%{version}

# extract the license
%{__sed} '9,112!d; s/^..//' source/os_specific/service_layers/oslinuxtbl.c > LICENSE

%build
export CC="%{__cc}"
export CFLAGS="%{rpmcflags}"
export LDFLAGS="%{rpmldflags}"

cd generate/unix
%{__make} clean
%ifarch %{x8664}
%{__make} -j1 BITS=64
%else
%{__make} -j1 BITS=32
%endif

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -j1 -C generate/unix install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE changes.txt
%attr(755,root,root) %{_bindir}/*

