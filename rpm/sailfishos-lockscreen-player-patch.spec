# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       sailfishos-lockscreen-voicemail-patch

# >> macros
BuildArch: noarch
# << macros

Summary:   Lockscreen voicemail notification patch 
Version:    0.0.5
Release:    1
Group:      Qt/Qt
License:    Public Domain
Source0:    %{name}-%{version}.tar.bz2
Requires:   patchmanager
Requires:   sailfish-version >= 1.1.4

%description
Lockscreen patch enabling to show an icon when you have a voicemail message to read.


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
mkdir -p %{buildroot}/usr/share/patchmanager/patches/sailfishos-lockscreen-player-patch
cp -r patch/* %{buildroot}/usr/share/patchmanager/patches/sailfishos-lockscreen-player-patch
# << install pre

# >> install post
# << install post

%files
%defattr(-,root,root,-)
%{_datadir}/patchmanager/patches/sailfishos-lockscreen-player-patch
# >> files
# << files
