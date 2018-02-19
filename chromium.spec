# NEVER EVER EVER turn this on in official builds
%global freeworld 1

# Leave this alone, please.
%global target out/Release
%global headlesstarget out/Headless

# Debuginfo packages aren't very useful here. If you need to debug
# you should do a proper debug build (not implemented in this spec yet)
%global debug_package %{nil}

# %%{nil} for Stable; -beta for Beta; -dev for Devel
# dash in -beta and -dev is intentional !
%global chromium_channel %{nil}
%global chromium_menu_name Chromium
%global chromium_browser_channel chromium-browser%{chromium_channel}
%global chromium_path %{_libdir}/chromium-browser%{chromium_channel}
%global crd_path %{_libdir}/chrome-remote-desktop

# We don't want any libs in these directories to generate Provides
# Requires is trickier.

%global __provides_exclude_from %{chromium_path}/.*\\.so|%{chromium_path}/lib/.*\\.so
%global privlibs libaccessibility|libaura_extra|libaura|libbase_i18n|libbase|libblink_common|libblink_core|libblink_modules|libblink_platform|libblink_web|libbluetooth|libboringssl|libbrowser_ui_views|libcaptive_portal|libcapture|libcc_blink|libcc_ipc|libcc_proto|libcc|libcc_surfaces|libchromium_sqlite3|libcloud_policy_proto_generated_compile|libcloud_policy_proto|libcommon|libcompositor|libcontent|libcrcrypto|libdbus|libdevice_battery|libdevice_core|libdevice_event_log|libdevice_gamepad|libdevice_geolocation|libdevices|libdevice_vibration|libdisplay_compositor|libdisplay|libdisplay_types|libdisplay_util|libdomain_reliability|libEGL|libevents_base|libevents_devices_x11|libevents_ipc|libevents_ozone_layout|libevents|libevents_x|libffmpeg|libfont_service_library|libgcm|libgeometry|libgesture_detection|libgfx_ipc_color|libgfx_ipc_geometry|libgfx_ipc_skia|libgfx_ipc|libgfx|libgfx_x11|libgin|libgles2_c_lib|libgles2_implementation|libgles2_utils|libGLESv2|libgl_init|libgl_wrapper|libgpu|libgtk2ui|libicui18n|libicuuc|libipc|libkeyboard|libkeyboard_with_content|libkeycodes_x11|libkeyed_service_content|libkeyed_service_core|libmedia_blink|libmedia_gpu|libmedia|libmemory_coordinator_browser|libmemory_coordinator_child|libmemory_coordinator_common|libmessage_center|libmidi|libmojo_blink_lib|libmojo_common_lib|libmojo_ime_lib|libmojo_public_system|libmojo_system_impl|libnative_theme|libnet|libnet_with_v8|libonc|libplatform|libpolicy_component|libpolicy_proto|libpower_save_blocker|libppapi_host|libppapi_proxy|libppapi_shared|libprefs|libprinting|libprotobuf_lite|libproxy_config|librange|libsandbox_services|libseccomp_bpf|libsessions|libshared_memory_support|libshell_dialogs|libskia|libsnapshot|libsql|libstartup_tracing|libstorage_browser|libstorage_common|libstub_window|libsuid_sandbox_client|libsurface|libtracing|libtranslator|libui_base_ime|libui_base|libui_base_x|libui_data_pack|libui_library|libui_touch_selection|libui_views_mus_lib|liburl_ipc|liburl_matcher|liburl|libuser_prefs|libv8|libviews|libwebdata_common|libweb_dialogs|libwebview|libwidevinecdm|libwm|libwtf|libx11_events_platform|libx11_window|libbindings|libgeolocation|libmojo_public_system_cpp|libtime_zone_monitor|libdevice_base|libcc_animation|libcpp|libdevice_base|libdiscardable_memory_client|libdiscardable_memory_common|libdiscardable_memory_service|libgeneric_sensor|libgl_in_process_context|libjs|libpower_monitor|libv8_libbase|libsensors|libdevice_vr|libcc_paint|libgtk3ui|libcapture_base|libcapture_lib|libfingerprint|libanimation|libcc_base|libcc_debug|libcodec|libcolor_space|libembedder|libgeometry_skia|libgin_features|libmedia_mojo_services|libplatform_wtf|libprotobuf_globals|libcdm_manager|libframe_sinks|libresource_coordinator_cpp|libblink_android_mojo_bindings_shared|libblink_mojo_bindings_shared|libblink_mojo_bindings_shared|libblink_offscreen_canvas_mojo_bindings_shared|libcontent_common_mojo_bindings_shared|libdevice_vr_mojo_bindings|libdevice_vr_mojo_bindings_blink|libdevice_vr_mojo_bindings_shared|libgeneric_sensor_public_interfaces_shared|libheadless|libipc_mojom|libipc_mojom_shared|libpublic|libresource_coordinator_public_interfaces_internal_shared|libservice_manager_cpp|libservice_manager_cpp_types|libservice_manager_mojom|libservice_manager_mojom_constants|libservice_manager_mojom_constants_shared|libservice_manager_mojom_shared|libgfx_switches|libmetrics_cpp|libui_devtools|libviz_common|libwm_public|libblink_controller|libcontent_public_common_mojo_bindings_shared|libgfx_switches|libhost|libinterfaces_shared|libmetrics_cpp|libservice|libviz_common|libwm_public|libviz_resource_format|libembedder_switches|libfreetype_harfbuzz|libmessage_support|libsandbox|libclient|libleveldatabase|libblink_core_mojo_bindings_shared|libgpu_util|libmedia_devices_mojo_bindings_shared|libmojo_platform_bindings_shared|libmojo_bindings_shared
%global __requires_exclude ^(%{privlibs})\\.so

# If we build with shared on, then chrome-remote-desktop depends on chromium libs.
# If we build with shared off, then users cannot swap out libffmpeg (and i686 gets a lot harder to build)
%global shared 1
# We should not need to turn this on. The app in the webstore _should_ work.
%global build_remoting_app 0

# Build Chrome Remote Desktop
%global build_remote_desktop 1

# AddressSanitizer mode
# https://www.chromium.org/developers/testing/addresssanitizer
%global asan 0

# nacl/pnacl are soon to be dead. We're just killing them off early.
%global killnacl 1

%if 0%{?killnacl}
 %global nacl 0
 %global nonacl 1
%else
# TODO: Try arm (nacl disabled)
%if 0%{?fedora}
 %ifarch i686
 %global nacl 0
 %global nonacl 1
 %else
 %global nacl 0
 %global nonacl 0
 %endif
%endif
%endif

%if 0
# Chromium's fork of ICU is now something we can't unbundle.
# This is left here to ease the change if that ever switches.
BuildRequires:  libicu-devel >= 5.4
%global bundleicu 0
%else
%global bundleicu 1
%endif

%global bundlere2 1

# The libxml_utils code depends on the specific bundled libxml checkout
# which is not compatible with the current code in the Fedora package as of
# 2017-06-08.
%global bundlelibxml 1

# Chromium breaks on wayland, hidpi, and colors with gtk3 enabled.
%global gtk3 1

# Enable vaapi
%global vaapi 1

%if 0%{?rhel} == 7
%global bundleopus 1
%global bundlejinja2 1
%global bundlelibusbx 1
%global bundleharfbuzz 1
%global bundlelibwebp 1
%global bundlelibpng 1
%global bundlelibjpeg 1
%else
%global bundleharfbuzz 0
%global bundlejinja2 1
%global bundleopus 1
%global bundlelibusbx 1
%global bundlelibwebp 0
%global bundlelibpng 0
%global bundlelibjpeg 0
%endif

# Needs at least harfbuzz 1.5.0 now.
# 2017-06-12
%if 0%{?fedora} < 28
%global bundleharfbuzz 1
%else
%global bundleharfbuzz 0
%endif

### Google API keys (see http://www.chromium.org/developers/how-tos/api-keys)
### Note: These are for Fedora use ONLY.
### For your own distribution, please get your own set of keys.
### http://lists.debian.org/debian-legal/2013/11/msg00006.html
%global api_key AIzaSyDUIXvzVrt5OkVsgXhQ6NFfvWlA44by-aw
%global default_client_id 449907151817.apps.googleusercontent.com
%global default_client_secret miEreAep8nuvTdvLums6qyLK
%global chromoting_client_id 449907151817-8vnlfih032ni8c4jjps9int9t86k546t.apps.googleusercontent.com

Name:		chromium%{chromium_channel}
Version:	64.0.3282.167
Release:	1%{?dist}.R
Epoch:		1
Summary:	A WebKit (Blink) powered web browser with video acceleration patches(experimental)
Url:		http://www.chromium.org/Home
License:	BSD and LGPLv2+ and ASL 2.0 and IJG and MIT and GPLv2+ and ISC and OpenSSL and (MPLv1.1 or GPLv2 or LGPLv2)

### Chromium Fedora Patches ###
Patch1:		chromium-45.0.2454.101-linux-path-max.patch
Patch2:		chromium-55.0.2883.75-addrfix.patch
# Google patched their bundled copy of icu 54 to include API functionality that wasn't added until 55.
# :P
Patch4:		chromium-46.0.2490.71-notest.patch
# Ignore broken nacl open fd counter
Patch7:		chromium-47.0.2526.80-nacl-ignore-broken-fd-counter.patch
# Use libusb_interrupt_event_handler from current libusbx (1.0.21-0.1.git448584a)
Patch9:		chromium-48.0.2564.116-libusb_interrupt_event_handler.patch
# Use PIE in the Linux sandbox (from openSUSE via Russian Fedora)
Patch15:	chromium-55.0.2883.75-sandbox-pie.patch
# Enable ARM CPU detection for webrtc (from archlinux via Russian Fedora)
Patch16:	chromium-52.0.2743.82-arm-webrtc.patch
# Do not force -m32 in icu compile on ARM (from archlinux via Russian Fedora)
Patch17:	chromium-56.0.2924.59-arm-icu-fix.patch
# Use /etc/chromium for master_prefs
Patch18:	chromium-52.0.2743.82-master-prefs-path.patch
# Fix last commit position issue
# https://groups.google.com/a/chromium.org/forum/#!topic/gn-dev/7nlJv486bD4
Patch21:	chromium-60.0.3112.7-last-commit-position.patch
# Fix issue where timespec is not defined when sys/stat.h is included.
Patch22:	chromium-53.0.2785.92-boringssl-time-fix.patch
# Fix gn build on Linux
# I wouldn't have to do this if there was a standard way to append extra compiler flags
Patch24:	chromium-59.0.3071.29-nullfix.patch
# Add explicit includedir for jpeglib.h
Patch25:	chromium-54.0.2840.59-jpeg-include-dir.patch
# On i686, pass --no-keep-memory --reduce-memory-overheads to ld.
Patch26:	chromium-59.0.3071.29-i686-ld-memory-tricks.patch
# obj/content/renderer/renderer/child_frame_compositing_helper.o: In function `content::ChildFrameCompositingHelper::OnSetSurface(cc::SurfaceId const&, gfx::Size const&, float, cc::SurfaceSequence const&)':
# /builddir/build/BUILD/chromium-54.0.2840.90/out/Release/../../content/renderer/child_frame_compositing_helper.cc:214: undefined reference to `cc_blink::WebLayerImpl::setOpaque(bool)'
Patch27:	chromium-63.0.3239.70-setopaque.patch
# Use -fpermissive to build WebKit
Patch31:	chromium-56.0.2924.87-fpermissive.patch
# Fix issue with compilation on gcc7
# Thanks to Ben Noordhuis
Patch33:	chromium-60.0.3095.5-gcc7.patch
# Revert https://chromium.googlesource.com/chromium/src/+/b794998819088f76b4cf44c8db6940240c563cf4%5E%21/#F0
# https://bugs.chromium.org/p/chromium/issues/detail?id=712737
# https://bugzilla.redhat.com/show_bug.cgi?id=1446851
Patch36:       chromium-58.0.3029.96-revert-b794998819088f76b4cf44c8db6940240c563cf4.patch
# Change struct ucontext to ucontext_t in breakpad
# https://patchwork.openembedded.org/patch/141358/
Patch40:	chromium-59.0.3071.115-ucontext-fix.patch
# Do not prefix libpng functions
Patch42:       chromium-60.0.3112.78-no-libpng-prefix.patch
# Do not mangle libjpeg
Patch43:       chromium-60.0.3112.78-jpeg-nomangle.patch
# Do not mangle zlib
Patch45:        chromium-60.0.3112.78-no-zlib-mangle.patch
# Apply this change to work around EPEL7 compiler issues
Patch46:        chromium-62.0.3202.45-kmaxskip-constexpr.patch
Patch47:        chromium-60.0.3112.90-vulkan-force-c99.patch
# more gcc fixes
# https://chromium.googlesource.com/chromium/src.git/+/cbe6845263215e0f3981c2a4c7937dadb14bef0d%5E%21/#F0
Patch52:	chromium-61.0.3163.79-MOAR-GCC-FIXES.patch
# from gentoo
Patch53:	chromium-61.0.3163.79-gcc-no-opt-safe-math.patch
# More gcc fixes for epel
Patch54:        chromium-gcc5-r3.patch
Patch58:	chromium-61.0.3163.79-dde535-gcc-fix.patch
Patch59:	chromium-62.0.3202.45-gcc-nc.patch
# Epel compiler really does not like assigning nullptr to a StructPtr
Patch60:	chromium-62.0.3202.62-epel7-no-nullptr-assignment-on-StructPtr.patch
# Another gcc 4.8 goods..
Patch61:	chromium-62.0.3202.45-rvalue-fix.patch
# Webrtc gentto patch 
# ftp://mirror.yandex.ru/gentoo-portage/www-client/chromium/files/chromium-webrtc-r0.patch
Patch62:	chromium-webrtc-r0.patch
Patch63:	chromium-63.0.3289.84-nolibc++.patch
Patch64:	chromium-63.0.3289.84-fix-ft-hb-unbundle.patch
Fixed an issue which prevents Amd GPU users from getting Hardware acceleration and fail to find swiftshader library.
Patch65:	chromium-64.0.3282.167-f172c7c.patch

### Russian Fedora Patches ###
# Clang Gentoo patch: ftp://mirror.yandex.ru/gentoo-portage/www-client/chromium/files/chromium-clang-r2.patch
Patch502:	chromium-clang-r2.patch
# Memcpy Gentoo patch: ftp://mirror.yandex.ru/gentoo-portage/www-client/chromium/files/chromium-memcpy-r0.patch
# memcpy used without including string.h
# Compiling Chromium with Clang 4.0.1 and using libstdc++ will fail on using
Patch503:	chromium-memcpy-r0.patch
# Cups Gentoo patch: ftp://mirror.yandex.ru/gentoo-portage/www-client/chromium/files/chromium-cups-r0.patch
# Fix use_cups=false build
Patch504:	chromium-cups-r0.patch
# Angle Gentoo patch: ftp://mirror.yandex.ru/gentoo-portage/www-client/chromium/files/chromium-angle-r0.patch
# Fixes compilation on some versions of GCC and probably Clang.
# Follow-up to http://crrev.com/c/786317
Patch505:	chromium-angle-r0.patch

# Vaapi Patches
# Ubuntu patch for chromium 64
# https://raw.githubusercontent.com/saiarcot895/chromium-ubuntu-build/branch-3282/debian/patches/enable_vaapi_on_linux_2.diff
Patch600:	enable_vaapi_on_linux_2.diff
# Allow fallback max resolution for VA to be read from file
# https://github.com/saiarcot895/chromium-ubuntu-build/pull/16
# https://raw.githubusercontent.com/saiarcot895/chromium-ubuntu-build/branch-3282/debian/patches/specify-max-resolution.patch
Patch601:	specify-max-resolution.patch

# Use chromium-latest.py to generate clean tarball from released build tarballs, found here:
# http://build.chromium.org/buildbot/official/
# For Chromium Fedora use chromium-latest.py --stable --ffmpegclean --ffmpegarm
# If you want to include the ffmpeg arm sources append the --ffmpegarm switch
# https://commondatastorage.googleapis.com/chromium-browser-official/chromium-%%{version}.tar.xz
%if %{freeworld}
Source0:	https://commondatastorage.googleapis.com/chromium-browser-official/chromium-%{version}.tar.xz
%else
Source0:	chromium-%{version}-clean.tar.xz
%endif
Source3:	chromium-browser.sh
Source4:	%{chromium_browser_channel}.desktop
# Also, only used if you want to reproduce the clean tarball.
Source5:	clean_ffmpeg.sh
Source6:	chromium-latest.py
Source7:	get_free_ffmpeg_source_files.py
# Get the names of all tests (gtests) for Linux
# Usage: get_linux_tests_name.py chromium-%%{version} --spec
Source8:	get_linux_tests_names.py
# GNOME stuff
Source9:	chromium-browser.xml
Source11:	chrome-remote-desktop@.service
Source13:	master_preferences

# We can assume gcc and binutils.
BuildRequires:	gcc-c++

%if 0%{?asan}
BuildRequires:	clang
BuildRequires:	llvm
%endif

BuildRequires:	alsa-lib-devel
BuildRequires:	atk-devel
BuildRequires:	bison
BuildRequires:	cups-devel
BuildRequires:	dbus-devel
BuildRequires:	desktop-file-utils
BuildRequires:	expat-devel
BuildRequires:	flex
BuildRequires:	fontconfig-devel
BuildRequires:	GConf2-devel
BuildRequires:	glib2-devel
BuildRequires:	gnome-keyring-devel
BuildRequires:	gtk2-devel
BuildRequires:	glibc-devel
BuildRequires:	gperf
BuildRequires:	libatomic
BuildRequires:	libcap-devel
BuildRequires:	libdrm-devel
BuildRequires:	libgcrypt-devel
BuildRequires:	libudev-devel
BuildRequires:	libusb-devel
BuildRequires:	libXdamage-devel
BuildRequires:	libXScrnSaver-devel
BuildRequires:	libXtst-devel
BuildRequires:	ninja-build >= 1.7.2
BuildRequires:	minizip-devel
BuildRequires:	mesa-libGL-devel
BuildRequires:	nodejs
BuildRequires:	nss-devel >= 3.26
BuildRequires:	pciutils-devel
BuildRequires:	pulseaudio-libs-devel
%if 0%{vaapi}
BuildRequires:	libva-devel
%endif

# for /usr/bin/appstream-util
BuildRequires: libappstream-glib

# Fedora turns on NaCl
# NaCl needs these
BuildRequires:	libstdc++-devel, openssl-devel
%if 0%{?nacl}
BuildRequires:	nacl-gcc, nacl-binutils, nacl-newlib
BuildRequires:	nacl-arm-gcc, nacl-arm-binutils, nacl-arm-newlib
# pNaCl needs this monster
# It's possible that someday this dep will stabilize, but
# right now, it needs to be updated everytime chromium bumps
# a major version.
BuildRequires:	chromium-native_client >= 52.0.2743.82
%ifarch x86_64
# Really, this is what we want:
# BuildRequires:  glibc-devel(x86-32) libgcc(x86-32)
# But, koji only offers glibc32. Maybe that's enough.
# This BR will pull in either glibc.i686 or glibc32.
BuildRequires:	/lib/libc.so.6 /usr/lib/libc.so
%endif
%endif
# Fedora tries to use system libs whenever it can.
BuildRequires:	bzip2-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	elfutils-libelf-devel
BuildRequires:	flac-devel
BuildRequires:	hwdata
BuildRequires:	kernel-headers
BuildRequires:	libevent-devel
BuildRequires:	libffi-devel
BuildRequires:	vulkan-devel
%if 0%{?bundleicu}
# If this is true, we're using the bundled icu.
# We'd like to use the system icu every time, but we cannot always do that.
%else
# Not newer than 54 (at least not right now)
BuildRequires:	libicu-devel = 54.1
%endif
BuildRequires:	libjpeg-devel
%if 0%{?bundlelibpng}
# If this is true, we're using the bundled libpng
# which we need to do because the RHEL 7 libpng doesn't work right anymore
%else
BuildRequires:	libpng-devel
%endif
%if 0
# see https://code.google.com/p/chromium/issues/detail?id=501318
BuildRequires:	libsrtp-devel >= 1.4.4
%endif
BuildRequires:	libudev-devel
%if %{bundlelibusbx}
# Do nothing
%else
Requires:	libusbx >= 1.0.21-0.1.git448584a
BuildRequires:	libusbx-devel >= 1.0.21-0.1.git448584a
%endif
# We don't use libvpx anymore because Chromium loves to
# use bleeding edge revisions here that break other things
# ... so we just use the bundled libvpx.
%if %{bundlelibwebp}
# Do nothing
%else
BuildRequires:	libwebp-devel
%endif
BuildRequires:	libxslt-devel
# Same here, it seems.
# BuildRequires:	libyuv-devel
%if %{bundleopus}
# Do nothing
%else
BuildRequires:	opus-devel
%endif
BuildRequires:	perl(Switch)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pulseaudio-libs-devel
BuildRequires:	python2
BuildRequires:	python-beautifulsoup4
BuildRequires:	python-BeautifulSoup
BuildRequires:	python-html5lib
%if 0%{?bundlejinja2}
# Using bundled bits, do nothing.
%else
BuildRequires:	python-jinja2
%endif
BuildRequires:	python-markupsafe
BuildRequires:	python-ply
BuildRequires:	python-simplejson
%if 0%{?bundlere2}
# Using bundled bits, do nothing.
%else
Requires:	re2 >= 20160401
BuildRequires:	re2-devel >= 20160401
%endif
BuildRequires:	speech-dispatcher-devel
BuildRequires:	yasm
BuildRequires:	zlib-devel
BuildRequires:	pkgconfig(gnome-keyring-1)
# remote desktop needs this
BuildRequires:	pam-devel
BuildRequires:	systemd

%if 0%{?rhel} == 7
BuildRequires: devtoolset-7-toolchain, devtoolset-7-libatomic-devel
%endif

# There is a hardcoded check for nss 3.26 in the chromium code (crypto/nss_util.cc)
Requires:	nss%{_isa} >= 3.26
Requires:	nss-mdns%{_isa}

# GTK modules it expects to find for some reason.
Requires:	libcanberra-gtk3%{_isa}

%if 0%{?fedora}
# This enables support for u2f tokens
Requires:	u2f-hidraw-policy
%endif

%if 0%{vaapi}
Requires:	libva
%endif

# Once upon a time, we tried to split these out... but that's not worth the effort anymore.
Provides:	chromium-ffmpegsumo = %{epoch}:%{version}-%{release}
Obsoletes:	chromium-ffmpegsumo <= 35.0.1916.114
# This is a lie. v8 has its own version... but I'm being lazy and not using it here.
# Barring Google getting much faster on the v8 side (or much slower on the Chromium side)
# the true v8 version will be much smaller than the Chromium version that it came from.
Provides:	chromium-v8 = %{epoch}:%{version}-%{release}
Obsoletes:	chromium-v8 <= 3.25.28.18
# This is a lie. webrtc never had any real version. 0.2 is greater than 0.1
Provides:	webrtc = 0.2
Obsoletes:	webrtc <= 0.1
%if 0%{?shared}
Requires:       chromium-libs%{_isa} = %{epoch}:%{version}-%{release}
# This is broken out so it can be replaced.
Requires:	chromium-libs-media%{_isa} = %{epoch}:%{version}-%{release}
# Nothing to do here. chromium-libs is real.
%else
Provides:	chromium-libs = %{epoch}:%{version}-%{release}
Obsoletes:	chromium-libs <= %{epoch}:%{version}-%{release}
%endif

ExclusiveArch:	x86_64 i686

# Bundled bits (I'm sure I've missed some)
Provides: bundled(angle) = 2422
Provides: bundled(bintrees) = 1.0.1
# This is a fork of openssl.
Provides: bundled(boringssl)
Provides: bundled(brotli) = 222564a95d9ab58865a096b8d9f7324ea5f2e03e
Provides: bundled(bspatch)
Provides: bundled(cacheinvalidation) = 20150720
Provides: bundled(colorama) = 799604a104
Provides: bundled(crashpad)
Provides: bundled(dmg_fp)
Provides: bundled(expat) = 2.2.0
Provides: bundled(fdmlibm) = 5.3
# Don't get too excited. MPEG and other legally problematic stuff is stripped out.
Provides: bundled(ffmpeg) = 3.2git
Provides: bundled(fips181) = 2.2.3
Provides: bundled(fontconfig) = 2.11.0
Provides: bundled(gperftools) = svn144
%if 0%{?bundleharfbuzz}
Provides: bundled(harfbuzz) = 1.4.2
%endif
Provides: bundled(hunspell) = 1.6.0
Provides: bundled(iccjpeg)
%if 0%{?bundleicu}
Provides: bundled(icu) = 58.1
%endif
Provides: bundled(kitchensink) = 1
Provides: bundled(leveldb) = 1.20
Provides: bundled(libaddressinput) = 0
Provides: bundled(libdrm) = 2.4.70
Provides: bundled(libevent) = 1.4.15
Provides: bundled(libjingle) = 9564
%if 0%{?bundlelibjpeg}
Provides: bundled(libjpeg-turbo) = 1.4.90
%endif
Provides: bundled(libphonenumber) = a4da30df63a097d67e3c429ead6790ad91d36cf4
%if 0%{?bundlelibpng}
Provides: bundled(libpng) = 1.6.22
%endif
Provides: bundled(libsrtp) = 1.5.2
%if %{bundlelibusbx}
Provides: bundled(libusbx) = 1.0.17
%endif
Provides: bundled(libvpx) = 1.6.0
%if %{bundlelibwebp}
Provides: bundled(libwebp) = 0.6.0
%endif
%if %{bundlelibxml}
# Well, it's actually newer than 2.9.4 and has code in it that has been reverted upstream... but eh.
Provides: bundled(libxml) = 2.9.4
%endif
Provides: bundled(libXNVCtrl) = 302.17
Provides: bundled(libyuv) = 1651
Provides: bundled(lzma) = 15.14
Provides: bundled(libudis86) = 1.7.1
Provides: bundled(mesa) = 9.0.3
Provides: bundled(NSBezierPath) = 1.0
Provides: bundled(mozc)
Provides: bundled(mt19937ar) = 2002.1.26
%if %{bundleopus}
Provides: bundled(opus) = 1.1.3
%endif
Provides: bundled(ots) = 8d70cffebbfa58f67a5c3ed0e9bc84dccdbc5bc0
Provides: bundled(protobuf) = 3.0.0.beta.3
Provides: bundled(qcms) = 4
%if 0%{?bundlere2}
Provides: bundled(re2)
%endif
Provides: bundled(sfntly) = 04740d2600193b14aa3ef24cd9fbb3d5996b9f77
Provides: bundled(skia)
Provides: bundled(SMHasher) = 0
Provides: bundled(snappy) = 1.1.4-head
Provides: bundled(speech-dispatcher) = 0.7.1
Provides: bundled(sqlite) = 3.17patched
Provides: bundled(superfasthash) = 0
Provides: bundled(talloc) = 2.0.1
Provides: bundled(usrsctp) = 0
Provides: bundled(v8) = 5.9.211.31
Provides: bundled(webrtc) = 90usrsctp
Provides: bundled(woff2) = 445f541996fe8376f3976d35692fd2b9a6eedf2d
Provides: bundled(xdg-mime)
Provides: bundled(xdg-user-dirs)
Provides: bundled(x86inc) = 0
# Provides: bundled(zlib) = 1.2.11

# For selinux scriptlet
Requires(post): /usr/sbin/semanage
Requires(post): /usr/sbin/restorecon

%description
Chromium is an open-source web browser, powered by WebKit (Blink).

%package common
Summary: Files needed for both the headless_shell and full Chromium

%description common
%{summary}.

%if 0%{?shared}
%package libs
Summary: Shared libraries used by chromium (and chrome-remote-desktop)
Requires: chromium-common%{_isa} = %{epoch}:%{version}-%{release}
Requires: chromium-libs-media%{_isa} = %{epoch}:%{version}
Obsoletes: chromium-widevinecdm-plugin < 23.0.0.207

%description libs
Shared libraries used by chromium (and chrome-remote-desktop).

%if %{freeworld}
%package libs-media-freeworld
Summary: Chromium media libraries built with all possible codecs
Provides: chromium-libs-media = %{epoch}:%{version}-%{release}
Provides: chromium-libs-media%{_isa} = %{epoch}:%{version}-%{release}
Obsoletes: chromium-libs-media < %{epoch}:%{version}-%{release}

%description libs-media-freeworld
Chromium media libraries built with all possible codecs. Chromium is an
open-source web browser, powered by WebKit (Blink). This package replaces
the default chromium-libs-media package, which is limited in what it
can include.
%else
%package libs-media
Summary: Shared libraries used by the chromium media subsystem
Requires: chromium-libs%{_isa} = %{epoch}:%{version}

%description libs-media
Shared libraries used by the chromium media subsystem.
%endif
%endif

%if %{build_remote_desktop}
%package -n chrome-remote-desktop
Requires(pre): shadow-utils
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Requires: xorg-x11-server-Xvfb
%if 0%{?rhel} == 7
Requires: python-psutil
%else
Requires: python2-psutil
%endif
%if 0%{?shared}
Requires: chromium-libs%{_isa} = %{epoch}:%{version}-%{release}
%endif
Summary: Remote desktop support for google-chrome & chromium

%description -n chrome-remote-desktop
Remote desktop support for google-chrome & chromium.
%endif


%package -n chromedriver
Summary:	WebDriver for Google Chrome/Chromium
%if 0%{?shared}
Requires:       chromium-libs%{_isa} = %{epoch}:%{version}-%{release}
%endif
# From Russian Fedora (minus the epoch)
Provides:	chromedriver-stable = %{epoch}:%{version}-%{release}
Conflicts:	chromedriver-testing
Conflicts:	chromedriver-unstable

%description -n chromedriver
WebDriver is an open source tool for automated testing of webapps across many
browsers. It provides capabilities for navigating to web pages, user input,
JavaScript execution, and more. ChromeDriver is a standalone server which
implements WebDriver's wire protocol for Chromium. It is being developed by
members of the Chromium and WebDriver teams.

%package headless
Summary:	A minimal headless shell built from Chromium
Requires:	chromium-common%{_isa} = %{epoch}:%{version}-%{release}

%description headless
A minimal headless client built from Chromium. headless_shell is built
without support for alsa, cups, dbus, gconf, gio, kerberos, pulseaudio, or
udev.

%prep
%setup -q -n chromium-%{version}

# Fix Russian Translation
sed -i 's@адежный@адёжный@g' components/strings/components_strings_ru.xtb

# fix debugedit: canonicalization unexpectedly shrank by one character
sed -i 's@gpu//@gpu/@g' content/renderer/gpu/compositor_forwarding_message_filter.cc
sed -i 's@audio_processing//@audio_processing/@g' third_party/webrtc/modules/audio_processing/utility/ooura_fft.cc
sed -i 's@audio_processing//@audio_processing/@g' third_party/webrtc/modules/audio_processing/utility/ooura_fft_sse2.cc

### Chromium Fedora Patches ###
%patch1 -p1 -b .pathmax
%patch2 -p1 -b .addrfix
%patch4 -p1 -b .notest
%patch7 -p1 -b .ignore-fd-count
%patch9 -p1 -b .modern-libusbx
%patch15 -b .sandboxpie
#%patch16 -p1 -b .armwebrtc
%patch17 -p1 -b .armfix
%patch18 -p1 -b .etc
%patch21 -p1 -b .lastcommit
%patch22 -p1 -b .timefix
%patch24 -p1 -b .nullfix
%patch25 -p1 -b .jpegfix
%patch26 -p1 -b .ldmemory
%patch27 -p1 -b .setopaque
%patch31 -p1 -b .permissive
#%patch33 -p1 -b .gcc7
%patch36 -p1 -b .revert
#%patch40 -p1 -b .ucontextfix
%patch42 -p1 -b .noprefix
%patch43 -p1 -b .nomangle
%patch45 -p1 -b .nozmangle
#%if 0%{?rhel} == 7
#%patch46 -p1 -b .kmaxskip
#%patch47 -p1 -b .c99
#%patch54 -p1 -b .gcc5fix
#%patch58 -p1 -b .dde5e35
#%patch59 -p1 -b .gcc-nc
#%patch60 -p1 -b .nonullptr
#%patch61 -p1 -b .another-rvalue-fix
#%endif

#%patch62 -p1 -b .webrtc
%patch63 -p1 -b .nolibc++
%patch64 -p1 -b .ft-hb
%patch65 -p1 -b  .f172c7c

#%patch52 -p1 -b .fixgccagain
%patch53 -p1 -b .nogccoptmath

### Russian Fedora Patches ###
%patch503 -p1 -b .memcpy
%patch504 -p1 -b .cups
%patch505 -p1 -b .angle

%if 0%{vaapi}
%patch600 -p1 -b .vaapi
#%patch601 -p1 -b .specify-max-resolution
%endif

%if 0%{?asan}
%patch502 -p1 -b .clang
export CC="clang"
export CXX="clang++"
%else
export CC="gcc"
export CXX="g++"
%endif
export AR="ar"
export RANLIB="ranlib"

# NUKE FROM ORBIT
#rm -rf buildtools/third_party/libc++/BUILD.gn

%if 0%{?nacl}
# prep the nacl tree
mkdir -p out/Release/gen/sdk/linux_x86/nacl_x86_newlib
cp -a --no-preserve=context /usr/%{_arch}-nacl/* out/Release/gen/sdk/linux_x86/nacl_x86_newlib

mkdir -p out/Release/gen/sdk/linux_x86/nacl_arm_newlib
cp -a --no-preserve=context /usr/arm-nacl/* out/Release/gen/sdk/linux_x86/nacl_arm_newlib

# Not sure if we need this or not, but better safe than sorry.
pushd out/Release/gen/sdk/linux_x86
ln -s nacl_x86_newlib nacl_x86_newlib_raw
ln -s nacl_arm_newlib nacl_arm_newlib_raw
popd

mkdir -p out/Release/gen/sdk/linux_x86/nacl_x86_newlib/bin
pushd out/Release/gen/sdk/linux_x86/nacl_x86_newlib/bin
ln -s /usr/bin/x86_64-nacl-gcc gcc
ln -s /usr/bin/x86_64-nacl-gcc x86_64-nacl-gcc
ln -s /usr/bin/x86_64-nacl-g++ g++
ln -s /usr/bin/x86_64-nacl-g++ x86_64-nacl-g++
# ln -s /usr/bin/x86_64-nacl-ar ar
ln -s /usr/bin/x86_64-nacl-ar x86_64-nacl-ar
# ln -s /usr/bin/x86_64-nacl-as as
ln -s /usr/bin/x86_64-nacl-as x86_64-nacl-as
# ln -s /usr/bin/x86_64-nacl-ranlib ranlib
ln -s /usr/bin/x86_64-nacl-ranlib x86_64-nacl-ranlib
# Cleanups
rm addr2line
ln -s /usr/bin/x86_64-nacl-addr2line addr2line
rm c++filt
ln -s /usr/bin/x86_64-nacl-c++filt c++filt
rm gprof
ln -s /usr/bin/x86_64-nacl-gprof gprof
rm readelf
ln -s /usr/bin/x86_64-nacl-readelf readelf
rm size
ln -s /usr/bin/x86_64-nacl-size size
rm strings
ln -s /usr/bin/x86_64-nacl-strings strings
popd

mkdir -p out/Release/gen/sdk/linux_x86/nacl_arm_newlib/bin
pushd out/Release/gen/sdk/linux_x86/nacl_arm_newlib/bin
ln -s /usr/bin/arm-nacl-gcc gcc
ln -s /usr/bin/arm-nacl-gcc arm-nacl-gcc
ln -s /usr/bin/arm-nacl-g++ g++
ln -s /usr/bin/arm-nacl-g++ arm-nacl-g++
ln -s /usr/bin/arm-nacl-ar arm-nacl-ar
ln -s /usr/bin/arm-nacl-as arm-nacl-as
ln -s /usr/bin/arm-nacl-ranlib arm-nacl-ranlib
popd

touch out/Release/gen/sdk/linux_x86/nacl_x86_newlib/stamp.untar out/Release/gen/sdk/linux_x86/nacl_x86_newlib/stamp.prep
touch out/Release/gen/sdk/linux_x86/nacl_x86_newlib/nacl_x86_newlib.json
touch out/Release/gen/sdk/linux_x86/nacl_arm_newlib/stamp.untar out/Release/gen/sdk/linux_x86/nacl_arm_newlib/stamp.prep
touch out/Release/gen/sdk/linux_x86/nacl_arm_newlib/nacl_arm_newlib.json

pushd out/Release/gen/sdk/linux_x86/
mkdir -p pnacl_newlib pnacl_translator
# Might be able to do symlinks here, but eh.
cp -a --no-preserve=context /usr/pnacl_newlib/* pnacl_newlib/
cp -a --no-preserve=context /usr/pnacl_translator/* pnacl_translator/
for i in lib/libc.a lib/libc++.a lib/libg.a lib/libm.a; do
	/usr/pnacl_newlib/bin/pnacl-ranlib pnacl_newlib/x86_64_bc-nacl/$i
	/usr/pnacl_newlib/bin/pnacl-ranlib pnacl_newlib/i686_bc-nacl/$i
	/usr/pnacl_newlib/bin/pnacl-ranlib pnacl_newlib/le32-nacl/$i
done

for i in lib/libpthread.a lib/libnacl.a; do
	/usr/pnacl_newlib/bin/pnacl-ranlib pnacl_newlib/le32-nacl/$i
done

for i in lib/clang/3.7.0/lib/x86_64_bc-nacl/libpnaclmm.a lib/clang/3.7.0/lib/i686_bc-nacl/libpnaclmm.a; do
	/usr/pnacl_newlib/bin/pnacl-ranlib pnacl_newlib/$i
done

for i in lib/clang/3.7.0/lib/le32-nacl/libpnaclmm.a lib/clang/3.7.0/lib/le32-nacl/libgcc.a; do
	/usr/pnacl_newlib/bin/pnacl-ranlib pnacl_newlib/$i
done

popd

mkdir -p native_client/toolchain/.tars/linux_x86
touch native_client/toolchain/.tars/linux_x86/pnacl_translator.json

pushd native_client/toolchain
ln -s ../../out/Release/gen/sdk/linux_x86 linux_x86
popd

mkdir -p third_party/llvm-build/Release+Asserts/bin
pushd third_party/llvm-build/Release+Asserts/bin
ln -sf /usr/bin/clang clang
ln -sf /usr/bin/clang++ clang++
popd
%endif

# Core defines are flags that are true for both the browser and headless.
CHROMIUM_CORE_GN_DEFINES=""
CHROMIUM_CORE_GN_DEFINES+=' is_debug=false'
%ifarch x86_64
CHROMIUM_CORE_GN_DEFINES+=' system_libdir="lib64"'
%endif
CHROMIUM_CORE_GN_DEFINES+=' google_api_key="%{api_key}" google_default_client_id="%{default_client_id}" google_default_client_secret="%{default_client_secret}"'
%if 0%{?asan}
CHROMIUM_CORE_GN_DEFINES+=' is_clang=true clang_base_path="/usr" clang_use_chrome_plugins=false fatal_linker_warnings=false use_lld=false'
%else
CHROMIUM_CORE_GN_DEFINES+=' is_clang=false'
%endif
CHROMIUM_CORE_GN_DEFINES+=' use_sysroot=false use_gold=false fieldtrial_testing_like_official_build=true  use_custom_libcxx=false'
%if %{freeworld}
CHROMIUM_CORE_GN_DEFINES+=' ffmpeg_branding="ChromeOS" proprietary_codecs=true'
%else
CHROMIUM_CORE_GN_DEFINES+=' ffmpeg_branding="Chromium" proprietary_codecs=false'
%endif
CHROMIUM_CORE_GN_DEFINES+=' treat_warnings_as_errors=false linux_use_bundled_binutils=false use_custom_libcxx=false'
%if 0%{vaapi}
CHROMIUM_CORE_GN_DEFINES+=' use_vaapi=true'
%endif
export CHROMIUM_CORE_GN_DEFINES

CHROMIUM_BROWSER_GN_DEFINES=""
CHROMIUM_BROWSER_GN_DEFINES+=' use_gio=true use_pulseaudio=true icu_use_data_file=true'
%if 0%{?nonacl}
CHROMIUM_BROWSER_GN_DEFINES+=' enable_nacl=false'
%endif
%if 0%{?shared}
CHROMIUM_BROWSER_GN_DEFINES+=' is_component_ffmpeg=true is_component_build=true'
%else
CHROMIUM_BROWSER_GN_DEFINES+=' is_component_ffmpeg=false is_component_build=false'
%endif
CHROMIUM_BROWSER_GN_DEFINES+=' remove_webcore_debug_symbols=true enable_hangout_services_extension=true'
CHROMIUM_BROWSER_GN_DEFINES+=' use_aura=true'
CHROMIUM_BROWSER_GN_DEFINES+=' enable_webrtc=true enable_widevine=true'
%if 0%{gtk3}
CHROMIUM_BROWSER_GN_DEFINES+=' use_gtk3=true'
%else
CHROMIUM_BROWSER_GN_DEFINES+=' use_gtk3=false'
%endif
export CHROMIUM_BROWSER_GN_DEFINES

CHROMIUM_HEADLESS_GN_DEFINES=""
CHROMIUM_HEADLESS_GN_DEFINES+=' use_ozone=true ozone_auto_platforms=false ozone_platform="headless" ozone_platform_headless=true'
CHROMIUM_HEADLESS_GN_DEFINES+=' headless_use_embedded_resources=true icu_use_data_file=false v8_use_external_startup_data=false'
CHROMIUM_HEADLESS_GN_DEFINES+=' enable_nacl=false enable_print_preview=false enable_remoting=false use_alsa=false'
CHROMIUM_HEADLESS_GN_DEFINES+=' use_cups=false use_dbus=false use_gconf=false use_gio=false use_kerberos=false use_libpci=false'
CHROMIUM_HEADLESS_GN_DEFINES+=' use_pulseaudio=false use_udev=false'
export CHROMIUM_HEADLESS_GN_DEFINES

# Remove most of the bundled libraries. Libraries specified below (taken from
# Gentoo's Chromium ebuild) are the libraries that needs to be preserved.
build/linux/unbundle/remove_bundled_libraries.py \
	'buildtools/third_party/libc++' \
	'buildtools/third_party/libc++abi' \
	'third_party/ffmpeg' \
	'third_party/adobe' \
	'third_party/flac' \
	'third_party/harfbuzz-ng' \
	'third_party/icu' \
	'third_party/inspector_protocol' \
	'v8/third_party/inspector_protocol' \
	'third_party/cld_3' \
	'base/third_party/libevent' \
	'third_party/libjpeg_turbo' \
	'third_party/libpng' \
	'third_party/libsrtp' \
	'third_party/libwebp' \
	'third_party/libxml' \
	'third_party/libxslt' \
%if %{freeworld}
	'third_party/openh264' \
%endif
%if 0%{?bundlere2}
	'third_party/re2' \
%endif
	'third_party/snappy' \
	'third_party/speech-dispatcher' \
	'third_party/usb_ids' \
	'third_party/xdg-utils' \
	'third_party/yasm' \
	'third_party/zlib' \
	'base/third_party/dmg_fp' \
	'base/third_party/dynamic_annotations' \
	'base/third_party/icu' \
	'base/third_party/nspr' \
	'base/third_party/superfasthash' \
	'base/third_party/symbolize' \
	'base/third_party/valgrind' \
	'base/third_party/xdg_mime' \
	'base/third_party/xdg_user_dirs' \
	'chrome/third_party/mozilla_security_manager' \
	'courgette/third_party' \
	'native_client_sdk/src/libraries/third_party/newlib-extras' \
	'native_client/src/third_party/dlmalloc' \
	'native_client/src/third_party/valgrind' \
	'net/third_party/mozilla_security_manager' \
	'net/third_party/nss' \
	'third_party/WebKit' \
	'third_party/analytics' \
	'third_party/angle' \
	'third_party/angle/src/common/third_party/base' \
	'third_party/angle/src/common/third_party/smhasher' \
	'third_party/angle/src/third_party/compiler' \
	'third_party/angle/src/third_party/libXNVCtrl' \
	'third_party/angle/src/third_party/trace_event' \
	'third_party/blink' \
	'third_party/blanketjs' \
	'third_party/boringssl' \
	'third_party/boringssl/src/third_party/fiat' \
	'third_party/breakpad' \
	'third_party/breakpad/breakpad/src/third_party/curl' \
	'third_party/brotli' \
	'third_party/cacheinvalidation' \
	'third_party/catapult' \
	'third_party/catapult/common/py_vulcanize/third_party/rcssmin' \
	'third_party/catapult/common/py_vulcanize/third_party/rjsmin' \
	'third_party/catapult/tracing/third_party/d3' \
	'third_party/catapult/tracing/third_party/gl-matrix' \
	'third_party/catapult/tracing/third_party/jszip' \
	'third_party/catapult/tracing/third_party/mannwhitneyu' \
	'third_party/catapult/tracing/third_party/oboe' \
	'third_party/catapult/tracing/third_party/pako' \
	'third_party/catapult/third_party/polymer' \
	'third_party/ced' \
	'third_party/crc32c' \
	'third_party/cros_system_api' \
	'third_party/devscripts' \
	'third_party/dom_distiller_js' \
	'third_party/expat' \
	'third_party/fips181' \
        'third_party/flatbuffers' \
	'third_party/flot' \
	'third_party/freetype' \
	'third_party/glslang-angle' \
	'third_party/google_input_tools' \
	'third_party/google_input_tools/third_party/closure_library' \
	'third_party/google_input_tools/third_party/closure_library/third_party/closure' \
	'third_party/googletest' \
	'third_party/hunspell' \
	'third_party/libdrm' \
	'third_party/iccjpeg' \
%if 0%{?bundlejinja2}
	'third_party/jinja2' \
%endif
	'third_party/jstemplate' \
	'third_party/khronos' \
	'third_party/leveldatabase' \
	'third_party/libXNVCtrl' \
	'third_party/libaddressinput' \
	'third_party/libjingle' \
	'third_party/libphonenumber' \
	'third_party/libsecret' \
	'third_party/libsrtp' \
	'third_party/libudev' \
	'third_party/libusb' \
	'third_party/libvpx' \
	'third_party/libvpx/source/libvpx/third_party/x86inc' \
	'third_party/libxml/chromium' \
	'third_party/libwebm' \
	'third_party/libyuv' \
%if 0%{?nacl}
	'third_party/llvm-build' \
%endif
	'third_party/lss' \
	'third_party/lzma_sdk' \
	'third_party/mesa' \
	'third_party/metrics_proto' \
	'third_party/modp_b64' \
	'third_party/mt19937ar' \
	'third_party/node' \
	'third_party/node/node_modules/polymer-bundler/lib/third_party/UglifyJS2' \
	'third_party/openmax_dl' \
	'third_party/opus' \
	'third_party/ots' \
	'third_party/pdfium' \
	'third_party/pdfium/third_party/agg23' \
	'third_party/pdfium/third_party/base' \
	'third_party/pdfium/third_party/build' \
	'third_party/pdfium/third_party/bigint' \
	'third_party/pdfium/third_party/freetype' \
	'third_party/pdfium/third_party/lcms' \
	'third_party/pdfium/third_party/libopenjpeg20' \
	'third_party/pdfium/third_party/libpng16' \
	'third_party/pdfium/third_party/libtiff' \
	'third_party/polymer' \
	'third_party/protobuf' \
	'third_party/protobuf/third_party/six' \
	'third_party/ply' \
	'third_party/qcms' \
	'third_party/qunit' \
	'third_party/sfntly' \
	'third_party/sinonjs' \
	'third_party/skia' \
	'third_party/skia/third_party/gif' \
	'third_party/skia/third_party/vulkan' \
	'third_party/smhasher' \
	'third_party/spirv-headers' \
	'third_party/spirv-tools-angle' \
	'third_party/sqlite' \
	'third_party/swiftshader' \
	'third_party/swiftshader/third_party/llvm-subzero' \
	'third_party/swiftshader/third_party/subzero' \
	'third_party/tcmalloc' \
	'third_party/usrsctp' \
	'third_party/vulkan' \
	'third_party/vulkan-validation-layers' \
	'third_party/web-animations-js' \
	'third_party/webdriver' \
	'third_party/webrtc' \
	'third_party/widevine' \
	'third_party/woff2' \
	'third_party/zlib/google' \
	'url/third_party/mozilla' \
	'v8/src/third_party/valgrind' \
	--do-remove

# Look, I don't know. This package is spit and chewing gum. Sorry.

%if ! 0%{?bundlejinja2}
rm -rf third_party/jinja2
ln -s %{python_sitelib}/jinja2 third_party/jinja2
%endif
rm -rf third_party/markupsafe
ln -s %{python_sitearch}/markupsafe third_party/markupsafe
# We should look on removing other python packages as well i.e. ply

%if %{build_remote_desktop}
# Fix hardcoded path in remoting code
sed -i 's|/opt/google/chrome-remote-desktop|%{crd_path}|g' remoting/host/setup/daemon_controller_delegate_linux.cc
%endif

export PATH=$PATH:%{_builddir}/depot_tools

build/linux/unbundle/replace_gn_files.py --system-libraries \
	flac \
	freetype \
%if 0%{?bundleharfbuzz}
%else
	harfbuzz-ng \
%endif
%if 0%{?bundleicu}
%else
	icu \
%endif
	libdrm \
%if %{bundlelibjpeg}
%else
	libjpeg \
%endif
%if %{bundlelibpng}
%else
	libpng \
%endif
%if %{bundlelibusbx}
%else
	libusb \
%endif
%if %{bundlelibwebp}
%else
	libwebp \
%endif
%if %{bundlelibxml}
%else
	libxml \
%endif
	libxslt \
%if %{bundleopus}
%else
	opus \
%endif
%if 0%{?bundlere2}
%else
	re2 \
%endif
	yasm \
	zlib

%if 0%{?rhel} == 7
. /opt/rh/devtoolset-7/enable
%endif

tools/gn/bootstrap/bootstrap.py -v --gn-gen-args "$CHROMIUM_CORE_GN_DEFINES $CHROMIUM_BROWSER_GN_DEFINES"
%{target}/gn gen --args="$CHROMIUM_CORE_GN_DEFINES $CHROMIUM_BROWSER_GN_DEFINES" %{target}

%{target}/gn gen --args="$CHROMIUM_CORE_GN_DEFINES $CHROMIUM_HEADLESS_GN_DEFINES" %{headlesstarget}

%if %{bundlelibusbx}
# no hackity hack hack
%else
# hackity hack hack
rm -rf third_party/libusb/src/libusb/libusb.h
# we _shouldn't need to do this, but it looks like we do.
cp -a %{_includedir}/libusb-1.0/libusb.h third_party/libusb/src/libusb/libusb.h
%endif

# make up a version for widevine
sed '14i#define WIDEVINE_CDM_VERSION_STRING "Something fresh"' -i "third_party/widevine/cdm/stub/widevine_cdm_version.h"

# Hard code extra version
FILE=chrome/common/channel_info_posix.cc
sed -i.orig -e 's/getenv("CHROME_VERSION_EXTRA")/"Russian Fedora"/' $FILE

# fix arm gcc
sed -i 's|arm-linux-gnueabihf-|arm-linux-gnu-|g' build/toolchain/linux/BUILD.gn

# setup node
mkdir -p third_party/node/linux/node-linux-x64/bin
ln -s /usr/bin/node third_party/node/linux/node-linux-x64/bin/node

%build
%if 0%{?rhel} == 7
. /opt/rh/devtoolset-7/enable
%endif

# Now do the full browser
# Do headless first.
ninja -C %{headlesstarget} -vvv headless_shell

ninja -C %{target} -vvv chrome chrome_sandbox chromedriver widevinecdmadapter clearkeycdm policy_templates

%if %{build_remote_desktop}

# remote client
pushd remoting

# ../../depot_tools/ninja -C ../%{target} -vvv remoting_me2me_host remoting_start_host remoting_it2me_native_messaging_host remoting_me2me_native_messaging_host remoting_native_messaging_manifests remoting_resources
ninja -C ../%{target} -vvv remoting_all
%if 0%{?build_remoting_app}
%if 0%{?nacl}
GOOGLE_CLIENT_ID_REMOTING_IDENTITY_API=%{chromoting_client_id} ninja -vv -C ../out/Release/ remoting_webapp
%endif
%endif
popd
%endif

# Nuke nacl/pnacl bits at the end of the build
rm -rf out/Release/gen/sdk
rm -rf native_client/toolchain
rm -rf third_party/llvm-build/*

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{chromium_path}
cp -a %{SOURCE3} %{buildroot}%{chromium_path}/%{chromium_browser_channel}.sh
export BUILD_TARGET=`cat /etc/redhat-release`
export CHROMIUM_PATH=%{chromium_path}
export CHROMIUM_BROWSER_CHANNEL=%{chromium_browser_channel}
sed -i "s|@@BUILD_TARGET@@|$BUILD_TARGET|g" %{buildroot}%{chromium_path}/%{chromium_browser_channel}.sh
sed -i "s|@@CHROMIUM_PATH@@|$CHROMIUM_PATH|g" %{buildroot}%{chromium_path}/%{chromium_browser_channel}.sh
sed -i "s|@@CHROMIUM_BROWSER_CHANNEL@@|$CHROMIUM_BROWSER_CHANNEL|g" %{buildroot}%{chromium_path}/%{chromium_browser_channel}.sh
%if "%{chromium_channel}" == "%%{nil}"
sed -i "s|@@EXTRA_FLAGS@@||g" %{buildroot}%{chromium_path}/%{chromium_browser_channel}.sh
%else
# Enable debug outputs for beta and dev channels
export EXTRA_FLAGS="--enable-logging=stderr --v=2"
sed -i "s|@@EXTRA_FLAGS@@|$EXTRA_FLAGS|g" %{buildroot}%{chromium_path}/%{chromium_browser_channel}.sh
%endif

ln -s %{chromium_path}/%{chromium_browser_channel}.sh %{buildroot}%{_bindir}/%{chromium_browser_channel}
mkdir -p %{buildroot}%{_mandir}/man1/

pushd %{target}
cp -a *.pak locales resources icudtl.dat %{buildroot}%{chromium_path}
%if 0%{?nacl}
cp -a nacl_helper* *.nexe pnacl tls_edit %{buildroot}%{chromium_path}
chmod -x %{buildroot}%{chromium_path}/nacl_helper_bootstrap* *.nexe
%endif
cp -a protoc pyproto %{buildroot}%{chromium_path}
cp -a chrome %{buildroot}%{chromium_path}/%{chromium_browser_channel}
cp -a chrome_sandbox %{buildroot}%{chromium_path}/chrome-sandbox
cp -a ../../chrome/app/resources/manpage.1.in %{buildroot}%{_mandir}/man1/%{chromium_browser_channel}.1
sed -i "s|@@PACKAGE@@|%{chromium_browser_channel}|g" %{buildroot}%{_mandir}/man1/%{chromium_browser_channel}.1
sed -i "s|@@MENUNAME@@|%{chromium_menu_name}|g" %{buildroot}%{_mandir}/man1/%{chromium_browser_channel}.1
# V8 initial snapshots
# https://code.google.com/p/chromium/issues/detail?id=421063
cp -a natives_blob.bin %{buildroot}%{chromium_path}
cp -a snapshot_blob.bin %{buildroot}%{chromium_path}
%if 0%{?shared}
cp -a lib*.so* %{buildroot}%{chromium_path}
%endif

# chromedriver
cp -a chromedriver %{buildroot}%{chromium_path}/chromedriver
ln -s %{chromium_path}/chromedriver %{buildroot}%{_bindir}/chromedriver

%if %{build_remote_desktop}
# Remote desktop bits
mkdir -p %{buildroot}%{crd_path}

%if 0%{?shared}
pushd %{buildroot}%{crd_path}
for i in ../chromium-browser%{?chromium_channel}/lib*.so; do
	libname=`basename $i`
	ln -s $i $libname
done
popd
%endif

# See remoting/host/installer/linux/Makefile for logic
cp -a remoting_native_messaging_host %{buildroot}%{crd_path}/native-messaging-host
cp -a remote_assistance_host %{buildroot}%{crd_path}/remote-assistance-host
cp -a remoting_locales %{buildroot}%{crd_path}/
cp -a remoting_me2me_host %{buildroot}%{crd_path}/chrome-remote-desktop-host
cp -a remoting_start_host %{buildroot}%{crd_path}/start-host
cp -a remoting_user_session %{buildroot}%{crd_path}/user-session

# chromium
mkdir -p %{buildroot}%{_sysconfdir}/chromium/native-messaging-hosts
# google-chrome
mkdir -p %{buildroot}%{_sysconfdir}/opt/chrome/
cp -a remoting/* %{buildroot}%{_sysconfdir}/chromium/native-messaging-hosts/
for i in %{buildroot}%{_sysconfdir}/chromium/native-messaging-hosts/*.json; do
	sed -i 's|/opt/google/chrome-remote-desktop|%{crd_path}|g' $i
done
mkdir -p %{buildroot}%{_sysconfdir}/opt/chrome/native-messaging-hosts
pushd %{buildroot}%{_sysconfdir}/opt/chrome/native-messaging-hosts
for i in ../../../chromium/native-messaging-hosts/*; do
# rpm gets unhappy when we symlink here
	cp -a $i .
done
popd

mkdir -p %{buildroot}/var/lib/chrome-remote-desktop
touch %{buildroot}/var/lib/chrome-remote-desktop/hashes

mkdir -p %{buildroot}%{_sysconfdir}/pam.d/
pushd %{buildroot}%{_sysconfdir}/pam.d/
ln -s system-auth chrome-remote-desktop
popd

%if 0%{?build_remoting_app}
%if 0%{?nacl}
cp -a remoting_client_plugin_newlib.* %{buildroot}%{chromium_path}
%endif
%endif
%endif
popd

pushd %{headlesstarget}
cp -a headless_lib.pak headless_shell %{buildroot}%{chromium_path}
popd

%if %{build_remote_desktop}
cp -a remoting/host/linux/linux_me2me_host.py %{buildroot}%{crd_path}/chrome-remote-desktop
cp -a remoting/host/installer/linux/is-remoting-session %{buildroot}%{crd_path}/

mkdir -p %{buildroot}%{_unitdir}
cp -a %{SOURCE11} %{buildroot}%{_unitdir}/
sed -i 's|@@CRD_PATH@@|%{crd_path}|g' %{buildroot}%{_unitdir}/chrome-remote-desktop@.service
%endif

# Add directories for policy management
mkdir -p %{buildroot}%{_sysconfdir}/chromium/policies/managed
mkdir -p %{buildroot}%{_sysconfdir}/chromium/policies/recommended

cp -a out/Release/gen/chrome/app/policy/common/html/en-US/*.html .
cp -a out/Release/gen/chrome/app/policy/linux/examples/chrome.json .

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/256x256/apps
cp -a chrome/app/theme/chromium/product_logo_256.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/%{chromium_browser_channel}.png
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/128x128/apps
cp -a chrome/app/theme/chromium/product_logo_128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{chromium_browser_channel}.png
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/64x64/apps
cp -a chrome/app/theme/chromium/product_logo_64.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{chromium_browser_channel}.png
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
cp -a chrome/app/theme/chromium/product_logo_48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{chromium_browser_channel}.png
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/24x24/apps
cp -a chrome/app/theme/chromium/product_logo_24.png %{buildroot}%{_datadir}/icons/hicolor/24x24/apps/%{chromium_browser_channel}.png
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/22x22/apps
cp -a chrome/app/theme/chromium/product_logo_22.png %{buildroot}%{_datadir}/icons/hicolor/22x22/apps/%{chromium_browser_channel}.png

# Install the master_preferences file
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
install -m 0644 %{SOURCE13} %{buildroot}%{_sysconfdir}/%{name}/

mkdir -p %{buildroot}%{_datadir}/applications/
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE4}

install -D -m0644 chrome/installer/linux/common/chromium-browser/chromium-browser.appdata.xml ${RPM_BUILD_ROOT}%{_datadir}/appdata/%{chromium_browser_channel}.appdata.xml
appstream-util validate-relax --nonet ${RPM_BUILD_ROOT}%{_datadir}/appdata/%{chromium_browser_channel}.appdata.xml

mkdir -p %{buildroot}%{_datadir}/gnome-control-center/default-apps/
cp -a %{SOURCE9} %{buildroot}%{_datadir}/gnome-control-center/default-apps/

mkdir -p %{buildroot}%{chromium_path}/PepperFlash

%post
# Set SELinux labels - semanage itself will adjust the lib directory naming
# But only do it when selinux is enabled, otherwise, it gets noisy.
if selinuxenabled; then
	semanage fcontext -a -t bin_t /usr/lib/%{chromium_browser_channel}
	semanage fcontext -a -t bin_t /usr/lib/%{chromium_browser_channel}/%{chromium_browser_channel}.sh
	semanage fcontext -a -t chrome_sandbox_exec_t /usr/lib/chrome-sandbox
	restorecon -R -v %{chromium_path}/%{chromium_browser_channel}
fi

touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
update-desktop-database &> /dev/null || :

%postun
if [ $1 -eq 0 ] ; then
	touch --no-create %{_datadir}/icons/hicolor &>/dev/null
	gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi
update-desktop-database &> /dev/null || :

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%if %{build_remote_desktop}
%pretrans -n chrome-remote-desktop -p <lua>
path = "/etc/opt/chrome/native-messaging-hosts"
st = posix.stat(path)
if st and st.type == "link" then
  os.remove(path)
end

%pre -n chrome-remote-desktop
getent group chrome-remote-desktop >/dev/null || groupadd -r chrome-remote-desktop

%post -n chrome-remote-desktop
%systemd_post chrome-remote-desktop@.service

%preun -n chrome-remote-desktop
%systemd_preun chrome-remote-desktop@.service

%postun -n chrome-remote-desktop
%systemd_postun_with_restart chrome-remote-desktop@.service
%endif

%files
%doc AUTHORS
%doc chrome_policy_list.html *.json
%license LICENSE
%config %{_sysconfdir}/%{name}/
%if %{build_remote_desktop}
%dir %{_sysconfdir}/%{name}/native-messaging-hosts
# This is chrome-remote-desktop stuff
%exclude %{_sysconfdir}/%{name}/native-messaging-hosts/*
%endif
%{_bindir}/%{chromium_browser_channel}
%dir %{chromium_path}
%{chromium_path}/*.bin
%{chromium_path}/chrome_*.pak
%{chromium_path}/keyboard_resources.pak
%{chromium_path}/resources.pak
%{chromium_path}/views_mus_resources.pak
%{chromium_path}/icudtl.dat
%{chromium_path}/%{chromium_browser_channel}
%{chromium_path}/%{chromium_browser_channel}.sh
%if 0%{?nacl}
%{chromium_path}/nacl_helper*
%{chromium_path}/*.nexe
%{chromium_path}/pnacl/
%{chromium_path}/tls_edit
%endif
%dir %{chromium_path}/PepperFlash/
%{chromium_path}/protoc
# %%{chromium_path}/remoting_locales/
# %%{chromium_path}/pseudo_locales/
# %%{chromium_path}/plugins/
%attr(4755, root, root) %{chromium_path}/chrome-sandbox
%{_mandir}/man1/%{chromium_browser_channel}.*
%{_datadir}/icons/hicolor/*/apps/%{chromium_browser_channel}.png
%{_datadir}/applications/*.desktop
%{_datadir}/appdata/*.appdata.xml
%{_datadir}/gnome-control-center/default-apps/chromium-browser.xml

%files common
%{chromium_path}/headless_lib.pak
%{chromium_path}/mus_app_resources_*.pak
%{chromium_path}/pyproto/
%{chromium_path}/resources/
%dir %{chromium_path}/locales/
%lang(am) %{chromium_path}/locales/am.pak
%lang(am) %{chromium_path}/locales/am.pak.info
%lang(ar) %{chromium_path}/locales/ar.pak
%lang(ar) %{chromium_path}/locales/ar.pak.info
%lang(bg) %{chromium_path}/locales/bg.pak
%lang(bg) %{chromium_path}/locales/bg.pak.info
%lang(bn) %{chromium_path}/locales/bn.pak
%lang(bn) %{chromium_path}/locales/bn.pak.info
%lang(ca) %{chromium_path}/locales/ca.pak
%lang(ca) %{chromium_path}/locales/ca.pak.info
%lang(cs) %{chromium_path}/locales/cs.pak
%lang(cs) %{chromium_path}/locales/cs.pak.info
%lang(da) %{chromium_path}/locales/da.pak
%lang(da) %{chromium_path}/locales/da.pak.info
%lang(de) %{chromium_path}/locales/de.pak
%lang(de) %{chromium_path}/locales/de.pak.info
%lang(el) %{chromium_path}/locales/el.pak
%lang(el) %{chromium_path}/locales/el.pak.info
%lang(en_GB) %{chromium_path}/locales/en-GB.pak
%lang(en_GB) %{chromium_path}/locales/en-GB.pak.info
%lang(en_US) %{chromium_path}/locales/en-US.pak
%lang(en_US) %{chromium_path}/locales/en-US.pak.info
%lang(es) %{chromium_path}/locales/es.pak
%lang(es) %{chromium_path}/locales/es.pak.info
%lang(es) %{chromium_path}/locales/es-419.pak
%lang(es) %{chromium_path}/locales/es-419.pak.info
%lang(et) %{chromium_path}/locales/et.pak
%lang(et) %{chromium_path}/locales/et.pak.info
%lang(fa) %{chromium_path}/locales/fa.pak
%lang(fa) %{chromium_path}/locales/fa.pak.info
%lang(fi) %{chromium_path}/locales/fi.pak
%lang(fi) %{chromium_path}/locales/fi.pak.info
%lang(fil) %{chromium_path}/locales/fil.pak
%lang(fil) %{chromium_path}/locales/fil.pak.info
%lang(fr) %{chromium_path}/locales/fr.pak
%lang(fr) %{chromium_path}/locales/fr.pak.info
%lang(gu) %{chromium_path}/locales/gu.pak
%lang(gu) %{chromium_path}/locales/gu.pak.info
%lang(he) %{chromium_path}/locales/he.pak
%lang(he) %{chromium_path}/locales/he.pak.info
%lang(hi) %{chromium_path}/locales/hi.pak
%lang(hi) %{chromium_path}/locales/hi.pak.info
%lang(hr) %{chromium_path}/locales/hr.pak
%lang(hr) %{chromium_path}/locales/hr.pak.info
%lang(hu) %{chromium_path}/locales/hu.pak
%lang(hu) %{chromium_path}/locales/hu.pak.info
%lang(id) %{chromium_path}/locales/id.pak
%lang(id) %{chromium_path}/locales/id.pak.info
%lang(it) %{chromium_path}/locales/it.pak
%lang(it) %{chromium_path}/locales/it.pak.info
%lang(ja) %{chromium_path}/locales/ja.pak
%lang(ja) %{chromium_path}/locales/ja.pak.info
%lang(kn) %{chromium_path}/locales/kn.pak
%lang(kn) %{chromium_path}/locales/kn.pak.info
%lang(ko) %{chromium_path}/locales/ko.pak
%lang(ko) %{chromium_path}/locales/ko.pak.info
%lang(lt) %{chromium_path}/locales/lt.pak
%lang(lt) %{chromium_path}/locales/lt.pak.info
%lang(lv) %{chromium_path}/locales/lv.pak
%lang(lv) %{chromium_path}/locales/lv.pak.info
%lang(ml) %{chromium_path}/locales/ml.pak
%lang(ml) %{chromium_path}/locales/ml.pak.info
%lang(mr) %{chromium_path}/locales/mr.pak
%lang(mr) %{chromium_path}/locales/mr.pak.info
%lang(ms) %{chromium_path}/locales/ms.pak
%lang(ms) %{chromium_path}/locales/ms.pak.info
%lang(nb) %{chromium_path}/locales/nb.pak
%lang(nb) %{chromium_path}/locales/nb.pak.info
%lang(nl) %{chromium_path}/locales/nl.pak
%lang(nl) %{chromium_path}/locales/nl.pak.info
%lang(pl) %{chromium_path}/locales/pl.pak
%lang(pl) %{chromium_path}/locales/pl.pak.info
%lang(pt_BR) %{chromium_path}/locales/pt-BR.pak
%lang(pt_BR) %{chromium_path}/locales/pt-BR.pak.info
%lang(pt_PT) %{chromium_path}/locales/pt-PT.pak
%lang(pt_PT) %{chromium_path}/locales/pt-PT.pak.info
%lang(ro) %{chromium_path}/locales/ro.pak
%lang(ro) %{chromium_path}/locales/ro.pak.info
%lang(ru) %{chromium_path}/locales/ru.pak
%lang(ru) %{chromium_path}/locales/ru.pak.info
%lang(sk) %{chromium_path}/locales/sk.pak
%lang(sk) %{chromium_path}/locales/sk.pak.info
%lang(sl) %{chromium_path}/locales/sl.pak
%lang(sl) %{chromium_path}/locales/sl.pak.info
%lang(sr) %{chromium_path}/locales/sr.pak
%lang(sr) %{chromium_path}/locales/sr.pak.info
%lang(sv) %{chromium_path}/locales/sv.pak
%lang(sv) %{chromium_path}/locales/sv.pak.info
%lang(sw) %{chromium_path}/locales/sw.pak
%lang(sw) %{chromium_path}/locales/sw.pak.info
%lang(ta) %{chromium_path}/locales/ta.pak
%lang(ta) %{chromium_path}/locales/ta.pak.info
%lang(te) %{chromium_path}/locales/te.pak
%lang(te) %{chromium_path}/locales/te.pak.info
%lang(th) %{chromium_path}/locales/th.pak
%lang(th) %{chromium_path}/locales/th.pak.info
%lang(tr) %{chromium_path}/locales/tr.pak
%lang(tr) %{chromium_path}/locales/tr.pak.info
%lang(uk) %{chromium_path}/locales/uk.pak
%lang(uk) %{chromium_path}/locales/uk.pak.info
%lang(vi) %{chromium_path}/locales/vi.pak
%lang(vi) %{chromium_path}/locales/vi.pak.info
%lang(zh_CN) %{chromium_path}/locales/zh-CN.pak
%lang(zh_CN) %{chromium_path}/locales/zh-CN.pak.info
%lang(zh_TW) %{chromium_path}/locales/zh-TW.pak
%lang(zh_TW) %{chromium_path}/locales/zh-TW.pak.info

%files headless
%{chromium_path}/headless_shell

%if 0%{?shared}
%files libs
%exclude %{chromium_path}/libffmpeg.so*
%exclude %{chromium_path}/libmedia.so*
%exclude %{chromium_path}/libwidevinecdm.so*
%{chromium_path}/lib*.so*

%if %{freeworld}
%files libs-media-freeworld
%else
%files libs-media
%endif
%{chromium_path}/libffmpeg.so*
%{chromium_path}/libmedia.so*
%{chromium_path}/libwidevinecdm.so*
%endif

%if %{build_remote_desktop}
%files -n chrome-remote-desktop
%{crd_path}/chrome-remote-desktop
%{crd_path}/chrome-remote-desktop-host
%{crd_path}/is-remoting-session
%if 0%{?shared}
%{crd_path}/lib*.so
%endif
%if %{build_remote_desktop}
%{crd_path}/native-messaging-host
%{crd_path}/remote-assistance-host
%{_sysconfdir}/pam.d/chrome-remote-desktop
%{_sysconfdir}/chromium/native-messaging-hosts/*
%{_sysconfdir}/opt/chrome/
%{crd_path}/remoting_locales/
%{crd_path}/start-host
%{crd_path}/user-session
%{_unitdir}/chrome-remote-desktop@.service
/var/lib/chrome-remote-desktop/
%endif
%if 0%{?build_remoting_app}
%if 0%{?nacl}
%{chromium_path}/remoting_client_plugin_newlib.*
%endif
%endif
%endif

%files -n chromedriver
%doc AUTHORS
%license LICENSE
%{_bindir}/chromedriver
%{chromium_path}/chromedriver

%changelog
* Wed Feb 14 2018 Arkady L. Shane <ashejn@russianfedora.pro> 64.0.3282.167-1.R
- update to 64.0.3282.167

* Fri Feb  2 2018 Arkady L. Shane <ashejn@russianfedora.pro> 64.0.3282.140-1.R
- update to 64.0.3282.140
- include user-session binary in chrome-remote-desktop subpackage

* Sun Jan 28 2018 Arkady L. Shane <ashejn@russianfedora.pro> 64.0.3282.119-2.R
- ok, enable vaapi.

* Thu Jan 25 2018 Arkady L. Shane <ashejn@russianfedora.pro> 64.0.3282.119-1.R
- update to 64.0.3282.119
- disable vaapi for stable

* Thu Jan 25 2018 Arkady L. Shane <ashejn@russianfedora.pro> 64.0.3282.113-2.R
- allow fallback max resolution for VA to be read from file

* Wed Jan 24 2018 Arkady L. Shane <ashejn@russianfedora.pro> 64.0.3282.113-1.R
- update to 64.0.3282.113

* Mon Jan 22 2018 Arkady L. Shane <ashejn@russianfedora.pro> 64.0.3282.99-1.R
- update 64.0.3282.99
- try to enable vaapi

* Thu Jan 11 2018 Arkady L. Shane <ashejn@russianfedora.pro> 64.0.3282.85-1.R
- update to 64.0.3282.85

* Sun Jan  7 2018 Arkady L. Shane <ashejn@russianfedora.pro> 64.0.3282.71-1.R
- update to 64.0.3282.71

* Mon Dec 25 2017 Arkady L. Shane <ashejn@russianfedora.pro> 64.0.3282.39-1.R
- update to 64.0.3282.39
- apply some Gentoo patches and drop old

* Fri Dec 15 2017 Arkady L. Shane <ashejn@russianfedora.pro> 63.0.3239.108-1.R
- update to 63.0.3239.108

* Tue Dec 12 2017 Arkady L. Shane <ashejn@russianfedora.pro> 63.0.3239.84-2.R
- enable remote desktop
- build with system freetype and harfbuzz

* Thu Dec  7 2017 Arkady L. Shane <ashejn@russianfedora.pro> 63.0.3239.84-1.R
- fix build with clang
- update to 63.0.3239.84
- disable build of remote desktop

* Thu Nov 30 2017 Arkady L. Shane <ashejn@russianfedora.pro> 63.0.3239.70-1.R
- update to 63.0.3239.70
- disable arm webrtc patch
- update opaque patch
- disable ucontext-fix patch
- update opus patch
- update harfbuzz patch
- disable bootstrap patch
- disable std++17 patch
- apped gentoo webrtc patch
- build with clang

* Wed Nov 15 2017 Arkady L. Shane <ashejn@russianfedora.pro> 62.0.3202.94-1.R
- update to 62.0.3202.94

* Tue Nov  7 2017 Arkady L. Shane <ashejn@russianfedora.pro> 62.0.3202.89-1.R
- 62.0.3202.89

* Fri Oct 27 2017 Arkady L. Shane <ashejn@russianfedora.pro> 62.0.3202.75-1.R
- update to 62.0.3202.75
- use devtoolset-7-toolchain to build on epel7
- use bundled libjpeg for RHEL 7

* Mon Oct 23 2017 Arkady L. Shane <ashejn@russianfedora.pro> 62.0.3202.62-2.R
- use flag use_cxx11 = true for RHEL 7

* Wed Oct 18 2017 Arkady L. Shane <ashejn@russianfedora.pro> 62.0.3202.62-1.R
- update to 62.0.3202.62
- patch crc32c sources instead of use c++17 everywere

* Mon Oct 16 2017 Arkady L. Shane <ashejn@russianfedora.pro> 62.0.3202.52-1.R
- update to 62.0.3202.52

* Thu Oct  5 2017 Arkady L. Shane <ashejn@russianfedora.pro> 62.0.3202.45-1.R
- update to 62.0.3202.45
- update kmaxskip-constexpr patch
- use std++17 standart

* Wed Oct  4 2017 Arkady L. Shane <ashejn@russianfedora.pro> 62.0.3202.38-1.R
- update to 62.0.3202.38
- drop camfix patch
- update patches
- drop atk patch

* Fri Sep 22 2017 Arkady L. Shane <ashejn@russianfedora.pro> 61.0.3163.100-1.R
- update to 61.0.3163.100
- lots of epel7 specific fixes
- use bundled libpng on epel7
- try to build with gtk3 for RHEL

* Sat Sep 16 2017 Arkady L. Shane <ashejn@russianfedora.pro> 61.0.3163.91-1.R
- update to 61.0.3163.91

* Wed Sep  6 2017 Arkady L. Shane <ashejn@russianfedora.pro> 61.0.3163.79-1.R
- update to 61.0.3163.79

* Thu Aug 31 2017 Arkady L. Shane <ashejn@russianfedora.pro> 61.0.3163.71-1.R
- update to 61.0.3163.71

* Mon Aug 28 2017 Arkady L. Shane <ashejn@russianfedora.pro> 61.0.3163.59-2.R
- fix dep issue with chrome-remote-desktop on el7
- added more provides

* Thu Aug 24 2017 Arkady L. Shane <ashejn@russianfedora.pro> 61.0.3163.59-1.R
- update to 61.0.3163.59
- apply gentoo atk patch

* Fri Aug 18 2017 Arkady L. Shane <ashejn@russianfedora.pro> 61.0.3163.49-1.R
- update to 61.0.3163.49
- update boot strap patch
- update setopaque patch
- update depot_tools.git-master.tar.gz

* Tue Aug 15 2017 Arkady L. Shane <ashejn@russianfedora.pro> 60.0.3112.101-1.R
- update to 60.0.3112.101

* Wed Aug  9 2017 Arkady L. Shane <ashejn@russianfedora.pro> 60.0.3112.90-2.R
- disable debuginfo package
- build with system libjpeg, webp and libpng
- added common and headless packages
- apply post 60 code commit to get code building on epel7
- fix build with gtk2 on RHEL < 7.4
- fix WebKit layout to build with old gcc

* Mon Aug  7 2017 Arkady L. Shane <ashejn@russianfedora.pro> 60.0.3112.90-1.R
- update to 60.0.3112.90
- apply ucontext patch
- drop freetype patch

* Thu Jul 20 2017 Arkady L. Shane <ashejn@russianfedora.pro> 60.0.3112.78-1.R
- update to 60.0.3112.78
- drop ugly hack for freetype

* Fri Jun 30 2017 Arkady L. Shane <ashejn@russianfedora.pro> 59.0.3071.115-2.R
- use freetype archive from git

* Tue Jun 27 2017 Arkady L. Shane <ashejn@russianfedora.pro> 59.0.3071.115-1.R
- update to 59.0.3071.115
- fix native-messaging-hosts dir to be a true dir instead of a symlink
- copy files into /etc/opt/chrome/native-messaging-hosts instead of making
  symlinks this results in duplicate copies of the same files, but eh. making
  rpm happy.
- fix build with missing freetype
- fix https://bugs.chromium.org/p/skia/issues/detail?id=6663

* Wed Jun 21 2017 Arkady L. Shane <ashejn@russianfedora.pro> 59.0.3071.109-1.R
- update to 59.0.3071.109

* Fri Jun 16 2017 Arkady L. Shane <ashejn@russianfedora.pro> 59.0.3071.104-1.R
- update to 59.0.3071.104
- added more system icons
- use appdata xml from tarball
- update bundle versions

* Tue Jun  6 2017 Arkady L. Shane <ashejn@russianfedora.pro> 59.0.3071.86-1.R
- update to 59.0.3071.86
- use bundled harfbuzz for Fedora less then 26

* Thu Jun  1 2017 Arkady L. Shane <ashejn@russianfedora.pro> 59.0.3071.83-1.R
- update to 59.0.3071.83

* Wed May 17 2017 Arkady L. Shane <ashejn@russianfedora.pro> 58.0.3029.110-2.R
- fix https://bugzilla.redhat.com/show_bug.cgi?id=1446851

* Thu May 11 2017 Arkady L. Shane <ashejn@russianfedora.pro> 58.0.3029.110-1.R
- update to 58.0.3029.110

* Wed May  3 2017 Arkady L. Shane <ashejn@russianfedora.pro> 58.0.3029.96-1.R
- update to 58.0.3029.96
- use new service file name

* Thu Apr 20 2017 Arkady L. Shane <ashejn@russianfedora.pro> 58.0.3029.81-1.R
- update to 58.0.3029.81

* Thu Mar 30 2017 Arkady L. Shane <ashejn@russianfedora.pro> 57.0.2987.133-1.R
- update to 57.0.2987.133

* Sun Feb  5 2017 Arkady L. Shane <ashejn@russianfedora.pro> 56.0.2924.87-2.R
- build with gtk3 support
- disable build of chrome-remote-desktop

* Thu Feb  2 2017 Arkady L. Shane <ashejn@russianfedora.pro> 56.0.2924.87-1.R
- update to 56.0.2924.87
- build third_party/WebKit with -fpermissive

* Thu Jan 26 2017 Arkady L. Shane <ashejn@russianfedora.pro> 56.0.2924.76-1.R
- update to 56.0.2924.76
- fix Russian Translation
- fix build with gcc 4

* Mon Jan 23 2017 Arkady L. Shane <ashejn@russianfedora.pro> 56.0.2924.67-1.R
- update to 56.0.2924.67

- some trouble with system python-jinja2 2.9.4. Use bundled
- fix debugedit: canonicalization unexpectedly shrank by one character

* Mon Jan 16 2017 Arkady L. Shane <ashejn@russianfedora.pro> 56.0.2924.59-1.R
- update to 56.0.2924.59
- update arm-icu-fix patch
- drop chromium-54.0.2840.90-aura-browser-link-to-snapshot.patch
- update translation patch

* Tue Dec 13 2016 Arkady L. Shane <ashejn@russianfedora.pro> 55.0.2883.87-1.R
- update to 55.0.2883.87
- use bundled jinja2 for el7

* Mon Dec  5 2016 Arkady L. Shane <ashejn@russianfedora.pro> 55.0.2883.75-1.R
- update to 55.0.2883.75
- drop gcc5 patch, I think we can do without it
- drop pnacl-fgnu-inline-asm patch
- drop re2 fix patch
- update sandpox-pie patch from openSUSE
- drop cups22 patch
- drop codec-aliases patch
- update addrfix patch
- update icu patch
- drop crrev-415028
- drop harfbuzz patch
- build without nacl
- disable gtk3, some build errors with chrome-remote-desktop
- Fix remoting_perftests build

* Tue Nov 15 2016 Arkady L. Shane <ashejn@russianfedora.pro> 54.0.2840.100-2.R
- enable gtk3 support

* Sat Nov 12 2016 Arkady L. Shane <ashejn@russianfedora.pro> 54.0.2840.100-1.R
- update to 54.0.2840.100

* Sat Nov  5 2016 Tom Callaway <spot@fedoraproject.org> 54.0.2840.90-3.R
- when use_aura is on, chrome/browser needs to link to ui/snapshot

* Sat Nov  5 2016 Arkady L. Shane <ashejn@urussianfedora.pro> 54.0.2840.90-2.1.R
- fix release

* Wed Nov  2 2016 Tom Callaway <spot@fedoraproject.org> 54.0.2840.90-2.R
- export setOpaque in cc_blink
- update to 54.0.2840.90
- debugging disabled
- fixup master_preferences

* Wed Oct 26 2016 Tom Callaway <spot@fedoraproject.org> 54.0.2840.71-2.R
- bump epoch

* Wed Oct 26 2016 Tom Callaway <spot@fedoraproject.org> 54.0.2840.71-1.R
- update to 54.0.2840.71

* Wed Oct 26 2016 Tom Callaway <spot@fedoraproject.org> 54.0.2840.59-2.R
- fix deps

* Thu Oct 13 2016 Tom Callaway <spot@fedoraproject.org> 54.0.2840.59-1.R
- 54.0.2840.59
- use bundled opus, libevent

* Sat Oct  8 2016 Arkady L. Shane <ashejn@russianfedora.pro> 53.0.2785.143-1.1.R
- disable gtk3

* Thu Oct  6 2016 Arkady L. Shane <ashejn@russianfedora.pro> 53.0.2785.143-1.R
- build freeworld version
- do not use system libxml to avoid not opening
  http://base.consultant.ru/cons/cgi/online.cgi?req=doc;base=LAW;n=160129;div=LAW;rnd=0.4700782325977544
- enable gtk3

* Fri Sep 30 2016 Tom Callaway <spot@fedoraproject.org> 53.0.2785.143-1
- 53.0.2785.143

* Tue Sep 20 2016 Tom Callaway <spot@fedoraproject.org> 53.0.2785.116-1
- 53.0.2785.116

* Wed Sep 14 2016 Tom Callaway <spot@fedoraproject.org> 53.0.2785.113-1
- 53.0.2785.113

* Thu Sep  8 2016 Tom Callaway <spot@fedoraproject.org> 53.0.2785.101-1
- 53.0.2785.101
- happy star trek day. live long and prosper.

* Wed Sep  7 2016 Tom Callaway <spot@fedoraproject.org> 53.0.2785.92-1
- add basic framework for gn tooling (disabled because it doesn't work yet)
- update to 53.0.2785.92
- fix HOME environment issue in chrome-remote-desktop service file

* Mon Aug 29 2016 Tom Callaway <spot@fedoraproject.org> 52.0.2743.116-11
- conditionalize Requires: u2f-hidraw-policy so that it is only used on Fedora
- use bundled harfbuzz on EL7

* Thu Aug 18 2016 Tom Callaway <spot@fedoraproject.org> 52.0.2743.116-10
- disable gtk3 because it breaks lots of things
- re-enable hidpi setting

* Tue Aug 16 2016 Tom Callaway <spot@fedoraproject.org> 52.0.2743.116-9
- filter out Requires/Provides for chromium-only libs and plugins

* Tue Aug 16 2016 Tom Callaway <spot@fedoraproject.org> 52.0.2743.116-8
- fix path on Requires(post) line for semanage

* Mon Aug 15 2016 Tom Callaway <spot@fedoraproject.org> 52.0.2743.116-7
- add Requires(post) items for selinux scriptlets

* Mon Aug 15 2016 Tom Callaway <spot@fedoraproject.org> 52.0.2743.116-6
- disable the "hidpi" setting
- unset MADV_FREE if set (should get F25+ working again)

* Fri Aug 12 2016 Tom Callaway <spot@fedoraproject.org> 52.0.2743.116-5
- do not package libwidevinecdm*.so, they are just empty shells
  instead, to enable widevine, get these files from Google Chrome

* Fri Aug 12 2016 Tom Callaway <spot@fedoraproject.org> 52.0.2743.116-4
- add "freeworld" conditional for testing netflix/widevine

* Fri Aug 12 2016 Tom Callaway <spot@fedoraproject.org> 52.0.2743.116-3
- move PepperFlash directory out of the nacl conditional (thanks to churchyard)
- fix widevine (thanks to David Vásquez and UnitedRPMS)

* Wed Aug 10 2016 Tom Callaway <spot@fedoraproject.org> 52.0.2743.116-2
- include clearkeycdm and widevinecdm files in libs-media

* Mon Aug  8 2016 Tom Callaway <spot@fedoraproject.org> 52.0.2743.116-1
- update to 52.0.2743.116

* Thu Aug  4 2016 Tom Callaway <spot@fedoraproject.org> 52.0.2743.82-13
- change libs split to "libs-media", as that actually works.
- add PepperFlash directory (nothing in it though, sorry)

* Wed Aug  3 2016 Tom Callaway <spot@fedoraproject.org> 52.0.2743.82-12
- split out libs package beyond ffmpeg, into libs and libs-content
- fix libusbx conditional for el7 to not nuke libusb headers
- disable speech-dispatcher header prefix setting if not fedora (el7)

* Wed Aug  3 2016 Tom Callaway <spot@fedoraproject.org> 52.0.2743.82-11
- split out chromium-libs-ffmpeg so it can be easily replaced
- conditionalize opus and libusbx for el7

* Wed Aug  3 2016 Tom Callaway <spot@fedoraproject.org> 52.0.2743.82-10
- Add ICU Text Codec aliases (from openSUSE via Russian Fedora)
- Use PIE in the Linux sandbox (from openSUSE via Russian Fedora)
- Enable ARM CPU detection for webrtc (from archlinux via Russian Fedora)
- Do not force -m32 in icu compile on ARM (from archlinux via Russian Fedora)
- Enable gtk3 support (via conditional)
- Enable fpic on linux
- Enable hidpi
- Force aura on
- Enable touch_ui
- Add chromedriver subpackage (from Russian Fedora)
- Set default master_preferences location to /etc/chromium
- Add master_preferences file as config file
- Improve chromium-browser.desktop (from Russian Fedora)

* Thu Jul 28 2016 Tom Callaway <spot@fedoraproject.org> 52.0.2743.82-9
- fix conditional to disable verbose logging output unless beta/dev

* Thu Jul 28 2016 Tom Callaway <spot@fedoraproject.org> 52.0.2743.82-8
- disable nacl/pnacl for Fedora 23 (and older)

* Thu Jul 28 2016 Tom Callaway <spot@fedoraproject.org> 52.0.2743.82-7
- fix post scriptlet so that selinux stuff only happens when selinux is enabled

* Thu Jul 28 2016 Richard Hughes <richard@hughsie.com> 52.0.2743.82-6
- Add an AppData file so that Chromium appears in the software center

* Wed Jul 27 2016 Tom Callaway <spot@fedoraproject.org> 52.0.2743.82-5
- enable nacl/pnacl (chromium-native_client has landed in Fedora)
- fix chromium-browser.sh to report Fedora build target properly

* Wed Jul 27 2016 Tom Callaway <spot@fedoraproject.org> 52.0.2743.82-4
- compile with -fno-delete-null-pointer-checks (fixes v8 crashes, nacl/pnacl)
- turn nacl/pnacl off until chromium-native_client lands in Fedora

* Tue Jul 26 2016 Tom Callaway <spot@fedoraproject.org> 52.0.2743.82-3
- turn nacl back on for x86_64

* Thu Jul 21 2016 Tom Callaway <spot@fedoraproject.org> 52.0.2743.82-2
- fix cups 2.2 support
- try to enable widevine compatibility (you still need to get the binary .so files from chrome)

* Thu Jul 21 2016 Tom Callaway <spot@fedoraproject.org> 52.0.2743.82-1
- update to 52.0.2743.82
- handle locales properly
- cleanup spec

* Tue Jul 19 2016 Tom Callaway <spot@fedoraproject.org> 52.0.2743.75-1
- update to 52.0.2743.75

* Wed Jul 6 2016 Tom Callaway <spot@fedoraproject.org> 52.0.2743.60-1
- bump to 52.0.2743.60, disable nacl for now

* Mon May 9 2016 Tom Callaway <spot@fedoraproject.org> 52.0.2723.2-1
- force to dev to see if it works better on F24+

* Wed May 4 2016 Tom Callaway <spot@fedoraproject.org> 50.0.2661.94-6
- apply upstream fix for https://bugs.chromium.org/p/chromium/issues/detail?id=604534

* Tue May 3 2016 Tom Callaway <spot@fedoraproject.org> 50.0.2661.94-5
- use bundled re2 (conditionalize it)

* Tue May 3 2016 Tom Callaway <spot@fedoraproject.org> 50.0.2661.94-4
- disable asan (it never quite built)
- do not preserve re2 bundled tree, causes header/library mismatch

* Mon May 2 2016 Tom Callaway <spot@fedoraproject.org> 50.0.2661.94-3
- enable AddressSanize (ASan) for debugging

* Sat Apr 30 2016 Tom Callaway <spot@fedoraproject.org> 50.0.2661.94-2
- use bundled icu always. *sigh*

* Fri Apr 29 2016 Tom Callaway <spot@fedoraproject.org> 50.0.2661.94-1
- update to 50.0.2661.94

* Wed Apr 27 2016 Tom Callaway <spot@fedoraproject.org> 50.0.2661.86-1
- update to 50.0.2661.86

* Thu Mar 17 2016 Tom Callaway <spot@fedoraproject.org> 49.0.2623.87-4
- protect third_party/woff2

* Thu Mar 17 2016 Tom Callaway <spot@fedoraproject.org> 49.0.2623.87-3
- add BuildRequires: libffi-devel

* Thu Mar 17 2016 Tom Callaway <spot@fedoraproject.org> 49.0.2623.87-2
- explicitly disable sysroot

* Thu Mar 17 2016 Tom Callaway <spot@fedoraproject.org> 49.0.2623.87-1
- update to 49.0.2623.87

* Mon Feb 29 2016 Tom Callaway <spot@fedoraproject.org> 48.0.2564.116-3
- Happy Leap Day!
- add Requires: u2f-hidraw-policy for u2f token support
- add Requires: xorg-x11-server-Xvfb for chrome-remote-desktop

* Fri Feb 26 2016 Tom Callaway <spot@fedoraproject.org> 48.0.2564.116-2
- fix icu BR

* Wed Feb 24 2016 Tom Callaway <spot@fedoraproject.org> 48.0.2564.116-1
- Update to 48.0.2564.116
- conditionalize icu properly
- fix libusbx handling (bz1270324)

* Wed Feb 17 2016 Tom Callaway <spot@fedoraproject.org> 48.0.2564.103-2
- fixes for gcc6

* Mon Feb  8 2016 Tom Callaway <spot@fedoraproject.org> 48.0.2564.103-1
- update to 48.0.2564.103
- use bundled libsrtp (because upstream has coded themselves into an ugly corner)

* Fri Jan 22 2016 Tom Callaway <spot@fedoraproject.org> 48.0.2564.82-1
- update to 48.0.2564.82

* Fri Jan 15 2016 Tom Callaway <spot@fedoraproject.org> 47.0.2526.111-1
- update to 47.0.2526.111

* Thu Jan 07 2016 Tomas Popela <tpopela@redhat.com> 47.0.2526.106-2
- compare hashes when downloading the tarballs
- Google started to include the Debian sysroots in tarballs - remove them while
  processing the tarball
- add a way to not use the system display server for tests instead of Xvfb
- update the depot_tools checkout to get some GN fixes
- use the remove_bundled_libraries script
- update the clean_ffmpeg script to print errors when some files that we are
  processing are missing
- update the clean_ffmpeg script to operate on tarball's toplevel folder
- don't show comments as removed tests in get_linux_tests_names script
- rework the process_ffmpeg_gyp script (also rename it to
  get_free_ffmpeg_source_files) to use the GN files insted of GYP (but we still
  didn't switched to GN build)

* Wed Dec 16 2015 Tom Callaway <spot@fedoraproject.org> 47.0.2526.106-1
- update to 47.0.2526.106

* Tue Dec 15 2015 Tom Callaway <spot@fedoraproject.org> 47.0.2526.80-4
- entirely patch out the broken fd counter from the nacl loader code
  killing it with fire would be better, but then chromium is on fire
  and that somehow makes it worse.

* Mon Dec 14 2015 Tom Callaway <spot@fedoraproject.org> 47.0.2526.80-3
- revert nacl fd patch (now we see 6 fds! 6 LIGHTS!)

* Fri Dec 11 2015 Tom Callaway <spot@fedoraproject.org> 47.0.2526.80-2
- build everything shared, but when we do shared builds, make -libs subpackage
- make chrome-remote-desktop dep on -libs subpackage in shared builds

* Wed Dec  9 2015 Tom Callaway <spot@fedoraproject.org> 47.0.2526.80-1
- update to 47.0.2526.80
- only build ffmpeg shared, not any other libs
  this is because if we build the other libs shared, then our
  chrome-remote-desktop build deps on those libs and we do not want that

* Tue Dec  8 2015 Tom Callaway <spot@fedoraproject.org> 47.0.2526.73-2
- The nacl loader claims it sees 7 fds open ALL THE TIME, and fails
  So, we tell it that it is supposed to see 7.
  I suspect building with shared objects is causing this disconnect.

* Wed Dec  2 2015 Tom Callaway <spot@fedoraproject.org> 47.0.2526.73-1
- update to 47.0.2526.73
- rework chrome-remote-desktop subpackage to work for google-chrome and chromium

* Wed Dec  2 2015 Tomas Popela <tpopela@redhat.com> 47.0.2526.69-1
- Update to 47.0.2526.69

* Tue Dec  1 2015 Tom Callaway <spot@fedoraproject.org> 46.0.2490.86-4
- still more remote desktop changes

* Mon Nov 30 2015 Tom Callaway <spot@fedoraproject.org> 46.0.2490.86-3
- lots of remote desktop cleanups

* Thu Nov 12 2015 Tom Callaway <spot@fedoraproject.org> 46.0.2490.86-2
- re-enable Requires/BuildRequires for libusbx
- add remote-desktop subpackage

* Wed Nov 11 2015 Tomas Popela <tpopela@redhat.com> 46.0.2490.86-1
- update to 46.0.2490.86
- clean the SPEC file
- add support for policies: https://www.chromium.org/administrators/linux-quick-start
- replace exec_mem_t SELinux label with bin_t - see rhbz#1281437
- refresh scripts that are used for processing the original tarball

* Fri Oct 30 2015 Tom Callaway <spot@fedoraproject.org> 46.0.2490.80-5
- tls_edit is a nacl thing. who knew?

* Thu Oct 29 2015 Tom Callaway <spot@fedoraproject.org> 46.0.2490.80-4
- more nacl fixups for i686 case

* Thu Oct 29 2015 Tom Callaway <spot@fedoraproject.org> 46.0.2490.80-3
- conditionalize nacl/nonacl, disable nacl on i686, build for i686

* Mon Oct 26 2015 Tom Callaway <spot@fedoraproject.org> 46.0.2490.80-2
- conditionalize shared bits (enable by default)

* Fri Oct 23 2015 Tom Callaway <spot@fedoraproject.org> 46.0.2490.80-1
- update to 46.0.2490.80

* Thu Oct 15 2015 Tom Callaway <spot@fedoraproject.org> 46.0.2490.71-1
- update to 46.0.2490.71

* Thu Oct 15 2015 Tom Callaway <spot@fedoraproject.org> 45.0.2454.101-2
- fix icu handling for f21 and older

* Mon Oct  5 2015 Tom Callaway <spot@fedoraproject.org> 45.0.2454.101-1
- update to 45.0.2454.101

* Thu Jun 11 2015 Tom Callaway <spot@fedoraproject.org> 43.0.2357.124-1
- update to 43.0.2357.124

* Tue Jun  2 2015 Tom Callaway <spot@fedoraproject.org> 43.0.2357.81-1
- update to 43.0.2357.81

* Thu Feb 26 2015 Tom Callaway <spot@fedoraproject.org> 40.0.2214.115-1
- update to 40.0.2214.115

* Thu Feb 19 2015 Tom Callaway <spot@fedoraproject.org> 40.0.2214.111-1
- update to 40.0.2214.111

* Mon Feb  2 2015 Tom Callaway <spot@fedoraproject.org> 40.0.2214.94-1
- update to 40.0.2214.94

* Tue Jan 27 2015 Tom Callaway <spot@fedoraproject.org> 40.0.2214.93-1
- update to 40.0.2214.93

* Sat Jan 24 2015 Tom Callaway <spot@fedoraproject.org> 40.0.2214.91-1
- update to 40.0.2214.91

* Wed Jan 21 2015 Tom Callaway <spot@fedoraproject.org> 39.0.2171.95-3
- use bundled icu on Fedora < 21, we need 5.2

* Tue Jan  6 2015 Tom Callaway <spot@fedoraproject.org> 39.0.2171.95-2
- rebase off Tomas's spec file for Fedora

* Fri Dec 12 2014 Tomas Popela <tpopela@redhat.com> 39.0.2171.95-1
- Update to 39.0.2171.95
- Resolves: rhbz#1173448

* Wed Nov 26 2014 Tomas Popela <tpopela@redhat.com> 39.0.2171.71-1
- Update to 39.0.2171.71
- Resolves: rhbz#1168128

* Wed Nov 19 2014 Tomas Popela <tpopela@redhat.com> 39.0.2171.65-2
- Revert the chrome-sandbox rename to chrome_sandbox
- Resolves: rhbz#1165653

* Wed Nov 19 2014 Tomas Popela <tpopela@redhat.com> 39.0.2171.65-1
- Update to 39.0.2171.65
- Use Red Hat Developer Toolset for compilation
- Set additional SELinux labels
- Add more unit tests
- Resolves: rhbz#1165653

* Fri Nov 14 2014 Tomas Popela <tpopela@redhat.com> 38.0.2125.122-1
- Update to 38.0.2125.122
- Resolves: rhbz#1164116

* Wed Oct 29 2014 Tomas Popela <tpopela@redhat.com> 38.0.2125.111-1
- Update to 38.0.2125.111
- Resolves: rhbz#1158347

* Fri Oct 24 2014 Tomas Popela <tpopela@redhat.com> 38.0.2125.104-2
- Fix the situation when the return key (and keys from numpad) does not work
  in HTML elements with input
- Resolves: rhbz#1153988
- Dynamically determine the presence of the PepperFlash plugin
- Resolves: rhbz#1154118

* Thu Oct 16 2014 Tomas Popela <tpopela@redhat.com> 38.0.2125.104-1
- Update to 38.0.2125.104
- Resolves: rhbz#1153012

* Thu Oct 09 2014 Tomas Popela <tpopela@redhat.com> 38.0.2125.101-2
- The boringssl is used for tests, without the possibility of using
  the system openssl instead. Remove the openssl and boringssl sources
  when not building the tests.
- Resolves: rhbz#1004948

* Wed Oct 08 2014 Tomas Popela <tpopela@redhat.com> 38.0.2125.101-1
- Update to 38.0.2125.101
- System openssl is used for tests, otherwise the bundled boringssl is used
- Don't build with clang
- Resolves: rhbz#1004948

* Wed Sep 10 2014 Tomas Popela <tpopela@redhat.com> 37.0.2062.120-1
- Update to 37.0.2062.120
- Resolves: rhbz#1004948

* Wed Aug 27 2014 Tomas Popela <tpopela@redhat.com> 37.0.2062.94-1
- Update to 37.0.2062.94
- Include the pdf viewer library

* Wed Aug 13 2014 Tomas Popela <tpopela@redhat.com> 36.0.1985.143-1
- Update to 36.0.1985.143
- Use system openssl instead of bundled one
- Resolves: rhbz#1004948

* Thu Jul 17 2014 Tomas Popela <tpopela@redhat.com> 36.0.1985.125-1
- Update to 36.0.1985.125
- Add libexif as BR
- Resolves: rhbz#1004948

* Wed Jun 11 2014 Tomas Popela <tpopela@redhat.com> 35.0.1916.153-1
- Update to 35.0.1916.153
- Resolves: rhbz#1004948

* Wed May 21 2014 Tomas Popela <tpopela@redhat.com> 35.0.1916.114-1
- Update to 35.0.1916.114
- Bundle python-argparse
- Resolves: rhbz#1004948

* Wed May 14 2014 Tomas Popela <tpopela@redhat.com> 34.0.1847.137-1
- Update to 34.0.1847.137
- Resolves: rhbz#1004948

* Mon May 5 2014 Tomas Popela <tpopela@redhat.com> 34.0.1847.132-1
- Update to 34.0.1847.132
- Bundle depot_tools and switch from make to ninja
- Remove PepperFlash
- Resolves: rhbz#1004948

* Mon Feb 3 2014 Tomas Popela <tpopela@redhat.com> 32.0.1700.102-1
- Update to 32.0.1700.102

* Thu Jan 16 2014 Tomas Popela <tpopela@redhat.com> 32.0.1700.77-1
- Update to 32.0.1700.77
- Properly kill Xvfb when tests fails
- Add libdrm as BR
- Add libcap as BR

* Tue Jan 7 2014 Tomas Popela <tpopela@redhat.com> 31.0.1650.67-2
- Minor changes in spec files and scripts
- Add Xvfb as BR for tests
- Add policycoreutils-python as Requires
- Compile unittests and run them in chech phase, but turn them off by default
  as many of them are failing in Brew

* Thu Dec 5 2013 Tomas Popela <tpopela@redhat.com> 31.0.1650.67-1
- Update to 31.0.1650.63

* Thu Nov 21 2013 Tomas Popela <tpopela@redhat.com> 31.0.1650.57-1
- Update to 31.0.1650.57

* Wed Nov 13 2013 Tomas Popela <tpopela@redhat.com> 31.0.1650.48-1
- Update to 31.0.1650.48
- Minimal supported RHEL6 version is now RHEL 6.5 due to GTK+

* Fri Oct 25 2013 Tomas Popela <tpopela@redhat.com> 30.0.1599.114-1
- Update to 30.0.1599.114
- Hide the infobar with warning that this version of OS is not supported
- Polished the chromium-latest.py

* Thu Oct 17 2013 Tomas Popela <tpopela@redhat.com> 30.0.1599.101-1
- Update to 30.0.1599.101
- Minor changes in scripts

* Wed Oct 2 2013 Tomas Popela <tpopela@redhat.com> 30.0.1599.66-1
- Update to 30.0.1599.66
- Automated the script for cleaning the proprietary sources from ffmpeg.

* Thu Sep 19 2013 Tomas Popela <tpopela@redhat.com> 29.0.1547.76-1
- Update to 29.0.1547.76
- Added script for removing the proprietary sources from ffmpeg. This script is called during cleaning phase of ./chromium-latest --rhel

* Mon Sep 16 2013 Tomas Popela <tpopela@redhat.com> 29.0.1547.65-2
- Compile with Dproprietary_codecs=0 and Dffmpeg_branding=Chromium to disable proprietary codecs (i.e. MP3)

* Mon Sep 9 2013 Tomas Popela <tpopela@redhat.com> 29.0.1547.65-1
- Initial version based on Tom Callaway's <spot@fedoraproject.org> work

