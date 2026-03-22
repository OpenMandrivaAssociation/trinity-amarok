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
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif

%define tde_pkg amarok

%define tde_prefix /opt/trinity


%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%define _debugsource_template %{nil}

%define tarball_name %{tde_pkg}-trinity


Name:		trinity-%{tde_pkg}
Version:	1.4.10
Release:	%{?tde_version:%{tde_version}_}5
Summary:	Media player for TDE
Group:		Applications/Multimedia
URL:		http://www.trinitydesktop.org/
#Url:		http://amarok.kde.org

License:	GPLv2+


Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/applications/multimedia/%{tarball_name}-%{tde_version}.tar.xz

BuildSystem:    cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DCONFIG_INSTALL_DIR=%{_sysconfdir}/trinity
BuildOption:    -DINCLUDE_INSTALL_DIR=%{tde_prefix}/include/tde
BuildOption:    -DWITH_KONQSIDEBAR=ON
BuildOption:    -DWITH_SYSTEM_SQLITE=ON
BuildOption:    -DBUILD_ALL=ON
BuildOption:    -DWITH_OPENGL=ON
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}
BuildOption:    -DWITH_LIBVISUAL=%{!?with_libvisual:OFF}%{?with_libvisual:ON}
BuildOption:    -DWITH_XINE=%{!?with_xine:OFF}%{?with_xine:ON} 
BuildOption:    -DWITH_YAUAP=%{!?with_yauap:OFF}%{?with_yauap:ON}
BuildOption:    -DWITH_AKODE=%{!?with_akode:OFF}%{?with_akode:ON}
BuildOption:    -DWITH_IPOD=%{!?with_gpod:OFF}%{?with_gpod:ON}
BuildOption:    -DWITH_IFP=%{!?with_ifp:OFF}%{?with_ifp:ON}
BuildOption:    -DWITH_NJB=%{!?with_njb:OFF}%{?with_njb:ON}
BuildOption:    -DWITH_MTP=%{!?with_mtp:OFF}%{?with_mtp:ON}
BuildOption:    -DWITH_DAAP=%{!?with_daap:OFF}%{?with_daap:ON}
BuildOption:    -DWITH_INOTIFY=%{!?with_inotify:OFF}%{?with_inotify:ON}

BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	trinity-konqueror-devel >= %{tde_version}
BuildRequires:  tqt3-dev-tools
BuildRequires:	trinity-filesystem >= %{tde_version}

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
BuildRequires:	pkgconfig(dbus-tqt)

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
%{?with_akode:BuildRequires:	pkgconfig(akode)}

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
%{tde_prefix}/bin/amarok
%{tde_prefix}/bin/amarokapp
%{tde_prefix}/bin/amarokcollectionscanner
%{tde_prefix}/bin/amarok_proxy.rb
%{tde_prefix}/share/apps/amarok/
%{tde_prefix}/share/icons/crystalsvg/*/actions/covermanager.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/dynamic.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/equalizer.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/mini_dock.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/player_playlist_2.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/podcast.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/podcast_new.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/random.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/repeat_playlist.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/repeat_track.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/visualizations.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/wiki.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/amarok_podcast.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/amarok_podcast_new.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/amazon_locale.png
%{tde_prefix}/share/icons/hicolor/*/*/*
%{tde_prefix}/share/applications/tde/*.desktop
%{tde_prefix}/share/servicetypes/*.desktop
%{tde_prefix}/share/apps/profiles/amarok.profile.xml
%config(noreplace) %{_sysconfdir}/trinity/amarokrc
%{tde_prefix}/share/config.kcfg/*.kcfg
%{tde_prefix}/share/services/amarokitpc.protocol
%{tde_prefix}/share/services/amaroklastfm.protocol
%{tde_prefix}/share/services/amarokpcast.protocol
%{tde_prefix}/share/man/man1/amarok.1*
%{tde_prefix}/share/man/man1/amarokapp.1*
%{tde_prefix}/share/man/man1/amarokcollectionscanner.1*
# -libs ?  -- Rex
%{tde_prefix}/%{_lib}/libamarok.so.0
%{tde_prefix}/%{_lib}/libamarok.so.0.0.0
# DAAP
%if %{with daap}
%{tde_prefix}/bin/amarok_daapserver.rb
%{tde_prefix}/%{_lib}/trinity/libamarok_daap-mediadevice.*
%{tde_prefix}/share/services/amarok_daap-mediadevice.desktop
%endif
# Mass-storage
%{tde_prefix}/share/services/amarok_massstorage-device.desktop
%{tde_prefix}/%{_lib}/trinity/libamarok_massstorage-device.*
# NFS
%{tde_prefix}/share/services/amarok_nfs-device.desktop
%{tde_prefix}/%{_lib}/trinity/libamarok_nfs-device.*
# SMB
%{tde_prefix}/share/services/amarok_smb-device.desktop
%{tde_prefix}/%{_lib}/trinity/libamarok_smb-device.*
# IPod
%if %{with gpod}
%{tde_prefix}/share/services/amarok_ipod-mediadevice.desktop
%{tde_prefix}/%{_lib}/trinity/libamarok_ipod-mediadevice.*
%endif
# VFAT
%{tde_prefix}/share/services/amarok_generic-mediadevice.desktop
%{tde_prefix}/%{_lib}/trinity/libamarok_generic-mediadevice.*
# iRiver
%if %{with ifp}
%{tde_prefix}/share/services/amarok_ifp-mediadevice.desktop
%{tde_prefix}/%{_lib}/trinity/libamarok_ifp-mediadevice.*
%endif
# Creative Zen
%if %{with njb}
%{tde_prefix}/share/services/amarok_njb-mediadevice.desktop
%{tde_prefix}/%{_lib}/trinity/libamarok_njb-mediadevice.*
%endif
# MTP players
%if %{with mtp}
%{tde_prefix}/share/services/amarok_mtp-mediadevice.desktop
%{tde_prefix}/%{_lib}/trinity/libamarok_mtp-mediadevice.*
%endif
# Void engine (noop)
%{tde_prefix}/share/services/amarok_void-engine_plugin.desktop
%{tde_prefix}/%{_lib}/trinity/libamarok_void-engine_plugin.*
# Xine engine
%if %{with xine}
%{tde_prefix}/share/services/amarok_xine-engine.desktop
%{tde_prefix}/%{_lib}/trinity/libamarok_xine-engine.*
%endif
## Gstreamer engine
#{tde_datadir}/services/amarok_gst10engine_plugin.desktop
#{tde_tdelibdir}/libamarok_gst10engine_plugin.*
# YAUAP
%if %{with yauap}
%{tde_prefix}/share/services/amarok_yauap-engine_plugin.desktop
%{tde_prefix}/%{_lib}/trinity/libamarok_yauap-engine_plugin.*
%endif
# AKODE
%if %{with akode}
%{tde_prefix}/share/services/amarok_aKode-engine.desktop
%{tde_prefix}/%{_lib}/trinity/libamarok_aKode-engine.*
%endif

##########

%package konqueror
Summary:		Amarok konqueror (service menus, sidebar) support
Group:			Applications/Multimedia

Requires:		%{name} = %{EVRD}
Requires:		trinity-konqueror

%description konqueror
%{summary}.

%files konqueror
%defattr(-,root,root,-)
%{tde_prefix}/share/apps/konqueror/servicemenus/*.desktop
%{tde_prefix}/%{_lib}/trinity/konqsidebar_universalamarok.*
%{tde_prefix}/share/apps/konqsidebartng/*/amarok_konquisidebar.desktop


##########

%if %{with libvisual}

%package visualisation
Summary:		Visualisation plugins for Amarok
Group:			Applications/Multimedia
Requires:		%{name} = %{EVRD}
# No plugins by default, we need libvisual-plugins
#Requires:   libvisual-plugins

%description visualisation
Amarok can use visualisation plugins from different origins.
Right now, only xmms is supported, which means that you can
use any of xmms' visualisation plugins with Amarok.

%files visualisation
%defattr(-,root,root,-)
%{tde_prefix}/bin/amarok_libvisual
%{tde_prefix}/share/man/man1/amarok_libvisual.1*

%endif


%conf -p
# Fix some Ruby stuff
if ! ruby -rrbconfig -e "puts Config.expand( Config::MAKEFILE_CONFIG['MAJOR'] )" &>/dev/null; then
  %__sed -i "amarok/src/mediadevice/daap/ConfigureChecks.cmake" \
         -e "s|Config::|RbConfig::|g" \
         -e "s|Config\.|RbConfig\.|g"
fi

unset QTDIR QTINC QTLIB
export PATH="%{tde_prefix}/bin:${PATH}"
export PKG_CONFIG_PATH="%{tde_prefix}/%{_lib}/pkgconfig"


%install -a
# unpackaged files
%__rm -f %{buildroot}/%{tde_prefix}/%{_lib}/lib*.la
# Removes '.so' to avoid automatic -devel dependency
%__rm -f %{buildroot}/%{tde_prefix}/%{_lib}/libamarok.so

# Locales
%find_lang %{tde_pkg}

# HTML
for lang_dir in %{buildroot}/%{tde_prefix}/share/doc/tde/HTML/* ; do
  if [ -d $lang_dir ]; then
    lang=$(basename $lang_dir)
    [ "$lang" == "en" ] && d=en/amarok || d=$lang
    echo "%lang($lang) %doc %{tde_prefix}/share/doc/tde/HTML/$d" >> amarok.lang
  fi
done

