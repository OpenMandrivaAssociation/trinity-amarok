%bcond clang 1
%bcond gamin 1
%bcond daap 0
%bcond ifp 1
%bcond gpod 1
%bcond mtp 1
%bcond njb 1
%bcond libvisual 1
%bcond inotify 1
%bcond xine 1
%bcond yauap 1
%bcond akode 1

# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif
%define pkg_rel 2

%define tde_pkg amarok
%define tde_prefix /opt/trinity
%define tde_bindir %{tde_prefix}/bin
%define tde_confdir %{_sysconfdir}/trinity
%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_mandir %{tde_datadir}/man
%define tde_tdeappdir %{tde_datadir}/applications/tde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%define _debugsource_template %{nil}

%define tarball_name %{tde_pkg}-trinity


Name:		trinity-%{tde_pkg}
Epoch:		%{tde_epoch}
Version:	1.4.10
Release:	%{?tde_version}_%{?!preversion:%{pkg_rel}}%{?preversion:0_%{preversion}}%{?dist}
Summary:	Media player for TDE
Group:		Applications/Multimedia
URL:		http://www.trinitydesktop.org/
#Url:		http://amarok.kde.org

License:	GPLv2+

#Vendor:		Trinity Desktop
#Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:		%{tde_prefix}

Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/applications/multimedia/%{tarball_name}-%{tde_version}%{?preversion:~%{preversion}}.tar.xz

BuildSystem:    cmake
BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_SKIP_RPATH=OFF
BuildOption:    -DCMAKE_SKIP_INSTALL_RPATH=OFF
BuildOption:    -DCMAKE_BUILD_WITH_INSTALL_RPATH=ON
BuildOption:    -DCMAKE_INSTALL_RPATH="%{tde_libdir}"
BuildOption:    -DCMAKE_NO_BUILTIN_CHRPATH=ON
BuildOption:    -DBIN_INSTALL_DIR=%{tde_bindir}
BuildOption:    -DCONFIG_INSTALL_DIR="%{tde_confdir}"
BuildOption:    -DINCLUDE_INSTALL_DIR=%{tde_tdeincludedir}
BuildOption:    -DLIB_INSTALL_DIR=%{tde_libdir}
BuildOption:    -DSHARE_INSTALL_PREFIX=%{tde_datadir}
BuildOption:    -DWITH_KONQSIDEBAR=ON
BuildOption:    -DWITH_SYSTEM_SQLITE=ON
BuildOption:    -DBUILD_ALL=ON
BuildOption:    -DWITH_OPENGL=ON
%{?with_libvisual:BuildOption:    -DWITH_LIBVISUAL=ON}
%{?with_xine:BuildOption:    -DWITH_XINE=ON} 
%{?!with_xine:BuildOption:    -DWITH_XINE=OFF}
%{?with_yauap:BuildOption:    -DWITH_YAUAP=ON}
%{?with_akode:BuildOption:    -DWITH_AKODE=ON}
%{!?with_akode:BuildOption:    -DWITH_AKODE=OFF}
%{?with_gpod:BuildOption:    -DWITH_IPOD=ON}
%{?with_ifp:BuildOption:    -DWITH_IFP=ON}
%{?with_njb:BuildOption:    -DWITH_NJB=ON}
%{?with_mtp:BuildOption:    -DWITH_MTP=ON}
%{!?with_daap:BuildOption:    -DWITH_DAAP=OFF}
%{?with_inotify:BuildOption:    -DWITH_INOTIFY=ON}

BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	trinity-konqueror-devel >= %{tde_version}

BuildRequires:	trinity-filesystem >= %{tde_version}
Requires:		trinity-filesystem >= %{tde_version}

BuildRequires:	desktop-file-utils
BuildRequires:	trinity-tde-cmake >= %{tde_version}

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	pkgconfig
BuildRequires:	gettext

# ACL support
BuildRequires:  pkgconfig(libacl)

# ALSA support
BuildRequires:  pkgconfig(alsa)

# PCRE2 support
BuildRequires:  pkgconfig(libpcre2-posix)

# LIBTOOL
BuildRequires:	libtool

BuildRequires:  pkgconfig(libusb)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:	mysql-devel
BuildRequires:	taglib-devel

# SDL support
BuildRequires:  pkgconfig(sdl)

# SQLITE3 support
BuildRequires:  pkgconfig(sqlite3)

# POSTGRESQL support
BuildRequires:  pkgconfig(libpq)

# IDN support
BuildRequires:	pkgconfig(libidn)

# GAMIN support
%{?with_gamin:BuildRequires:	pkgconfig(gamin)}

# DBUS support
BuildRequires:  pkgconfig(dbus-1)

# DBUS-(T)QT support
BuildRequires:	trinity-dbus-tqt-devel >= 1:0.63

# IFP support
%{?with_ifp:BuildRequires:	%{_lib}ifp-devel}

# GPOD (ipod) support
%{?with_gpod:BuildRequires:	pkgconfig(libgpod-1.0) >= 0.4.2}

# MTP players
%{?with_mtp:BuildRequires:  pkgconfig(libmtp)}

# Creative Nomad Jukebox
%{?with_njb:BuildRequires:  pkgconfig(libnjb)}

# VISUAL support
%{?with_libvisual:BuildRequires:  pkgconfig(libvisual-0.4)}

# INOTIFY support
%{?with_inotify:BuildRequires:	%{_lib}inotifytools-devel}

# XINE support
%if %{with xine}
BuildRequires:  pkgconfig(libxine)
Requires:       xine-plugins
%endif

# AKODE support
%{?with_akode:BuildRequires:	trinity-akode-devel}

# ruby
BuildRequires:	ruby
BuildRequires:	ruby-devel

# PYTHON support
%global python python3
%global __python %__python3
%global python_sitearch %{python3_sitearch}
%{!?python_sitearch:%global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
BuildRequires:	%{python}
BuildRequires:	%{python}-devel

BuildRequires:  pkgconfig(dri)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)

# To open the selected browser, works with Patch2
Requires:		xdg-utils
Requires(post): xdg-utils
Requires(postun): xdg-utils


%description
Amarok is a multimedia player with:
 - fresh playlist concept, very fast to use, with drag and drop
 - plays all formats supported by the various engines
 - audio effects, like reverb and compressor
 - compatible with the .m3u and .pls formats for playlists
 - nice GUI, integrates into the TDE look, but with a unique touch

%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%doc COPYING AUTHORS ChangeLog README.md
%{tde_bindir}/amarok
%{tde_bindir}/amarokapp
%{tde_bindir}/amarokcollectionscanner
%{tde_bindir}/amarok_proxy.rb
%{tde_datadir}/apps/amarok/
%{tde_datadir}/icons/crystalsvg/*/actions/covermanager.png
%{tde_datadir}/icons/crystalsvg/*/actions/dynamic.png
%{tde_datadir}/icons/crystalsvg/*/actions/equalizer.png
%{tde_datadir}/icons/crystalsvg/*/actions/mini_dock.png
%{tde_datadir}/icons/crystalsvg/*/actions/player_playlist_2.png
%{tde_datadir}/icons/crystalsvg/*/actions/podcast.png
%{tde_datadir}/icons/crystalsvg/*/actions/podcast_new.png
%{tde_datadir}/icons/crystalsvg/*/actions/random.png
%{tde_datadir}/icons/crystalsvg/*/actions/repeat_playlist.png
%{tde_datadir}/icons/crystalsvg/*/actions/repeat_track.png
%{tde_datadir}/icons/crystalsvg/*/actions/visualizations.png
%{tde_datadir}/icons/crystalsvg/*/actions/wiki.png
%{tde_datadir}/icons/crystalsvg/*/actions/amarok_podcast.png
%{tde_datadir}/icons/crystalsvg/*/actions/amarok_podcast_new.png
%{tde_datadir}/icons/crystalsvg/*/actions/amazon_locale.png
%{tde_datadir}/icons/hicolor/*/*/*
%{tde_tdeappdir}/*.desktop
%{tde_datadir}/servicetypes/*.desktop
%{tde_datadir}/apps/profiles/amarok.profile.xml
%config(noreplace) %{tde_confdir}/amarokrc
%{tde_datadir}/config.kcfg/*.kcfg
%{tde_datadir}/services/amarokitpc.protocol
%{tde_datadir}/services/amaroklastfm.protocol
%{tde_datadir}/services/amarokpcast.protocol
%{tde_mandir}/man1/amarok.1*
%{tde_mandir}/man1/amarokapp.1*
%{tde_mandir}/man1/amarokcollectionscanner.1*
# -libs ?  -- Rex
%{tde_libdir}/libamarok.so.0
%{tde_libdir}/libamarok.so.0.0.0
# DAAP
%if %{with daap}
%{tde_bindir}/amarok_daapserver.rb
%{tde_tdelibdir}/libamarok_daap-mediadevice.*
%{tde_datadir}/services/amarok_daap-mediadevice.desktop
%endif
# Mass-storage
%{tde_datadir}/services/amarok_massstorage-device.desktop
%{tde_tdelibdir}/libamarok_massstorage-device.*
# NFS
%{tde_datadir}/services/amarok_nfs-device.desktop
%{tde_tdelibdir}/libamarok_nfs-device.*
# SMB
%{tde_datadir}/services/amarok_smb-device.desktop
%{tde_tdelibdir}/libamarok_smb-device.*
# IPod
%if %{with gpod}
%{tde_datadir}/services/amarok_ipod-mediadevice.desktop
%{tde_tdelibdir}/libamarok_ipod-mediadevice.*
%endif
# VFAT
%{tde_datadir}/services/amarok_generic-mediadevice.desktop
%{tde_tdelibdir}/libamarok_generic-mediadevice.*
# iRiver
%if %{with ifp}
%{tde_datadir}/services/amarok_ifp-mediadevice.desktop
%{tde_tdelibdir}/libamarok_ifp-mediadevice.*
%endif
# Creative Zen
%if %{with njb}
%{tde_datadir}/services/amarok_njb-mediadevice.desktop
%{tde_tdelibdir}/libamarok_njb-mediadevice.*
%endif
# MTP players
%if %{with mtp}
%{tde_datadir}/services/amarok_mtp-mediadevice.desktop
%{tde_tdelibdir}/libamarok_mtp-mediadevice.*
%endif
# Void engine (noop)
%{tde_datadir}/services/amarok_void-engine_plugin.desktop
%{tde_tdelibdir}/libamarok_void-engine_plugin.*
# Xine engine
%if %{with xine}
%{tde_datadir}/services/amarok_xine-engine.desktop
%{tde_tdelibdir}/libamarok_xine-engine.*
%endif
## Gstreamer engine
#{tde_datadir}/services/amarok_gst10engine_plugin.desktop
#{tde_tdelibdir}/libamarok_gst10engine_plugin.*
# YAUAP
%if %{with yauap}
%{tde_datadir}/services/amarok_yauap-engine_plugin.desktop
%{tde_tdelibdir}/libamarok_yauap-engine_plugin.*
%endif
# AKODE
%if %{with akode}
%{tde_datadir}/services/amarok_aKode-engine.desktop
%{tde_tdelibdir}/libamarok_aKode-engine.*
%endif

##########

%package konqueror
Summary:		Amarok konqueror (service menus, sidebar) support
Group:			Applications/Multimedia

Requires:		%{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:		trinity-konqueror

%description konqueror
%{summary}.

%files konqueror
%defattr(-,root,root,-)
%{tde_datadir}/apps/konqueror/servicemenus/*.desktop
%{tde_tdelibdir}/konqsidebar_universalamarok.*
%{tde_datadir}/apps/konqsidebartng/*/amarok_konquisidebar.desktop


##########

%if %{with libvisual}

%package visualisation
Summary:		Visualisation plugins for Amarok
Group:			Applications/Multimedia
Requires:		%{name} = %{?epoch:%{epoch}:}%{version}-%{release}
# No plugins by default, we need libvisual-plugins
#Requires:   libvisual-plugins

%description visualisation
Amarok can use visualisation plugins from different origins.
Right now, only xmms is supported, which means that you can
use any of xmms' visualisation plugins with Amarok.

%files visualisation
%defattr(-,root,root,-)
%{tde_bindir}/amarok_libvisual
%{tde_mandir}/man1/amarok_libvisual.1*

%endif


%conf -p
# Fix some Ruby stuff
if ! ruby -rrbconfig -e "puts Config.expand( Config::MAKEFILE_CONFIG['MAJOR'] )" &>/dev/null; then
  %__sed -i "amarok/src/mediadevice/daap/ConfigureChecks.cmake" \
         -e "s|Config::|RbConfig::|g" \
         -e "s|Config\.|RbConfig\.|g"
fi

unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig"


%install -a
# unpackaged files
%__rm -f %{buildroot}/%{tde_libdir}/lib*.la
# Removes '.so' to avoid automatic -devel dependency
%__rm -f %{buildroot}/%{tde_libdir}/libamarok.so

# Locales
%find_lang %{tde_pkg}

# HTML
for lang_dir in %{buildroot}/%{tde_tdedocdir}/HTML/* ; do
  if [ -d $lang_dir ]; then
    lang=$(basename $lang_dir)
    [ "$lang" == "en" ] && d=en/amarok || d=$lang
    echo "%lang($lang) %doc %{tde_tdedocdir}/HTML/$d" >> amarok.lang
  fi
done

