# This spec file is based on other spec files, ebuilds, PKGBUILDs available from
#  [1] https://repos.fedorapeople.org/repos/spot/chromium/
#  [2] https://copr.fedoraproject.org/coprs/churchyard/chromium-russianfedora-tested/
#  [3] https://www.archlinux.org/packages/extra/x86_64/chromium/
#  [4] https://src.fedoraproject.org/rpms/chromium/
#  [5] https://gitweb.gentoo.org/repo/gentoo.git/tree/www-client/chromium/

# Get the version number of latest stable version
# $ curl -s 'https://omahaproxy.appspot.com/all?os=linux&channel=stable' | sed 1d | cut -d , -f 3
######################################################################################################################
####################################################################################################
#Global Libraries
#Do not turn it on in Fedora copr!
%global freeworld 1
### Google API keys (see http://www.chromium.org/developers/how-tos/api-keys)
### Note: These are for Fedora use ONLY.
### For your own distribution, please get your own set of keys.
### http://lists.debian.org/debian-legal/2013/11/msg00006.html
%global api_key AIzaSyDUIXvzVrt5OkVsgXhQ6NFfvWlA44by-aw
%global default_client_id 449907151817.apps.googleusercontent.com
%global default_client_secret miEreAep8nuvTdvLums6qyLK
%global chromiumdir %{_libdir}/chromium-browser
%global __provides_exclude_from %{chromium_path}/.*\\.so|%{chromium_path}/lib/.*\\.so
%global __provides_exclude_from %{chromium_path}/.*\\.so|%{chromium_path}/lib/.*\\.so
%global privlibs libaccessibility|libaura_extra|libaura|libbase_i18n|libbase|libblink_common|libblink_core|libblink_modules|libblink_platform|libblink_web|libbluetooth|libboringssl|libbrowser_ui_views|libcaptive_portal|libcapture|libcc_blink|libcc_ipc|libcc_proto|libcc|libcc_surfaces|libchromium_sqlite3|libcloud_policy_proto_generated_compile|libcloud_policy_proto|libcommon|libcompositor|libcontent|libcrcrypto|libdbus|libdevice_battery|libdevice_core|libdevice_event_log|libdevice_gamepad|libdevice_geolocation|libdevices|libdevice_vibration|libdisplay_compositor|libdisplay|libdisplay_types|libdisplay_util|libdomain_reliability|libEGL|libevents_base|libevents_devices_x11|libevents_ipc|libevents_ozone_layout|libevents|libevents_x|libffmpeg|libfont_service_library|libgcm|libgeometry|libgesture_detection|libgfx_ipc_color|libgfx_ipc_geometry|libgfx_ipc_skia|libgfx_ipc|libgfx|libgfx_x11|libgin|libgles2_c_lib|libgles2_implementation|libgles2_utils|libGLESv2|libgl_init|libgl_wrapper|libgpu|libgtk2ui|libicui18n|libicuuc|libipc|libkeyboard|libkeyboard_with_content|libkeycodes_x11|libkeyed_service_content|libkeyed_service_core|libmedia_blink|libmedia_gpu|libmedia|libmemory_coordinator_browser|libmemory_coordinator_child|libmemory_coordinator_common|libmessage_center|libmidi|libmojo_blink_lib|libmojo_common_lib|libmojo_ime_lib|libmojo_public_system|libmojo_system_impl|libnative_theme|libnet|libnet_with_v8|libonc|libplatform|libpolicy_component|libpolicy_proto|libpower_save_blocker|libppapi_host|libppapi_proxy|libppapi_shared|libprefs|libprinting|libprotobuf_lite|libproxy_config|librange|libsandbox_services|libseccomp_bpf|libsessions|libshared_memory_support|libshell_dialogs|libskia|libsnapshot|libsql|libstartup_tracing|libstorage_browser|libstorage_common|libstub_window|libsuid_sandbox_client|libsurface|libtracing|libtranslator|libui_base_ime|libui_base|libui_base_x|libui_data_pack|libui_library|libui_touch_selection|libui_views_mus_lib|liburl_ipc|liburl_matcher|liburl|libuser_prefs|libv8|libviews|libwebdata_common|libweb_dialogs|libwebview|libwidevinecdm|libwm|libwtf|libx11_events_platform|libx11_window|libbindings|libgeolocation|libmojo_public_system_cpp|libtime_zone_monitor|libdevice_base|libcc_animation|libcpp|libdevice_base|libdiscardable_memory_client|libdiscardable_memory_common|libdiscardable_memory_service|libgeneric_sensor|libgl_in_process_context|libjs|libpower_monitor|libv8_libbase|libsensors|libdevice_vr|libcc_paint|libgtk3ui|libcapture_base|libcapture_lib|libfingerprint|libanimation|libcc_base|libcc_debug|libcodec|libcolor_space|libembedder|libgeometry_skia|libgin_features|libmedia_mojo_services|libplatform_wtf|libprotobuf_globals|libcdm_manager|libframe_sinks|libresource_coordinator_cpp|libblink_android_mojo_bindings_shared|libblink_mojo_bindings_shared|libblink_mojo_bindings_shared|libblink_offscreen_canvas_mojo_bindings_shared|libcontent_common_mojo_bindings_shared|libdevice_vr_mojo_bindings|libdevice_vr_mojo_bindings_blink|libdevice_vr_mojo_bindings_shared|libgeneric_sensor_public_interfaces_shared|libheadless|libipc_mojom|libipc_mojom_shared|libpublic|libresource_coordinator_public_interfaces_internal_shared|libservice_manager_cpp|libservice_manager_cpp_types|libservice_manager_mojom|libservice_manager_mojom_constants|libservice_manager_mojom_constants_shared|libservice_manager_mojom_shared|libgfx_switches|libmetrics_cpp|libui_devtools|libviz_common|libwm_public|libblink_controller|libcontent_public_common_mojo_bindings_shared|libgfx_switches|libhost|libinterfaces_shared|libmetrics_cpp|libservice|libviz_common|libwm_public|libviz_resource_format|libembedder_switches|libfreetype_harfbuzz|libmessage_support|libsandbox|libclient|libleveldatabase|libblink_core_mojo_bindings_shared|libgpu_util|libmedia_devices_mojo_bindings_shared|libmojo_platform_bindings_shared|libmojo_bindings_shared|libcbor|libcrash_key|libdevice_features|libgfx_ipc_buffer_types|libgles2|libgpu_ipc_service|libmojo_base_lib|libmojo_base_mojom_shared|libmojo_base_shared_typemap_traits|libnetwork_session_configurator|libresource_coordinator_cpp_base|libresource_coordinator_public_interfaces|libresource_coordinator_public_interfaces_blink|libresource_coordinator_public_interfaces_shared
%global __requires_exclude ^(%{privlibs})\\.so
########################################################################################################################
%if 0%{?fedora} < 26
%bcond_without system_jinja2
%else
%bcond_with system_jinja2
%endif

# https://github.com/dabeaz/ply/issues/66
%if 0%{?fedora} >= 24
%bcond_without system_ply
%else
%bcond_with system_ply
%endif

# Require libxml2 > 2.9.4 for XML_PARSE_NOXXE
%if 0%{?fedora} >= 27
%bcond_without system_libxml2
%else
%bcond_with system_libxml2
%endif

# Require harfbuzz >= 1.5.0 for hb_glyph_info_t
%if 0%{?fedora} >= 28
%bcond_without system_harfbuzz
%else
%bcond_with system_harfbuzz
%endif

# Allow testing whether icu can be unbundled
%bcond_with system_libicu

# Allow testing whether libvpx can be unbundled
%bcond_with system_libvpx

# Allow building with symbols to ease debugging
# Enabled by default because Fedora Copr has enough memory
#Disabled by default in OBS because it has less memory
%bcond_without symbol

# Allow compiling with clang
# Disabled by default becaue gcc is the system compiler
%bcond_with clang

# Allow disabling unconditional build dependency on clang
# Enabled by default because nacl always uses clang to compile some files
%bcond_without require_clang

# Allow using compilation flags set by Fedora RPM macros
# Disabled by default because it causes out-of-memory error on Fedora Copr
%bcond_with fedora_compilation_flags

Name:       chromium
Version:    65.0.3325.181
Release:    101%{?dist}.chromium_vaapi
Summary:    A WebKit (Blink) powered web browser with video acceleration

License:    BSD and LGPLv2+ and ASL 2.0 and IJG and MIT and GPLv2+ and ISC and OpenSSL and (MPLv1.1 or GPLv2 or LGPLv2)
URL:        https://www.chromium.org/Home

# Unfortunately, Fedora Copr forbids uploading sources with patent-encumbered
# ffmpeg code even if they are never compiled and linked to target binraies,
# so we must repackage upstream tarballs to satisfy this requirement. However,
# we cannot simply delete all code of ffmpeg because this will disable support
# for some commonly-used free codecs such as Ogg Theora. Instead, helper
# scripts included in official Fedora packages are copied, modified, and used
# to automate the repackaging work.
#
# If you don't use Fedora services, you can uncomment the following line and
# use the upstream source tarball instead of the repackaged one.
#
# The repackaged source tarball used here is produced by:
# ./chromium-latest.py --stable --ffmpegclean --ffmpegarm
%if %{freeworld}
Source0:    https://commondatastorage.googleapis.com/chromium-browser-official/chromium-%{version}.tar.xz
%else
Source0:    chromium-%{version}-clean.tar.xz
%endif
Source1:    chromium-latest.py
Source2:    chromium-ffmpeg-clean.sh
Source3:    chromium-ffmpeg-free-sources.py

# The following two source files are copied and modified from
# https://repos.fedorapeople.org/repos/spot/chromium/
Source10:   chromium-browser.sh
Source11:   chromium-browser.desktop

# The following two source files are copied verbatim from
# https://src.fedoraproject.org/cgit/rpms/chromium.git/tree/
Source12:   chromium-browser.xml
Source13:   chromium-browser.appdata.xml

# Add a patch from Fedora to fix GN build
# https://src.fedoraproject.org/cgit/rpms/chromium.git/commit/?id=0df9641
Patch1:    commit.patch

# Add a patch from Gentoo to fix ANGLE build
# https://gitweb.gentoo.org/repo/gentoo.git/commit/?id=1a8dd9f
#Patch2:    angle.patch
#Gcc patches from gentoo
Patch8:		gcc71.patch
Patch9:		gcc72.patch
Patch10:	gcc73.patch
Patch11:	gcc74.patch
Patch12:	gcc75.patch
Patch13:	gcc76.patch
Patch14:	gcc77.patch
Patch15:	gcc78.patch
Patch16:	gcc79.patch
Patch17:	gcc710.patch
Patch18:	gcc711.patch
Patch19:	gcc712.patch
Patch20:	gcc713.patch
Patch21:	gcc714.patch
Patch22:	gcc715.patch


# Add a patch from Gentoo to fix compositor build
# https://gitweb.gentoo.org/repo/gentoo.git/commit/?id=9b71cea
# https://gitweb.gentoo.org/repo/gentoo.git/commit/?id=2ad380a
#Patch3:    memcpy.patch
Patch4:    math.patch
Patch5:    stdin.patch
#Vaapi Patches from inox-patchset
#Patch4:    move.patch
#Patch5:    init.patch
#Patch6:    2ndstep.patch
#Patch7:    rgbx.patch
Patch6:    init.patch
Patch7:    vaapi.patch

ExclusiveArch: x86_64 

# Make sure we don't encounter GCC 5.1 bug
%if 0%{?fedora} >= 22
BuildRequires: gcc >= 5.1.1-2
%endif
# Chromium 54 requires clang to enable nacl support
# Chromium 59 requires llvm-ar to enable nacl support
%if %{with clang} || %{with require_clang}
BuildRequires: clang, llvm
%endif
# Basic tools and libraries
BuildRequires: ninja-build, nodejs, bison, gperf, hwdata
BuildRequires: libgcc, glibc, libatomic
BuildRequires: libcap-devel, cups-devel, minizip-devel, alsa-lib-devel
BuildRequires: mesa-libGL-devel, mesa-libEGL-devel
BuildRequires: pkgconfig(gtk+-2.0), pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(libexif), pkgconfig(nss)
BuildRequires: pkgconfig(xtst), pkgconfig(xscrnsaver)
BuildRequires: pkgconfig(dbus-1), pkgconfig(libudev)
BuildRequires: pkgconfig(gnome-keyring-1)
BuildRequires: pkgconfig(libffi)
# remove_bundled_libraries.py --do-remove
BuildRequires: python2-rpm-macros
BuildRequires: python-beautifulsoup4
BuildRequires: python-html5lib
%if %{with system_jinja2}
%if 0%{?fedora} >= 24
BuildRequires: python2-jinja2
%else
BuildRequires: python-jinja2
%endif
%endif
%if 0%{?fedora} >= 26
BuildRequires: python2-markupsafe
%else
BuildRequires: python-markupsafe
%endif
%if %{with system_ply}
BuildRequires: python2-ply
%endif
# replace_gn_files.py --system-libraries
BuildRequires: flac-devel
BuildRequires: freetype-devel
%if %{with system_harfbuzz}
BuildRequires: harfbuzz-devel
%endif
%if %{with system_libicu}
BuildRequires: libicu-devel
%endif
BuildRequires: libdrm-devel
BuildRequires: libjpeg-turbo-devel
BuildRequires: libpng-devel
# Chromium requires libvpx 1.5.0 and some non-default options
%if %{with system_libvpx}
BuildRequires: libvpx-devel
%endif
BuildRequires: libwebp-devel
%if %{with system_libxml2}
BuildRequires: pkgconfig(libxml-2.0)
%endif
BuildRequires: pkgconfig(libxslt)
BuildRequires: opus-devel
BuildRequires: re2-devel
BuildRequires: snappy-devel
BuildRequires: yasm
BuildRequires: zlib-devel
# use_*
BuildRequires: pciutils-devel
BuildRequires: speech-dispatcher-devel
BuildRequires: pulseaudio-libs-devel
# install desktop files
BuildRequires: desktop-file-utils
# install AppData files
BuildRequires: libappstream-glib
#for vaapi
BuildRequires:	libva-devel
Requires(post):   desktop-file-utils
Requires(postun): desktop-file-utils
Requires:         hicolor-icon-theme
Requires:	libva
Obsoletes:     chromedriver <= %{version}-%{release}
Obsoletes:     chromium-common <= %{version}-%{release}
Obsoletes:     chromium-headless <= %{version}-%{release}
Obsoletes:     chromium-libs <= %{version}-%{release}
Obsoletes:     chromium-libs-media <= %{version}-%{release}
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
Provides: bundled(libGLESv2.so()(64bit))
Provides: bundled(expat) = 2.2.0
Provides: bundled(fdmlibm) = 5.3
# Don't get too excited. MPEG and other legally problematic stuff is stripped out.
Provides: bundled(ffmpeg) = 3.2git
Provides: bundled(fips181) = 2.2.3
Provides: bundled(fontconfig) = 2.11.0
Provides: bundled(gperftools) = svn144
Provides: bundled(harfbuzz) = 1.4.2
Provides: bundled(hunspell) = 1.6.0
Provides: bundled(iccjpeg)
Provides: bundled(icu) = 58.1
Provides: bundled(kitchensink) = 1
Provides: bundled(leveldb) = 1.20
Provides: bundled(libaddressinput) = 0
Provides: bundled(libdrm) = 2.4.70
Provides: bundled(libevent) = 1.4.15
Provides: bundled(libjingle) = 9564
Provides: bundled(libjpeg-turbo) = 1.4.90
Provides: bundled(libphonenumber) = a4da30df63a097d67e3c429ead6790ad91d36cf4
Provides: bundled(libpng) = 1.6.22
Provides: bundled(libsrtp) = 1.5.2
Provides: bundled(libusbx) = 1.0.17
Provides: bundled(libvpx) = 1.6.0
Provides: bundled(libwebp) = 0.6.0
# Well, it's actually newer than 2.9.4 and has code in it that has been reverted upstream... but eh.
Provides: bundled(libxml) = 2.9.4
Provides: bundled(libXNVCtrl) = 302.17
Provides: bundled(libyuv) = 1651
Provides: bundled(lzma) = 15.14
Provides: bundled(libudis86) = 1.7.1
Provides: bundled(mesa) = 9.0.3
Provides: bundled(NSBezierPath) = 1.0
Provides: bundled(mozc)
Provides: bundled(mt19937ar) = 2002.1.26
Provides: bundled(opus) = 1.1.3
Provides: bundled(ots) = 8d70cffebbfa58f67a5c3ed0e9bc84dccdbc5bc0
Provides: bundled(protobuf) = 3.0.0.beta.3
Provides: bundled(qcms) = 4
Provides: bundled(re2)
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
Provides:	chromium-ffmpegsumo = %{version}-%{release}
Obsoletes:	chromium-ffmpegsumo <= 35.0.1916.114
Provides:	chromium-v8 = %{version}-%{release}
Obsoletes:	chromium-v8 <= 3.25.28.18
# This is a lie. webrtc never had any real version. 0.2 is greater than 0.1
Provides:	webrtc = 0.2
Obsoletes:	webrtc <= 0.1
Provides:      chromedriver = %{version}-%{release}
Provides:      chromium-common = %{version}-%{release}
Provides:      chromium-headless = %{version}-%{release}
Provides:      chromium-libs = %{version}-%{release}
Provides:      chromium-libs-media = %{version}-%{release}

Provides:      chromedriver-stable = %{version}-%{release}
Conflicts:     chromedriver-testing
Conflicts:     chromedriver-unstable


%description
Chromium is an open-source web browser, powered by WebKit (Blink).
###########################################################################################################################
%prep
%autosetup -p1

./build/linux/unbundle/remove_bundled_libraries.py --do-remove \
    base/third_party/dmg_fp \
    base/third_party/dynamic_annotations \
    base/third_party/icu \
    base/third_party/libevent \
    base/third_party/nspr \
    base/third_party/superfasthash \
    base/third_party/symbolize \
    base/third_party/valgrind \
    base/third_party/xdg_mime \
    base/third_party/xdg_user_dirs \
    chrome/third_party/mozilla_security_manager \
    courgette/third_party \
    native_client/src/third_party/dlmalloc \
    native_client/src/third_party/valgrind \
    net/third_party/mozilla_security_manager \
    net/third_party/nss \
    third_party/adobe \
    third_party/analytics \
    third_party/angle \
    third_party/angle/src/common/third_party/base \
    third_party/angle/src/common/third_party/smhasher \
    third_party/angle/src/third_party/compiler \
    third_party/angle/src/third_party/libXNVCtrl \
    third_party/angle/src/third_party/trace_event \
    third_party/boringssl \
    third_party/boringssl/src/third_party/fiat \
    third_party/blink \
    third_party/breakpad \
    third_party/breakpad/breakpad/src/third_party/curl \
    third_party/brotli \
    third_party/cacheinvalidation \
    third_party/catapult \
    third_party/catapult/common/py_vulcanize/third_party/rcssmin \
    third_party/catapult/common/py_vulcanize/third_party/rjsmin \
    third_party/catapult/third_party/polymer \
    third_party/catapult/tracing/third_party/d3 \
    third_party/catapult/tracing/third_party/gl-matrix \
    third_party/catapult/tracing/third_party/jszip \
    third_party/catapult/tracing/third_party/mannwhitneyu \
    third_party/catapult/tracing/third_party/oboe \
    third_party/catapult/tracing/third_party/pako \
    third_party/ced \
    third_party/cld_3 \
    third_party/crc32c \
    third_party/cros_system_api \
    third_party/devscripts \
    third_party/dom_distiller_js \
    third_party/ffmpeg \
    third_party/fips181 \
    third_party/flatbuffers \
    third_party/flot \
    third_party/freetype \
    third_party/glslang-angle \
    third_party/google_input_tools \
    third_party/google_input_tools/third_party/closure_library \
    third_party/google_input_tools/third_party/closure_library/third_party/closure \
    third_party/googletest \
%if !%{with system_harfbuzz}
    third_party/harfbuzz-ng \
%endif
    third_party/hunspell \
    third_party/iccjpeg \
%if !%{with system_libicu}
    third_party/icu \
%endif
    third_party/inspector_protocol \
%if !%{with system_jinja2}
    third_party/jinja2 \
%endif
    third_party/jstemplate \
    third_party/khronos \
    third_party/leveldatabase \
    third_party/libaddressinput \
    third_party/libaom \
    third_party/libjingle \
    third_party/libphonenumber \
    third_party/libsecret \
    third_party/libsrtp \
    third_party/libudev \
%if !%{with system_libvpx}
    third_party/libvpx \
    third_party/libvpx/source/libvpx/third_party/x86inc \
%endif
    third_party/libwebm \
%if %{with system_libxml2}
    third_party/libxml/chromium \
%else
    third_party/libxml \
%endif
    third_party/libXNVCtrl \
    third_party/libyuv \
    third_party/lss \
    third_party/lzma_sdk \
    third_party/mesa \
    third_party/metrics_proto \
    third_party/modp_b64 \
    third_party/mt19937ar \
    third_party/node \
    third_party/node/node_modules/polymer-bundler/lib/third_party/UglifyJS2 \
    %if %{freeworld}
    third_party/openh264 \
    %endif
    third_party/openmax_dl \
    third_party/ots \
    third_party/pdfium \
    third_party/pdfium/third_party/agg23 \
    third_party/pdfium/third_party/base \
    third_party/pdfium/third_party/bigint \
    third_party/pdfium/third_party/build \
    third_party/pdfium/third_party/freetype \
    third_party/pdfium/third_party/lcms \
    third_party/pdfium/third_party/libopenjpeg20 \
    third_party/pdfium/third_party/libpng16 \
    third_party/pdfium/third_party/libtiff \
%if !%{with system_ply}
    third_party/ply \
%endif
    third_party/polymer \
    third_party/protobuf \
    third_party/protobuf/third_party/six \
    third_party/qcms \
    third_party/s2cellid \
    third_party/sfntly \
    third_party/skia \
    third_party/skia/third_party/gif \
    third_party/skia/third_party/vulkan \
    third_party/smhasher \
    third_party/speech-dispatcher \
    third_party/spirv-headers \
    third_party/spirv-tools-angle \
    third_party/sqlite \
    third_party/swiftshader \
    third_party/swiftshader/third_party/llvm-subzero \
    third_party/swiftshader/third_party/subzero \
    third_party/tcmalloc \
    third_party/usb_ids \
    third_party/usrsctp \
    third_party/vulkan \
    third_party/vulkan-validation-layers \
    third_party/web-animations-js \
    third_party/webdriver \
    third_party/WebKit \
    third_party/webrtc \
    third_party/widevine \
    third_party/woff2 \
    third_party/xdg-utils \
    third_party/yasm/run_yasm.py \
    third_party/zlib/google \
    url/third_party/mozilla \
    v8/src/third_party/valgrind \
    v8/src/third_party/utf8-decoder \
    v8/third_party/inspector_protocol

./build/linux/unbundle/replace_gn_files.py --system-libraries \
    flac \
    freetype \
    fontconfig \
%if %{with system_libicu}
    icu \
%endif
    libdrm \
    libjpeg \
    libpng \
%if %{with system_libvpx}
    libvpx \
%endif
    libwebp \
%if %{with system_libxml2}
    libxml \
%endif
    libxslt \
    opus \
    re2 \
    snappy \
    yasm \
    zlib



sed -i 's|//third_party/usb_ids|/usr/share/hwdata|g' device/usb/BUILD.gn

# Workaround build error caused by debugedit
# https://bugzilla.redhat.com/show_bug.cgi?id=304121
sed -i "/relpath/s|/'$|'|" tools/metrics/ukm/gen_builders.py
sed -i 's|^\(#include "[^"]*\)//\([^"]*"\)|\1/\2|' \
    third_party/webrtc/modules/audio_processing/utility/ooura_fft.cc \
    third_party/webrtc/modules/audio_processing/utility/ooura_fft_sse2.cc

%if %{with system_jinja2}
rmdir third_party/jinja2
ln -s %{python2_sitelib}/jinja2 third_party/jinja2
%endif

rmdir third_party/markupsafe
ln -s %{python2_sitearch}/markupsafe third_party/markupsafe

%if %{with system_ply}
rmdir third_party/ply
ln -s %{python2_sitelib}/ply third_party/ply
%endif

mkdir -p third_party/node/linux/node-linux-x64/bin
ln -s %{_bindir}/node third_party/node/linux/node-linux-x64/bin/node

# Hard code extra version
FILE=chrome/common/channel_info_posix.cc
sed -i.orig -e 's/getenv("CHROME_VERSION_EXTRA")/"Chromium Vaapi for Fedora"/' $FILE

########################################################################################
%build
export AR=ar NM=nm

# Fedora 25 doesn't have __global_cxxflags
%if %{with fedora_compilation_flags}
export CFLAGS="$(echo '%{__global_cflags}' | sed 's/-fexceptions//')"
export CXXFLAGS="$(echo '%{?__global_cxxflags}%{!?__global_cxxflags:%{__global_cflags}}' | sed 's/-fexceptions//')"
export LDFLAGS='%{__global_ldflags}'
%endif

%if %{with clang}
export CC=clang CXX=clang++
%else
export CC=gcc CXX=g++
export CXXFLAGS="$CXXFLAGS -fno-delete-null-pointer-checks -fpermissive"
%endif
# do not eat all memory
ninjaproc="%{?jobs:%{jobs}}"
echo "Available memory:"
cat /proc/meminfo
echo "System limits:"
ulimit -a
if test -n "$ninjaproc" -a "$ninjaproc" -gt 1 ; then
    mem_per_process=1600000
    max_mem=$(awk '/MemTotal/ { print $2 }' /proc/meminfo)
    max_jobs="$(($max_mem / $mem_per_process))"
    test "$ninjaproc" -gt "$max_jobs" && ninjaproc="$max_jobs" && echo "Warning: Reducing number of jobs to $max_jobs because of memory limits"
    test "$ninjaproc" -le 0 && ninjaproc=1 && echo "Warning: Do not use the parallel build at all becuse of memory limits"
fi

gn_args=(
    is_debug=false
    use_vaapi=true
    enable_swiftshader=false
    is_component_build=false
    use_sysroot=false
    use_custom_libcxx=false
    use_aura=true
%ifarch x86_64
    'system_libdir="lib64"'
%endif
    use_cups=true
    use_gconf=false
    use_gnome_keyring=false
    use_gio=true
    use_kerberos=true
    use_libpci=true
    use_pulseaudio=true
    use_system_freetype=true
%if %{with system_harfbuzz}
    use_system_harfbuzz=true
%endif
%if %{freeworld}
    enable_hangout_services_extension=true
    'ffmpeg_branding="Chrome"'
    proprietary_codecs=true
%else
    'ffmpeg_branding="Chromium"'
    proprietary_codecs=false
    enable_hangout_services_extension=false
%endif
    enable_nacl=false
    enable_webrtc=true
    fatal_linker_warnings=false
    treat_warnings_as_errors=false
    linux_use_bundled_binutils=false
    fieldtrial_testing_like_official_build=true
    'custom_toolchain="//build/toolchain/linux/unbundle:default"'
    'host_toolchain="//build/toolchain/linux/unbundle:default"'
    'google_api_key="%{api_key}"'
    'google_default_client_id="%{default_client_id}"'
    'google_default_client_secret="%{default_client_secret}"'
)

gn_args+=(
%if %{with clang} || %{with require_clang}
    'clang_base_path="/usr"'
%endif
)

gn_args+=(
%if %{with clang}
    is_clang=true
    clang_use_chrome_plugins=false
%else
    is_clang=false
%endif
)

gn_args+=(
%if %{with symbol}
    symbol_level=1
%else
    symbol_level=0
%endif
)

./tools/gn/bootstrap/bootstrap.py --gn-gen-args "${gn_args[*]}"
./out/Release/gn gen out/Release --args="${gn_args[*]}"
ninja -v -j $ninjaproc -C out/Release chrome chrome_sandbox chromedriver widevinecdmadapter

#-----------------------------------------------------------------------------
%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{chromiumdir}/locales
#mkdir -p %{buildroot}%{chromiumdir}/swiftshader
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_datadir}/appdata
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/gnome-control-center/default-apps
sed -e "s|@@CHROMIUMDIR@@|%{chromiumdir}|" -e "s|@@BUILDTARGET@@|`cat /etc/redhat-release`|" \
    %{SOURCE10} > chromium-browser.sh
install -m 755 chromium-browser.sh %{buildroot}%{_bindir}/chromium-browser
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE11}
install -m 644 %{SOURCE12} %{buildroot}%{_datadir}/gnome-control-center/default-apps/
appstream-util validate-relax --nonet %{SOURCE13}
install -m 644 %{SOURCE13} %{buildroot}%{_datadir}/appdata/
sed -e "s|@@MENUNAME@@|Chromium|g" -e "s|@@PACKAGE@@|chromium|g" \
    chrome/app/resources/manpage.1.in > chrome.1
install -m 644 chrome.1 %{buildroot}%{_mandir}/man1/chromium-browser.1
install -m 755 out/Release/chrome %{buildroot}%{chromiumdir}/chromium-browser
install -m 4755 out/Release/chrome_sandbox %{buildroot}%{chromiumdir}/chrome-sandbox
install -m 755 out/Release/chromedriver %{buildroot}%{chromiumdir}/
%if !%{with system_libicu}
install -m 644 out/Release/icudtl.dat %{buildroot}%{chromiumdir}/
%endif
install -m 755 out/Release/lib*.so* %{buildroot}%{chromiumdir}/
install -m 644 out/Release/natives_blob.bin %{buildroot}%{chromiumdir}/
install -m 644 out/Release/snapshot_blob.bin %{buildroot}%{chromiumdir}/
install -m 644 out/Release/*.pak %{buildroot}%{chromiumdir}/
install -m 644 out/Release/locales/*.pak %{buildroot}%{chromiumdir}/locales/
for i in 16 32; do
    mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps
    install -m 644 chrome/app/theme/default_100_percent/chromium/product_logo_$i.png \
        %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/chromium-browser.png
done
for i in 22 24 32 48 64 128 256; do
    if [ ${i} = 32 ]; then ext=xpm; else ext=png; fi
    if [ ${i} = 32 ]; then dir=linux/; else dir=; fi
    mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps
    install -m 644 chrome/app/theme/chromium/${dir}product_logo_$i.${ext} \
        %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/chromium-browser.${ext}
done

#------------------------------------------------------------------------------
%post
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
update-desktop-database &> /dev/null || :
#----------------------------------------------------------------------
%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi
update-desktop-database &> /dev/null || :
#------------------------------------------------------------------------
%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
#------------------------------------------------------------------------------------------------------------------------

%files
%license LICENSE
%doc AUTHORS README.md
%{_bindir}/chromium-browser
%{_datadir}/appdata/chromium-browser.appdata.xml
%{_datadir}/applications/chromium-browser.desktop
%{_datadir}/gnome-control-center/default-apps/chromium-browser.xml
%{_datadir}/icons/hicolor/16x16/apps/chromium-browser.png
%{_datadir}/icons/hicolor/22x22/apps/chromium-browser.png
%{_datadir}/icons/hicolor/24x24/apps/chromium-browser.png
%{_datadir}/icons/hicolor/32x32/apps/chromium-browser.png
%{_datadir}/icons/hicolor/32x32/apps/chromium-browser.xpm
%{_datadir}/icons/hicolor/48x48/apps/chromium-browser.png
%{_datadir}/icons/hicolor/64x64/apps/chromium-browser.png
%{_datadir}/icons/hicolor/128x128/apps/chromium-browser.png
%{_datadir}/icons/hicolor/256x256/apps/chromium-browser.png
%{_mandir}/man1/chromium-browser.1.gz
%dir %{chromiumdir}
%{chromiumdir}/chromium-browser
%{chromiumdir}/chrome-sandbox
%{chromiumdir}/chromedriver
%if !%{with system_libicu}
%{chromiumdir}/icudtl.dat
%endif
%{chromiumdir}/natives_blob.bin
%{chromiumdir}/snapshot_blob.bin
%{chromiumdir}/*.pak
%{chromiumdir}/lib*.so*
%dir %{chromiumdir}/locales
%{chromiumdir}/locales/*.pak
%license LICENSE
%doc AUTHORS
