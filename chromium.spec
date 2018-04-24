# This spec file is based on other spec files, ebuilds, PKGBUILDs available from
#  [1] https://repos.fedorapeople.org/repos/spot/chromium/
#  [2] https://copr.fedoraproject.org/coprs/churchyard/chromium-russianfedora-tested/
#  [3] https://www.archlinux.org/packages/extra/x86_64/chromium/
#  [4] https://src.fedoraproject.org/rpms/chromium/
#  [5] https://gitweb.gentoo.org/repo/gentoo.git/tree/www-client/chromium/
#  [6] https://copr.fedorainfracloud.org/coprs/lantw44/chromium/
# Get the version number of latest stable version
# $ curl -s 'https://omahaproxy.appspot.com/all?os=linux&channel=stable' | sed 1d | cut -d , -f 3
######################################################################################################################
####################################################################################################
#Global Libraries
#Do not turn these on in Fedora copr!
%global obs 0
%global freeworld 0
### Google API keys (see http://www.chromium.org/developers/how-tos/api-keys)
### Note: These are for Fedora use ONLY.
### For your own distribution, please get your own set of keys.
### http://lists.debian.org/debian-legal/2013/11/msg00006.html
%global api_key AIzaSyDUIXvzVrt5OkVsgXhQ6NFfvWlA44by-aw
%global default_client_id 449907151817.apps.googleusercontent.com
%global default_client_secret miEreAep8nuvTdvLums6qyLK
%global chromiumdir %{_libdir}/chromium-browser

####################################Bullshit Area##################################################
%global __provides_exclude_from %{chromium_path}/.*\\.so|%{chromium_path}/lib/.*\\.so
%global privlibs libaccessibility|libanimation|libaura_extra|libaura|libbase_i18n|libbase|libbindings|libblink_android_mojo_bindings_shared|libblink_common|libblink_controller|libblink_core_mojo_bindings_shared|libblink_core|libblink_modules|libblink_mojo_bindings_shared|libblink_offscreen_canvas_mojo_bindings_shared|libblink_platform|libbluetooth|libboringssl|libbrowser_ui_views|libcaptive_portal|libcapture_base|libcapture_lib|libcbor|libcc_animation|libcc_base|libcc_blink|libcc_debug|libcc_ipc|libcc_paint|libcc|libcdm_manager|libchromium_sqlite3|libclearkeycdm|libclient|libcloud_policy_proto_generated_compile|libcodec|libcolor_space|libcommon|libcompositor|libcontent_common_mojo_bindings_shared|libcontent_public_common_mojo_bindings_shared|libcontent|libcpp|libcrash_key|libcrcrypto|libdbus|libdevice_base|libdevice_event_log|libdevice_features|libdevice_gamepad|libdevices|libdevice_vr_mojo_bindings_blink|libdevice_vr_mojo_bindings_shared|libdevice_vr_mojo_bindings|libdevice_vr|libdiscardable_memory_client|libdiscardable_memory_common|libdiscardable_memory_service|libdisplay|libdisplay_types|libdisplay_util|libdomain_reliability|libEGL|libembedder|libembedder_switches|libevents_base|libevents_devices_x11|libevents_ozone_layout|libevents|libevents_x|libffmpeg|libfingerprint|libfontconfig|libfreetype_harfbuzz|libgcm|libgeolocation|libgeometry_skia|libgeometry|libgesture_detection|libgfx_ipc_buffer_types|libgfx_ipc_color|libgfx_ipc_geometry|libgfx_ipc_skia|libgfx_ipc|libgfx|libgfx_switches|libgfx_x11|libgin|libgles2_c_lib|libgles2_implementation|libgles2|libgles2_utils|libGLESv2|libgl_init|libgl_in_process_context|libgl_wrapper|libgpu_ipc_service|libgpu|libgpu_util|libgtk3ui|libheadless|libhost|libicui18n|libicuuc|libipc_mojom_shared|libipc_mojom|libipc|libkeyboard|libkeyboard_with_content|libkeycodes_x11|libkeyed_service_content|libkeyed_service_core|libleveldatabase|libmanager|libmedia_blink|libmedia_devices_mojo_bindings_shared|libmedia_gpu|libmedia_mojo_services|libmedia|libmessage_center|libmessage_support|libmetrics_cpp|libmidi|libmojo_base_lib|libmojo_base_mojom_blink|libmojo_base_mojom_shared|libmojo_base_mojom|libmojo_base_shared_typemap_traits|libmojo_bindings_shared|libmojo_common_lib|libmojo_ime_lib|libmojo_platform_bindings_shared|libmojo_public_system_cpp|libmojo_public_system|libmojo_system_impl|libnative_theme|libnet|libnet_with_v8|libnetwork_session_configurator|libonc|libplatform|libpolicy_component|libpolicy_proto|libppapi_host|libppapi_proxy|libppapi_shared|libprefs|libprinting|libprotobuf_lite|libproxy_config|librange|libresource_coordinator_cpp_base|libresource_coordinator_cpp|libresource_coordinator_public_interfaces_blink|libresource_coordinator_public_interfaces_shared|libresource_coordinator_public_interfaces|libsandbox_services|libsandbox|libseccomp_bpf|libsensors|libservice_manager_cpp|libservice_manager_cpp_types|libservice_manager_mojom_blink|libservice_manager_mojom_constants_blink|libservice_manager_mojom_constants_shared|libservice_manager_mojom_constants|libservice_manager_mojom_shared|libservice_manager_mojom|libservice|libsessions|libshared_memory_support|libshell_dialogs|libskia|libsnapshot|libsql|libstartup_tracing|libstorage_browser|libstorage_common|libstub_window|libsuid_sandbox_client|libsurface|libtracing|libui_base_ime|libui_base|libui_base_x|libui_data_pack|libui_devtools|libui_touch_selection|libui_views_mus_lib|liburl_ipc|liburl_matcher|liburl|libuser_manager|libuser_prefs|libv8_libbase|libv8_libplatform|libv8|libviews|libviz_common|libviz_resource_format|libVkLayer_core_validation|libVkLayer_object_tracker|libVkLayer_parameter_validation|libVkLayer_threading|libVkLayer_unique_objects|libwebdata_common|libweb_dialogs|libwebview|libwidevinecdmadapter|libwidevinecdm|libwm_public|libwm|libwtf|libx11_events_platform|libx11_window
%global __requires_exclude ^(%{privlibs})\\.so

########################################################################################################################


#######################################CONFIGS###############################################################

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
%global symbol 0

# Allow compiling with clang
# Enabled by default because gcc is shit 

%global clang 1

# Allow using compilation flags set by Fedora RPM macros
# Disabled by default because it causes out-of-memory error on Fedora Copr
%bcond_with fedora_compilation_flags


########################################################################################################
Name:       chromium
Version:    66.0.3359.117
Release:    108%{?dist}.chromium_vaapi
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
#Added clang llvm compiler to save myself from outdated gcc from http://releases.llvm.org/download.html(prebuilt binaries)
Source4:    llvm-clang.tar.xz

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
Patch2:    widevine.patch

#how the hell they forgot about adding this to the tarball :@
Patch11:    blinktools.patch




%if %{clang}
#Will use any clang patch here


%else
#Gcc patches area. 
Patch12:    gcc7-r540828.patch
Patch13:    gcc7-r541029.patch
Patch14:    gcc7-r541827.patch
Patch15:    gcc7516.patch
Patch16:    gcc7815.patch

# Add a patch from Fedora to fix build with GCC 8
# https://src.fedoraproject.org/cgit/rpms/chromium.git/commit/?id=8cfa28d
# https://src.fedoraproject.org/cgit/rpms/chromium.git/commit/?id=61203bf
Patch17:    mojojojo.patch
%endif

Patch50:    unrar.patch

#Video acceleration patch from https://chromium-review.googlesource.com/c/chromium/src/+/532294
Patch100:    vaapi.patch

%if !%{clang}
# Make sure we don't encounter any bug! GCC below 7.3.1-5 fails.
%if 0%{?fedora} >= 22
BuildRequires: gcc >= 7.3.1-5
%endif
%endif
# Chromium 54 requires clang to enable nacl support
# Chromium 59 requires llvm-ar to enable nacl support

#BuildRequires: clang, llvm
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
#------------------------------------------------------------------------------------------
Requires(post):   desktop-file-utils
Requires(postun): desktop-file-utils

# For selinux scriptlet
#Requires(post): /usr/sbin/semanage
#Requires(post): /usr/sbin/restorecon
Requires:         hicolor-icon-theme

#Libva required
Requires:	libva
Obsoletes:     chromedriver <= %{version}-%{release}
Obsoletes:     chromium-common <= %{version}-%{release}
Obsoletes:     chromium-headless <= %{version}-%{release}
Obsoletes:     chromium-libs <= %{version}-%{release}
Obsoletes:     chromium-libs-media <= %{version}-%{release}

Provides:      chromedriver = %{version}-%{release}
Provides:      chromium-common = %{version}-%{release}
Provides:      chromium-headless = %{version}-%{release}
Provides:      chromium-libs = %{version}-%{release}
Provides:      chromium-libs-media = %{version}-%{release}

Provides:      chromedriver-stable = %{version}-%{release}
Conflicts:     chromedriver-testing
Conflicts:     chromedriver-unstable

%if !%{symbol}
%global debug_package %{nil}
%endif

%description
Chromium is an open-source web browser, powered by WebKit (Blink).
###########################################################################################################################
%prep
%autosetup -p1
%if %{clang}
#Add and extract clang llvm to third_party dir
pushd third_party
tar -xf %{SOURCE4} 
chmod +x -R llvm-clang/bin/*
popd
%endif

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
    buildtools/third_party/libc++ \
    buildtools/third_party/libc++abi \
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
    third_party/angle/third_party/glslang \
    third_party/angle/third_party/spirv-headers \
    third_party/angle/third_party/spirv-tools \
    third_party/angle/third_party/vulkan-validation-layers \
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
    third_party/libaom/source/libaom/third_party/x86inc \
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
%if %{clang}
    third_party/llvm-clang \
%endif
    third_party/lss \
    third_party/lzma_sdk \
    third_party/mesa \
    third_party/metrics_proto \
    third_party/modp_b64 \
    third_party/node \
    third_party/node/node_modules/polymer-bundler/lib/third_party/UglifyJS2 \
    third_party/openh264 \
    third_party/openmax_dl \
    third_party/ots \
    third_party/pdfium \
    third_party/pdfium/third_party/agg23 \
    third_party/pdfium/third_party/base \
    third_party/pdfium/third_party/bigint \
    third_party/pdfium/third_party/freetype \
    third_party/pdfium/third_party/lcms \
    third_party/pdfium/third_party/libopenjpeg20 \
    third_party/pdfium/third_party/libpng16 \
    third_party/pdfium/third_party/libtiff \
    third_party/pdfium/third_party/skia_shared \
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

# Fix the path to nodejs binary
mkdir -p third_party/node/linux/node-linux-x64/bin
ln -s %{_bindir}/node third_party/node/linux/node-linux-x64/bin/node

# Hard code extra version
FILE=chrome/common/channel_info_posix.cc
sed -i.orig -e 's/getenv("CHROME_VERSION_EXTRA")/"Chromium Vaapi for Fedora"/' $FILE

########################################################################################
%build
%if %{obs}
# do not eat all memory on open build service
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
%endif


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
%if %{clang}
    is_clang=true
%if %{obs}
   'clang_base_path = "~/rpmbuild/BUILD/chromium-%{version}/third_party/llvm-clang/"'
%else
'clang_base_path = "~/build/BUILD/chromium-%{version}/third_party/llvm-clang/"'
%endif
    clang_use_chrome_plugins=false
%else
    is_clang=false
%endif
)

gn_args+=(
%if %{symbol}
    symbol_level=1
%else
    symbol_level=0
%endif
)

#export compilar variables
export AR=ar NM=nm

# Fedora 25 doesn't have __global_cxxflags
%if %{with fedora_compilation_flags}
export CFLAGS="$(echo '%{__global_cflags}' | sed 's/-fexceptions//')"
export CXXFLAGS="$(echo '%{?__global_cxxflags}%{!?__global_cxxflags:%{__global_cflags}}' | sed 's/-fexceptions//')"
export LDFLAGS='%{__global_ldflags}'
%endif

%if %{clang}
%if %{obs}
export CC=~/rpmbuild/BUILD/chromium-%{version}/third_party/llvm-clang/bin/clang 
export CXX=~/rpmbuild/BUILD/chromium-%{version}/third_party/llvm-clang/bin/clang++
%else
export CC=~/build/BUILD/chromium-%{version}/third_party/llvm-clang/bin/clang
export CXX=~/build/BUILD/chromium-%{version}/third_party/llvm-clang/bin/clang++
%endif
%else
export CC=gcc CXX=g++
export CXXFLAGS="$CXXFLAGS -fno-delete-null-pointer-checks -fpermissive"
%endif




tools/gn/bootstrap/bootstrap.py -v --gn-gen-args "${gn_args[*]}"
out/Release/gn gen out/Release --args="${gn_args[*]}"

%if %{freeworld}
ninja -v %{_smp_mflags} -C out/Release chrome chrome_sandbox chromedriver widevinecdmadapter
%else
ninja -v %{_smp_mflags} -C out/Release chrome chrome_sandbox chromedriver
%endif

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
install -m 644 out/Release/v8_context_snapshot.bin %{buildroot}%{chromiumdir}/
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
# Set SELinux labels - semanage itself will adjust the lib directory naming
# But only do it when selinux is enabled, otherwise, it gets noisy.
#Disabling this for the moment
#if selinuxenabled; then
#	semanage fcontext -a -t bin_t %{chromiumdir}/chromium-browser
#	semanage fcontext -a -t bin_t %{chromiumdir}/chromedriver
#	semanage fcontext -a -t chrome_sandbox_exec_t %{chromiumdir}/chrome-sandbox
#	restorecon -R -v %{chromiumdir}/
#fi
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
%{chromiumdir}/v8_context_snapshot.bin
%{chromiumdir}/*.pak
%{chromiumdir}/lib*.so*
%dir %{chromiumdir}/locales
%{chromiumdir}/locales/*.pak
%license LICENSE
%doc AUTHORS

##################################################################################################

%changelog
* Mon Apr 23 2018 Akarshan Biswas <akarshan.biswas@gmail.com> - 66.0.3359.117-108.chromium_vaapi
- Fixed crashing by adding v8_context_snapshot and Changed to llvm clang from
  gcc

* Fri Apr 20 2018 Akarshan Biswas <akarshan.biswas@gmail.com> - 66.0.3359.117-106.chromium_vaapi
- Update to 66.0.3359.117

* Fri Mar 23 2018 Akarshan Biswas <akarshan.biswas@gmail.com> - 65.0.3325.181-105.chromium_vaapi
- Update to 65.0.3325.181

* Wed Mar 21 2018 Akarshan Biswas <akarshan.biswas@gmail.com> - 65.0.3325.162-103.chromium_vaapi
- Update to 65.0.3325.162

* Wed Mar 07 2018 Akarshan Biswas <akarshan.biswas@gmail.com> - 65.0.3325.146-102.chromium_vaapi
- Updated to 65.0.3325.146

* Thu Mar 01 2018 Akarshan Biswas <akarshan.biswas@gmail.com> - 64.0.3282.186-101.chromium_vaapi
- Initial release
