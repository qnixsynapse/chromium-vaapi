#Global Libraries
#Do not turn it on in Fedora copr!
%global freeworld 1
#This can be any folder on out
%global target out/Release
### Google API keys (see http://www.chromium.org/developers/how-tos/api-keys)
### Note: These are for Fedora use ONLY.
### For your own distribution, please get your own set of keys.
### http://lists.debian.org/debian-legal/2013/11/msg00006.html
%global api_key AIzaSyDUIXvzVrt5OkVsgXhQ6NFfvWlA44by-aw
%global default_client_id 449907151817.apps.googleusercontent.com
%global default_client_secret miEreAep8nuvTdvLums6qyLK
###############################Exclude Private chromium libs###########################
%global __requires_exclude %{chromiumdir}/.*\\.so
%global __provides_exclude_from %{chromiumdir}/.*\\.so
#######################################CONFIGS###########################################
# Fedora's Python 2 stack is being removed, we use the bundled Python libraries	
# This can be revisited once we upgrade to Python 3	
%global bundlepylibs 1
%if 0%{bundlepylibs}
%bcond_with system_ply
%else
%bcond_without system_ply
%endif
# This package depends on automagic byte compilation            
# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_2            
%global _python_bytecompile_extra 1
#Require harfbuzz >= 2.4.0 for hb_subset_input_set_retain_gids
%if 0%{?fedora} >= 31
%bcond_without system_harfbuzz
%else
%bcond_with system_harfbuzz
%endif
# Require libxml2 > 2.9.4 for XML_PARSE_NOXXE
%bcond_without system_libxml2


# Allow testing whether icu can be unbundled
# A patch fix building so enabled by default for Fedora 30
# Need icu version >= 64
%bcond_with system_libicu
# Allow testing whether libvpx can be unbundled
%bcond_without system_libvpx
# Allow testing whether ffmpeg can be unbundled
%bcond_without system_ffmpeg
#Allow minizip to be unbundled
#mini-compat is going to be removed from fedora 30!
%bcond_without system_minizip
# Need re2 ver. 2016.07.21 for re2::LazyRE2 
%bcond_with system_re2

#Turn on verbose mode
%global debug_logs 0
#Allow jumbo builds
# Enabled by default
%global jumbo 1
#------------------------------------------------------
#Build debug packages for debugging
%global debug_pkg 1
# Enable building with ozone support
%global ozone 0
##############################Package Definitions######################################
Name:       chromium-vaapi
Version:    77.0.3865.90
Release:    1%{?dist}
Summary:    A Chromium web browser with video decoding acceleration
License:    BSD and LGPLv2+ and ASL 2.0 and IJG and MIT and GPLv2+ and ISC and OpenSSL and (MPLv1.1 or GPLv2 or LGPLv2)
URL:        https://www.chromium.org/Home
%if %{freeworld}
Source0:    https://commondatastorage.googleapis.com/chromium-browser-official/chromium-%{version}.tar.xz
%else
# Unfortunately, Fedora & Copr forbids uploading sources with patent-encumbered
# ffmpeg code even if they are never compiled and linked to target binaries,
# so we must repackage upstream tarballs to satisfy this requirement. However,
# we cannot simply delete all code of ffmpeg because this will disable support
# for some commonly-used free codecs such as Ogg Theora. Instead, helper
# scripts included in official Fedora packages are copied, modified, and used
# to automate the repackaging work.
# Get those helper scripts from https://src.fedoraproject.org/rpms/chromium
# If you don't use Fedora services, Just set the value of freeworld in this spec file
# to 1 to use the upstreanm packaged source.
# The repackaged source tarball used here is produced by:
# ./chromium-latest.py --stable --ffmpegclean --ffmpegarm --deleteunrar
Source0:   chromium-%{version}-clean.tar.xz
%endif
# The following two source files are copied and modified from the chromium source
Source10:  %{name}.sh
#Add our own appdata file. 
Source11:  %{name}.appdata.xml
#Personal stuff
Source15:  LICENSE
######################## Installation Folder #################################################
#Our installation folder
%global chromiumdir %{_libdir}/%{name}
########################################################################################
#Compiler settings
# Make sure we don't encounter any bug
BuildRequires: gcc-c++
# Basic tools and libraries needed for building
BuildRequires: ninja-build, nodejs, bison, gperf, hwdata
BuildRequires: libgcc, glibc, libatomic
BuildRequires: libcap-devel, cups-devel, alsa-lib-devel
BuildRequires: mesa-libGL-devel, mesa-libEGL-devel
%if %{with system_minizip}
BuildRequires:	minizip-compat-devel
%endif
# Pipewire need this.
%if 0%{?fedora} >= 29
BuildRequires:	pkgconfig(libpipewire-0.2)
%endif
BuildRequires: pkgconfig(gtk+-2.0), pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(libexif), pkgconfig(nss)
BuildRequires: pkgconfig(xtst), pkgconfig(xscrnsaver)
BuildRequires: pkgconfig(dbus-1), pkgconfig(libudev)
BuildRequires: pkgconfig(gnome-keyring-1)
BuildRequires: pkgconfig(libffi)
#for vaapi
BuildRequires: pkgconfig(libva)
%if %{ozone}
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server)
%endif

#Python stuffs
%if 0%{?bundlepylibs}
	
# Using bundled bits, do nothing.
#This is needed for remove_bundled_libraries.py
BuildRequires: /usr/bin/python2
	
%else
BuildRequires: python2-rpm-macros
BuildRequires: python2-beautifulsoup4
BuildRequires: python2-lxml
BuildRequires: python2-html5lib
BuildRequires: python2-markupsafe
Buildrequires: python2-six
%if %{with system_ply}
BuildRequires: python2-ply
%endif
%endif
%if %{with system_re2}
BuildRequires: re2-devel
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
%if %{with system_ffmpeg}
BuildRequires: ffmpeg-devel
%endif
BuildRequires: libwebp-devel
%if %{with system_libxml2}
BuildRequires: pkgconfig(libxml-2.0)
%endif
BuildRequires: pkgconfig(libxslt)
BuildRequires: opus-devel
BuildRequires: snappy-devel
BuildRequires: yasm
BuildRequires: pciutils-devel
BuildRequires: speech-dispatcher-devel
BuildRequires: pulseaudio-libs-devel
# install desktop files
BuildRequires: desktop-file-utils
# install AppData files
BuildRequires: libappstream-glib
# Mojojojo need this >:(
BuildRequires: java-1.8.0-openjdk
# Libstdc++ static needed for linker
BuildRequires:  libstdc++-static
#Runtime Requirements
Requires:       hicolor-icon-theme
#Some recommendations
Recommends:    libva-utils
%if !%{debug_pkg}
%global debug_package %{nil}
%endif
# This build should be only available to amd64
ExclusiveArch: x86_64
# Define Patches here ##
# Enable video acceleration on chromium for Linux
Patch1:    enable-vaapi.patch
# Enable support for widevine
Patch2:   widevine.patch
#Use Normal BAM on Linux
Patch3:   UseNormalBAM.patch
#Fix certificare transperancy error introduced by the current stable version of chromium
Patch5:    cert-trans-google.patch 
# Bootstrap still uses python command
Patch51:  py2-bootstrap.patch
# Fix building with system icu
Patch52:  chromium-system-icu.patch
# Let's brand chromium!
Patch54:  brand.patch
#Stolen from Fedora to fix building with pipewire
# https://src.fedoraproject.org/rpms/chromium/blob/master/f/chromium-73.0.3683.75-pipewire-cstring-fix.patch
Patch65: chromium-73.0.3683.75-pipewire-cstring-fix.patch
# Fix header
Patch68: Add-missing-header-to-fix-webrtc-build.patch
# GCC patches
Patch69: chromium-gcc9-r681333.patch
Patch70: chromium-gcc9-r681321.patch
Patch71: chromium-unbundle-zlib.patch
Patch72: chromium-base-location.patch
Patch73: chromium-gcc9-r684731.patch

# This patch fixes linking when build with system harfbuzz is enabled
Patch74: link-against-harfbuzz-subset.patch


%description
%{name} is an open-source web browser, powered by WebKit (Blink)
############################################PREP###########################################################
%prep
%autosetup -n chromium-%{version} -p1
%if !%{with system_libicu}
%patch52 -p1  -R
%endif
%if !%{freeworld}
%patch54 -p1 -R
%endif
%if !%{with system_harfbuzz}
%patch74 -p1 -R
%endif


#Let's change the default shebang of python files.
find -depth -type f -writable -name "*.py" -exec sed -iE '1s=^#! */usr/bin/\(python\|env python\)[23]\?=#!%{__python2}=' {} +
./build/linux/unbundle/remove_bundled_libraries.py --do-remove \
    base/third_party/cityhash \
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
    net/third_party/quic \
    net/third_party/uri_template \
    third_party/abseil-cpp \
    third_party/adobe \
    third_party/angle \
    third_party/angle/src/common/third_party/base \
    third_party/angle/src/common/third_party/smhasher \
    third_party/angle/src/common/third_party/xxhash \
    third_party/angle/src/third_party/compiler \
    third_party/angle/src/third_party/libXNVCtrl \
    third_party/angle/src/third_party/trace_event \
    third_party/glslang \
    third_party/angle/third_party/spirv-headers \
    third_party/angle/third_party/spirv-tools \
    third_party/angle/third_party/vulkan-headers \
    third_party/angle/third_party/vulkan-loader \
    third_party/angle/third_party/vulkan-tools \
    third_party/angle/third_party/vulkan-validation-layers \
    third_party/apple_apsl \
    third_party/axe-core \
    third_party/boringssl \
    third_party/boringssl/src/third_party/fiat \
    third_party/boringssl/src/third_party/sike \
    third_party/boringssl/linux-aarch64/crypto/third_party/sike \
    third_party/boringssl/linux-x86_64/crypto/third_party/sike \
    third_party/blink \
    third_party/breakpad \
    third_party/breakpad/breakpad/src/third_party/curl \
    third_party/brotli \
    third_party/cacheinvalidation \
    third_party/catapult \
    third_party/catapult/common/py_vulcanize/third_party/rcssmin \
    third_party/catapult/common/py_vulcanize/third_party/rjsmin \
    %if 0%{?bundlepylibs}
    third_party/catapult/third_party/beautifulsoup4 \
    third_party/catapult/third_party/html5lib-python \
    %endif
    third_party/catapult/third_party/polymer \
    third_party/catapult/third_party/six \
    third_party/catapult/tracing/third_party/d3 \
    third_party/catapult/tracing/third_party/gl-matrix \
    third_party/catapult/tracing/third_party/jszip \
    third_party/catapult/tracing/third_party/mannwhitneyu \
    third_party/catapult/tracing/third_party/oboe \
    third_party/catapult/tracing/third_party/pako \
    third_party/ced \
    third_party/cld_3 \
    third_party/closure_compiler \
    third_party/crashpad \
    third_party/crashpad/crashpad/third_party/lss \
    third_party/crashpad/crashpad/third_party/zlib \
    third_party/crc32c \
    third_party/cros_system_api \
    third_party/dawn \
    third_party/dav1d \
    third_party/devscripts \
    third_party/dom_distiller_js \
    third_party/emoji-segmenter \
%if !%{with system_ffmpeg}
    third_party/ffmpeg \
%endif
    third_party/flatbuffers \
    third_party/flot \
    third_party/freetype \
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
    third_party/jinja2 \
    third_party/jsoncpp \
    third_party/jstemplate \
    third_party/khronos \
    third_party/leveldatabase \
    third_party/libaddressinput \
    third_party/libaom \
    third_party/libaom/source/libaom/third_party/vector \
    third_party/libaom/source/libaom/third_party/x86inc \
    third_party/libjingle \
    third_party/libphonenumber \
    third_party/libsecret \
    third_party/libsrtp \
    third_party/libsync \
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
%if 0%{?bundlepylibs}	
	third_party/markupsafe \
%endif
    third_party/mesa \
    third_party/metrics_proto \
%if %{ozone}
    third_party/minigbm \
%endif
%if !%{with system_minizip}
    third_party/minizip/ \
%endif
    third_party/modp_b64 \
    third_party/nasm \
    third_party/node \
    third_party/node/node_modules/polymer-bundler/lib/third_party/UglifyJS2 \
    third_party/one_euro_filter \
    third_party/openh264 \
    third_party/openscreen \
    third_party/openscreen/src/third_party/tinycbor/src/src \
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
    third_party/perfetto \
    third_party/pffft \
%if !%{with system_ply}
    third_party/ply \
%endif
    third_party/polymer \
    third_party/protobuf \
    third_party/protobuf/third_party/six \
    third_party/pyjson5 \
    third_party/qcms \
%if !%{with system_re2}
    third_party/re2 \
%endif
    third_party/rnnoise \
    third_party/s2cellid \
    third_party/sfntly \
    third_party/skia \
    third_party/skia/include/third_party/skcms \
    third_party/skia/include/third_party/vulkan \
    third_party/skia/third_party/gif \
    third_party/skia/third_party/vulkan \
    third_party/skia/third_party/skcms \
    third_party/smhasher \
    third_party/speech-dispatcher \
    third_party/spirv-headers \
    third_party/SPIRV-Tools \
    third_party/sqlite \
    third_party/swiftshader \
    third_party/swiftshader/third_party/llvm-7.0 \
    third_party/swiftshader/third_party/llvm-subzero \
    third_party/swiftshader/third_party/subzero \
    third_party/swiftshader/third_party/SPIRV-Headers/include/spirv/unified1 \
    third_party/tcmalloc \
    third_party/unrar \
    third_party/usb_ids \
    third_party/usrsctp \
    third_party/vulkan \
%if %{ozone}
    third_party/wayland \
%endif
    third_party/web-animations-js \
    third_party/webdriver \
    third_party/webrtc \
    third_party/webrtc/common_audio/third_party/fft4g \
    third_party/webrtc/common_audio/third_party/spl_sqrt_floor \
    third_party/webrtc/modules/third_party/fft \
    third_party/webrtc/modules/third_party/g711 \
    third_party/webrtc/modules/third_party/g722 \
    third_party/webrtc/rtc_base/third_party/base64 \
    third_party/webrtc/rtc_base/third_party/sigslot \
    third_party/widevine \
    third_party/woff2 \
    third_party/xdg-utils \
    third_party/yasm/run_yasm.py \
    third_party/zlib/google \
%if !%{with system_minizip}
    third_party/zlib \
%endif
    tools/gn/base/third_party/icu \
    url/third_party/mozilla \
    v8/src/third_party/siphash \
    v8/src/third_party/valgrind \
    v8/src/third_party/utf8-decoder \
    v8/third_party/inspector_protocol \
    v8/third_party/v8

./build/linux/unbundle/replace_gn_files.py --system-libraries \
%if %{with system_ffmpeg}
    ffmpeg \
%endif
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
%if %{with system_re2}
    re2 \
%endif
    snappy \
    yasm \
%if %{with system_minizip}
    zlib
%endif

sed -i 's|//third_party/usb_ids|/usr/share/hwdata|g' \
    services/device/public/cpp/usb/BUILD.gn

%if !0%{?bundlepylibs}
rmdir third_party/markupsafe
ln -s %{python2_sitearch}/markupsafe third_party/markupsafe
%if %{with system_ply}
rmdir third_party/ply
ln -s %{python2_sitelib}/ply third_party/ply
%endif
%endif

# Fix the path to nodejs binary
mkdir -p third_party/node/linux/node-linux-x64/bin
ln -s %{_bindir}/node third_party/node/linux/node-linux-x64/bin/node
# Hard code extra version
FILE=chrome/common/channel_info_posix.cc
sed -i.orig -e 's/getenv("CHROME_VERSION_EXTRA")/"%{name}"/' $FILE
#####################################BUILD#############################################
%build
#export compilar variables
export AR=ar NM=nm AS=as
export CC=gcc CXX=g++

# GN needs gold to bootstrap
export LDFLAGS="$LDFLAGS -fuse-ld=gold"

gn_args=(
    is_debug=false
    use_vaapi=true
    is_component_build=false
    use_sysroot=false
    use_custom_libcxx=false
    use_aura=true
    'system_libdir="%{_lib}"'
    use_cups=true
    use_gnome_keyring=true
    use_gio=true
    use_kerberos=true
    use_libpci=true
    use_pulseaudio=true
    link_pulseaudio=true
    use_system_freetype=true
    enable_widevine=true
%if %{with system_harfbuzz}
    use_system_harfbuzz=true
%endif
%if %{freeworld}
    'ffmpeg_branding="Chrome"'
    proprietary_codecs=true
%else
    'ffmpeg_branding="Chromium"'
    proprietary_codecs=false
%endif
    enable_nacl=false
    enable_hangout_services_extension=false
    fatal_linker_warnings=false
    treat_warnings_as_errors=false
    linux_use_bundled_binutils=false
    blink_symbol_level = 0
    fieldtrial_testing_like_official_build=true
    'custom_toolchain="//build/toolchain/linux/unbundle:default"'
    'host_toolchain="//build/toolchain/linux/unbundle:default"'
    'google_api_key="%{api_key}"'
    'google_default_client_id="%{default_client_id}"'
    'google_default_client_secret="%{default_client_secret}"'
)

#compiler settings
# 'clang_base_path = "/usr"'
# use_lld=false
  #  clang_use_chrome_plugins=false
gn_args+=(
    is_clang=false
)
#Jumbo stuff
gn_args+=(
%if %{jumbo}
    use_jumbo_build=true
    jumbo_file_merge_limit=6
    concurrent_links=1
%endif
)

#Pipewire
gn_args+=(
%if 0%{?fedora} >= 29
     rtc_use_pipewire=true
     rtc_link_pipewire=true
%endif
)

# Ozone stuff : Whole work is done completely upstream.
gn_args+=(
%if %{ozone}
    use_ozone=true
    use_system_minigbm=true 
    use_xkbcommon=true
%endif
)


#symbol
gn_args+=(
%if %{debug_pkg}
    symbol_level=1
%endif
)
tools/gn/bootstrap/bootstrap.py  --gn-gen-args "${gn_args[*]}"
%{target}/gn --script-executable=%{__python2} gen --args="${gn_args[*]}" %{target}
%if %{debug_logs}
ninja  %{_smp_mflags} -C %{target} -v  chrome chrome_sandbox chromedriver
%else
ninja  %{_smp_mflags} -C %{target}   chrome chrome_sandbox chromedriver
%endif
######################################Install####################################
%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{chromiumdir}/locales
mkdir -p %{buildroot}%{chromiumdir}/MEIPreload
mkdir -p %{buildroot}%{chromiumdir}/swiftshader
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_metainfodir}
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/gnome-control-center/default-apps
sed -e "s|@@CHROMIUMDIR@@|%{chromiumdir}|"     %{SOURCE10} > %{name}.sh
install -m 755 %{name}.sh %{buildroot}%{_bindir}/%{name}
install -m 644 %{SOURCE11} %{buildroot}%{_metainfodir}
sed -e "s|@@MENUNAME@@|%{name}|g" -e "s|@@PACKAGE@@|%{name}|g" \
    chrome/app/resources/manpage.1.in > chrome.1
install -m 644 chrome.1 %{buildroot}%{_mandir}/man1/%{name}.1
sed -e "s|@@MENUNAME@@|%{name}|g" -e "s|@@PACKAGE@@|%{name}|g" -e "s|@@USR_BIN_SYMLINK_NAME@@|%{name}|g" \
    chrome/installer/linux/common/desktop.template > %{name}.desktop
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{name}.desktop
sed -e "s|@@MENUNAME@@|%{name}|g" -e "s|@@PACKAGE@@|%{name}|g" -e "s|@@INSTALLDIR@@|%{_bindir}|g" \
chrome/installer/linux/common/default-app.template > %{name}.xml
install -m 644 %{name}.xml %{buildroot}%{_datadir}/gnome-control-center/default-apps/
install -m 755 %{target}/chrome %{buildroot}%{chromiumdir}/%{name}
install -m 4755 %{target}/chrome_sandbox %{buildroot}%{chromiumdir}/chrome-sandbox
install -m 755 %{target}/chromedriver %{buildroot}%{chromiumdir}/
%if !%{with system_libicu}
install -m 644 %{target}/icudtl.dat %{buildroot}%{chromiumdir}/
%endif
install -m 644 %{target}/natives_blob.bin %{buildroot}%{chromiumdir}/
install -m 644 %{target}/v8_context_snapshot.bin %{buildroot}%{chromiumdir}/
install -m 644 %{target}/*.pak %{buildroot}%{chromiumdir}/
install -m 644 %{target}/locales/*.pak %{buildroot}%{chromiumdir}/locales/
install -m 644 %{target}/xdg*  %{buildroot}%{chromiumdir}/
install -m 644 %{target}/MEIPreload/* %{buildroot}%{chromiumdir}/MEIPreload/
install -m 755 %{target}/swiftshader/*.so %{buildroot}%{chromiumdir}/swiftshader/

# Icons
for i in 16 32; do
    mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps
    install -m 644 chrome/app/theme/default_100_percent/chromium/product_logo_$i.png \
        %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/%{name}.png
done
for i in 24 32 48 64 128 256; do
    if [ ${i} = 32 ]; then ext=xpm; else ext=png; fi
    if [ ${i} = 32 ]; then dir=linux/; else dir=; fi
    mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps
    install -m 644 chrome/app/theme/chromium/${dir}product_logo_$i.${ext} \
        %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/%{name}.${ext}
done
####################################check##################################################
%check
appstream-util validate-relax --nonet "%{buildroot}%{_metainfodir}/%{name}.appdata.xml"
######################################files################################################
%files
%license LICENSE
%doc AUTHORS 
%{_bindir}/%{name}
%{_metainfodir}/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/gnome-control-center/default-apps/%{name}.xml
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_datadir}/icons/hicolor/24x24/apps/%{name}.png
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/32x32/apps/%{name}.xpm
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
%{_mandir}/man1/%{name}.1.gz
%dir %{chromiumdir}
%{chromiumdir}/%{name}
%{chromiumdir}/chrome-sandbox
%{chromiumdir}/chromedriver
%if !%{with system_libicu}
%{chromiumdir}/icudtl.dat
%endif
%{chromiumdir}/natives_blob.bin
%{chromiumdir}/v8_context_snapshot.bin
%{chromiumdir}/*.pak
%{chromiumdir}/xdg-mime
%{chromiumdir}/xdg-settings
%dir %{chromiumdir}/MEIPreload
%{chromiumdir}/MEIPreload/manifest.json
%{chromiumdir}/MEIPreload/preloaded_data.pb
%dir %{chromiumdir}/locales
%{chromiumdir}/locales/*.pak
%dir %{chromiumdir}/swiftshader
%{chromiumdir}/swiftshader/libEGL.so
%{chromiumdir}/swiftshader/libGLESv2.so
%{chromiumdir}/swiftshader/libvulkan.so
#########################################changelogs#################################################
%changelog
* Sat Sep 21 2019 Akarshan Biswas <akarshanbiswas@fedoraproject.org> - 77.0.3865.90-1
- Update to 77.0.3865.90
- Disabled Nvidia support
- Use the bundled python2 as python2 is going to be removed from Fedora

* Fri Aug 30 2019 Akarshan Biswas <akarshanbiswas@fedoraproject.org> - 76.0.3809.132-2
- Update to 76.0.3809.132

* Mon Aug 12 2019 Akarshan Biswas <akarshanbiswas@fedoraproject.org> - 76.0.3809.100-2
- Fix a bug which causes chromium to reject certificates by throwing ERR_CERTIFICATE_TRANSPARENCY_REQUIRED

* Sat Aug 10 2019 Akarshan Biswas <akarshanbiswas@fedoraproject.org> - 76.0.3809.100-1
- Update to 76.0.3809.100

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 75.0.3770.142-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Aug 03 2019 Akarshan Biswas <akarshanbiswas@fedoraproject.org> - 76.0.3809.87-1
- Update to 76.0.3809.87
- Use system ffmpeg and libvpx

* Wed Jul 17 2019 Akarshan Biswas <akarshanbiswas@fedoraproject.org> - 75.0.3770.142-1
- Update to 75.0.3770.142
- Removed Nvidia GPU video decode blacklist
- Add a patch to fix a bug around RenderProcessHost to avoid crash

* Wed Jul 03 2019 Akarshan Biswas <akarshanbiswas@fedoraproject.org> - 75.0.3770.100-2
- Fix vaapi regression on few intel devices, disabled vaapi post processing for Nvidia

* Wed Jun 19 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 75.0.3770.100-1
- Update to 75.0.3770.100

* Sat Jun 15 2019 Akarshan Biswas <akarshanbiswas@fedoraproject.org> 75.0.3770.90-1
- Update to 75.0.3770.90
- Re bundle icu; requires 64 and up
- Use system minizip again

* Wed Jun 12 2019 Akarshan Biswas <akarshanbiswas@fedoraproject.org> 75.0.3770.80-2
- Use %%autosetup and switch back to GCC (build fails on clang often which makes it non beneficial to GCC)
- Change recommends to libva-utils since acceleration is broken on few intel devices

* Sat Jun 08 2019 Akarshan Biswas <akarshanbiswas@fedoraproject.org> 75.0.3770.80-1
- Update to 75.0.3770.80

* Fri May 24 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 74.0.3729.169-1
- Update to 74.0.3729.169

* Thu May 16 2019 Akarshan Biswas <akarshanbiswas@fedoraproject.org> - 74.0.3729.157-1
- Update to 74.0.3729.157

* Sun May 05 2019 Akarshan Biswas <akarshanbiswas@fedoraproject.org> - 74.0.3729.131-1
- Update to 74.0.3729.131 and spec cleanup

* Thu Apr 25 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 74.0.3729.108-1
- Update to 74.0.3729.108
- Install missing MEIPreload component

* Fri Apr 05 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 73.0.3683.103-1
- Update to 73.0.3683.103

* Tue Apr 02 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 73.0.3683.86-3
- Revert switching to GNU ar and nm

* Tue Mar 26 2019 Akarshan Biswas <akarshanbiswas@fedoraproject.org> - 73.0.3683.86-2
- Switched to GNU ar and nm to work around a bug in the current llvm in f30 #rhbz 1685029
- Pipewire flag added to enable it by default on Fedora

* Fri Mar 22 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 73.0.3683.86-1
- Update to 73.0.3683.86

* Fri Mar 15 2019 Akarshan Biswas <akarshanbiswas@fedoraproject.org> 73.0.3683.75-2
- Enable pipewire support
- Added a patch from fedora to fix building with pipewire support
- Add a patch from upstream to stop vsync error spam when running on wayland
- Disable fedora compile flags and re enable gold on rawhide due to linker bugs

* Fri Mar 15 2019 Akarshan Biswas <akarshanbiswas@fedoraproject.org> 73.0.3683.75-1
- Update to 73.0.3683.75
- Update BuildRequires for ozone, libva; used pkgconfig instead


* Sun Mar 03 2019 Akarshan Biswas <akarshanbiswas@fedoraproject.org> 72.0.3626.121-1
- Updated to 72.0.3626.121
- spec cleanup

* Tue Feb 19 2019 Akarshan Biswas <akarshanbiswas@fedoraproject.org> 72.0.3626.109-1
- Update to 72.0.3626.109
- remove ozone patches

* Wed Feb 06 2019 Akarshan Biswas <akarshanbiswas@fedoraproject.org> 72.0.3626.81-2
- Rebundle icu for fedora 29 and fedora 28; Need icu version >= 63.1

* Tue Feb 05 2019 Akarshan Biswas <akarshanbiswas@fedoraproject.org> 72.0.3626.81-1
- Update to 72.0.3626.81
- Add a patch to fix missing includes in webrtc
- ozone updates (WIP)
- Fix gn where it now needs gold linker in bootstrap
- remove clang building implementation in this spec (out of scope)
- Make sure chromium uses the x11 GDK backend in wayland

* Fri Dec 21 2018 Akarshan Biswas <akarshan.biswas@hotmail.com> 71.0.3578.98-2
- Re enable the non effective enable_widevine flag

* Sat Dec 15 2018 Akarshan Biswas <akarshan.biswas@hotmail.com> 71.0.3578.98-1
- Update to 71.0.3578.98 

* Thu Dec 06 2018 Akarshan Biswas <akarshan.biswas@hotmail.com> 71.0.3578.80-1
- Update to 71.0.3578.80
- Add a patch to fix libva version mismatch error 
- Re bundle re2 as it's ancient on Fedora
- Enable experimental support for wayland-ozone in the spec file (WIP; disabled by default)
- Bring patch definitions closer to %%prep so to find and apply patches easier.

* Mon Nov 26 2018 Akarshan Biswas <akarshan.biswas@hotmail.com> 70.0.3538.110-1
- Update to 70.0.3538.110

* Thu Nov 15 2018 Akarshan Biswas <akarshan.biswas@hotmail.com> 70.0.3538.102-2
- Add a patch from upstream to remove sysroot-related options from gn bootstrap

* Wed Nov 14 2018 Akarshan Biswas <akarshan.biswas@hotmail.com> 70.0.3538.102-1
- Update to 70.0.3538.102

* Wed Nov 07 2018 Akarshan Biswas <akarshan.biswas@hotmail.com> 70.0.3538.77-4
- Replace %%autosetup with %%setup and fix spec file because applying condition on patch defines is wrong.

* Wed Nov 07 2018 Akarshan Biswas <akarshan.biswas@hotmail.com> 70.0.3538.77-3
- Add a patch to fix building on rawhide with harfbuzz2

* Tue Nov 06 2018 Akarshan Biswas <akarshan.biswas@hotmail.com> 70.0.3538.77-2
- Use correct branding in chromium
- update vaapi patch

* Fri Oct 26 2018 Akarshan Biswas <akarshan.biswas@hotmail.com> 70.0.3538.77-1
- Update to 70.0.3538.77
- Add a patch to fix building with system libicu

* Sun Oct 21 2018 Akarshan Biswas <akarshan.biswas@hotmail.com> 70.0.3538.67-2
- Reduce jumbo_file_merge_limit to a much lower number since rpmfusion koji can't keep up.

* Wed Oct 17 2018 Akarshan Biswas <akarshan.biswas@hotmail.com> 70.0.3538.67-1
- Update to 70.0.3538.67
- brand new vaapi patch 
- Add few patches to fix gcc
- turned on support for jumbo builds by default across all branches
- Added -fpermissive flag as requirement

* Fri Oct 12 2018 Akarshan Biswas <akarshan.biswas@hotmail.com> 69.0.3497.100-5
- turned of gold in rawhide as it crashes with fedora flags
- spec cleanup
- Minor appdata typo fix

* Thu Oct 11 2018 Akarshan Biswas <akarshan.biswas@hotmail.com> 69.0.3497.100-4
- Rebuild for new libva version on fedora 29+
- Use metainfodir for installing metadata

* Fri Sep 28 2018 Akarshan Biswas <akarshan.biswas@hotmail.com> 69.0.3497.100-3
- Remove dependency on minizip-compat package(https://bugzilla.redhat.com/show_bug.cgi?id=1632170)
- Add conditions to build with{out} system minizip

* Sat Sep 22 2018 Akarshan Biswas <akarshan.biswas@hotmail.com> 69.0.3497.100-2
- Produce an entire new package with unique appdata 
- Use desktop and default app template from the source
- enable debug builds
- Update chromium wrapper
- Remove dependent on unrar

* Tue Sep 18 2018 Akarshan Biswas <akarshan.biswas@hotmail.com> 69.0.3497.100-1
- Updated chromium to 69.0.3497.100.
- Enabled fedora GCC build flags and removed those flags which can cause confict with chromium's gyp flags.
- Removed some duplicate flags and added g1 to ease memory which building.

* Thu Sep 13 2018 Akarshan Biswas <akarshan.biswas@hotmail.com> 69.0.3497.92-1
- updated chromium to 69.0.3497.92
- fixed vaapi patch
- Moved appstream validation to check

* Thu Sep 06 2018 Akarshan Biswas <akarshan.biswas@hotmail.com> 69.0.3497.81-1
- updated chromium to 69.0.3497.81
- removed useless requirements
- turned on verbose
- removed conditions on obsolete fedora releases
- fixed fedora compilation flags

* Wed Aug 29 2018 Akarshan Biswas <akarshan.biswas@hotmail.com> 68.0.3440.106-1
- Deleted provides and excludes and added conflict


