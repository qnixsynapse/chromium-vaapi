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
#Global Libraries
#Do not turn it on in Fedora copr!
%global freeworld 1
#This can be any folder on out
%global target out/Release
#Our installation folder
%global chromiumdir %{_libdir}/chromium-vaapi
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
# Require harfbuzz >= 1.5.0 for hb_glyph_info_t
%if 0%{?fedora} >= 28
%bcond_without system_harfbuzz
%else
%bcond_with system_harfbuzz
%endif
# Require libxml2 > 2.9.4 for XML_PARSE_NOXXE
%bcond_without system_libxml2

# https://github.com/dabeaz/ply/issues/66
%bcond_without system_ply

# Allow testing whether icu can be unbundled
%bcond_with system_libicu
# Allow testing whether libvpx can be unbundled
%bcond_with system_libvpx
#Allow minizip to be unbundled
#mini-compat is going to be removed from fedora 30!
%if 0%{?fedora} >= 30
%bcond_with system_minizip
%else
%bcond_without system_minizip
%endif
#Turn on verbose mode
%global debug_logs 1
#Build debug packages for debugging
%global debug_pkg 1
# Allow compiling with clang
%global clang 0
#Allow building with Fedora compilation flags
%global fedora_compilation_flags 1
##############################Package Definitions######################################
Name:       chromium-vaapi
Version:    69.0.3497.100
Release:    3%{?dist}
Summary:    A Chromium web browser with video decoding acceleration
License:    BSD and LGPLv2+ and ASL 2.0 and IJG and MIT and GPLv2+ and ISC and OpenSSL and (MPLv1.1 or GPLv2 or LGPLv2)
URL:        https://www.chromium.org/Home
%if %{freeworld}
Source0:    https://commondatastorage.googleapis.com/chromium-browser-official/chromium-%{version}.tar.xz
%else
Source0:    chromium-%{version}-clean.tar.xz
%endif
# The following two source files are copied and modified from the chromium source
Source10:   %{name}.sh
#Add our own appdata file. ##TODO
Source11:   %{name}.appdata.xml
#Personal stuff
Source15:   LICENSE
#Video acceleration patch from https://chromium-review.googlesource.com/c/chromium/src/+/532294
Patch1:    vaapi.patch
Patch2:    widevine.patch
%if %{clang}
#Will use any clang patch here
#Fix breaking builds caused by gcc_ar_wrapper.py from upstream
Patch7: llvm-arflags.patch
%else
#Gcc patches area.
%endif
#More patches to fix chromium build here
#remove dependency on unrar. That's a nasty code.
Patch50:    unrar.patch
#Bootstrap still uses python command
Patch51:    py2-bootstrap.patch
#This build should be only available to amd64
ExclusiveArch: x86_64
########################################################################################
#Compiler settings
%if %{clang}	
BuildRequires: clang, llvm, lld
%else 
#GCC mode on
# Make sure we don't encounter any bug
BuildRequires: gcc 
BuildRequires: gcc-c++
%endif
# Basic tools and libraries needed for building
BuildRequires: ninja-build, nodejs, bison, gperf, hwdata
BuildRequires: libgcc, glibc, libatomic, libstdc++-static
BuildRequires: libcap-devel, cups-devel, alsa-lib-devel
BuildRequires: mesa-libGL-devel, mesa-libEGL-devel
%if %{with system_minizip}
BuildRequires:	minizip-devel
%endif
BuildRequires: pkgconfig(gtk+-2.0), pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(libexif), pkgconfig(nss)
BuildRequires: pkgconfig(xtst), pkgconfig(xscrnsaver)
BuildRequires: pkgconfig(dbus-1), pkgconfig(libudev)
BuildRequires: pkgconfig(gnome-keyring-1)
BuildRequires: pkgconfig(libffi)
# remove_bundled_libraries.py --do-remove
BuildRequires: python2-rpm-macros
BuildRequires: python2-beautifulsoup4
BuildRequires: python2-html5lib
BuildRequires: python2-markupsafe
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
BuildRequires: pciutils-devel
BuildRequires: speech-dispatcher-devel
BuildRequires: pulseaudio-libs-devel
# install desktop files
BuildRequires: desktop-file-utils
# install AppData files
BuildRequires: libappstream-glib
#for vaapi
BuildRequires:	libva-devel
#Runtime Requirements
Requires:         hicolor-icon-theme
#Some recommendations
Recommends:    libva-intel-hybrid-driver%{?_isa}
Recommends:    libva-intel-driver%{?_isa}
%if !%{debug_pkg}
%global debug_package %{nil}
%endif
%description
chromium-vaapi is an open-source web browser, powered by WebKit (Blink)
############################################PREP###########################################################
%prep
%autosetup -n chromium-%{version} -p1
#Let's change the default shebang of python files.
find -depth -type f -name "*.py" -exec sed -iE '1s=^#! */usr/bin/\(python\|env python\)[23]\?=#!%{__python2}=' {} +
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
    net/third_party/http2 \
    net/third_party/mozilla_security_manager \
    net/third_party/nss \
    net/third_party/quic \
    net/third_party/spdy \
    third_party/abseil-cpp \
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
    third_party/angle/third_party/vulkan-headers \
    third_party/angle/third_party/vulkan-loader \
    third_party/angle/third_party/vulkan-tools \
    third_party/angle/third_party/vulkan-validation-layers \
    third_party/apple_apsl \
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
    third_party/crashpad \
    third_party/crashpad/crashpad/third_party/zlib \
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
    third_party/jinja2 \
    third_party/jstemplate \
    third_party/khronos \
    third_party/leveldatabase \
    third_party/libaddressinput \
    third_party/libaom \
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
    third_party/mesa \
    third_party/metrics_proto \
%if !%{with system_minizip}
    third_party/minizip/ \
%endif
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
    third_party/perfetto \
%if !%{with system_ply}
    third_party/ply \
%endif
    third_party/polymer \
    third_party/protobuf \
    third_party/protobuf/third_party/six \
    third_party/pyjson5 \
    third_party/qcms \
    third_party/rnnoise \
    third_party/s2cellid \
    third_party/sfntly \
    third_party/skia \
    third_party/skia/third_party/gif \
    third_party/skia/third_party/vulkan \
    third_party/skia/third_party/skcms \
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
%if !%{with system_minizip}
    third_party/zlib \
%endif
    tools/gn/base/third_party/icu \
    url/third_party/mozilla \
    v8/third_party/antlr4 \
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
%if %{with system_minizip}
    zlib
%endif
    

sed -i 's|//third_party/usb_ids|/usr/share/hwdata|g' device/usb/BUILD.gn
%if %{clang}
# Remove compiler flags not supported by our system clang
  sed -i \
    -e '/"-Wno-ignored-pragma-optimize"/d' \
    build/config/compiler/BUILD.gn
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
sed -i.orig -e 's/getenv("CHROME_VERSION_EXTRA")/"Chromium(vaapi) Fedora Project"/' $FILE
#####################################BUILD#############################################
%build
#export compilar variables
%if %{clang}
export AR=llvm-ar NM=llvm-nm
export CC=clang CXX=clang++
%else
export AR=ar NM=nm
export CC=gcc CXX=g++
%if %{fedora_compilation_flags}
#Build falgs to make hardened binaries
#Remove some flags which can create conflicts with chromium gyp flags. 
export CFLAGS="$(echo '%{__global_cflags}' |sed -e 's/-fexceptions//' \
                                                -e 's/-Werror=format-security//' \
                                                -e 's/-pipe//' \
                                                -e 's/-g/-g1/g' \
                                                -e 's/-g1record-g1cc-switches//' )"
export CXXFLAGS="$(echo '%{?__global_cxxflags}%{!?__global_cxxflags:%{__global_cflags}}' | sed -e 's/-fexceptions//' \
                                                                                               -e 's/-Werror=format-security//' \
                                                                                               -e 's/-pipe//' \
                                                                                               -e 's/-g/-g1/g' \
                                                                                               -e 's/-g1record-g1cc-switches//' )"

export LDFLAGS='%{__global_ldflags}'
%else
export CXXFLAGS=$CXXFLAGS" -fno-delete-null-pointer-checks"
%endif
%endif
gn_args=(
    is_debug=false
    use_vaapi=true
    use_gtk3=true
    enable_swiftshader=false
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
    remove_webcore_debug_symbols=true
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
    'clang_base_path = "/usr"'
    clang_use_chrome_plugins=false
%else
    is_clang=false
    use_lld=false
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
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_datadir}/metainfo
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/gnome-control-center/default-apps
sed -e "s|@@CHROMIUMDIR@@|%{chromiumdir}|" -e "s|@@BUILDTARGET@@|`cat /etc/redhat-release`|" \
    %{SOURCE10} > chromium-vaapi.sh
install -m 755 chromium-vaapi.sh %{buildroot}%{_bindir}/%{name}
install -m 644 %{SOURCE11} %{buildroot}%{_datadir}/metainfo
sed -e "s|@@MENUNAME@@|%{name}|g" -e "s|@@PACKAGE@@|%{name}|g" \
    chrome/app/resources/manpage.1.in > chrome.1
install -m 644 chrome.1 %{buildroot}%{_mandir}/man1/%{name}.1
#Using the template from the source. Still doesn't help in fixing.
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
for i in 16 32; do
    mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps
    install -m 644 chrome/app/theme/default_100_percent/chromium/product_logo_$i.png \
        %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/%{name}.png
done
for i in 22 24 32 48 64 128 256; do
    if [ ${i} = 32 ]; then ext=xpm; else ext=png; fi
    if [ ${i} = 32 ]; then dir=linux/; else dir=; fi
    mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps
    install -m 644 chrome/app/theme/chromium/${dir}product_logo_$i.${ext} \
        %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/%{name}.${ext}
done
####################################check##################################################
%check
appstream-util validate-relax --nonet "%{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml"
######################################files################################################
%files
%license LICENSE
%doc AUTHORS 
%{_bindir}/chromium-vaapi
%{_datadir}/metainfo/chromium-vaapi.appdata.xml
%{_datadir}/applications/chromium-vaapi.desktop
%{_datadir}/gnome-control-center/default-apps/chromium-vaapi.xml
%{_datadir}/icons/hicolor/16x16/apps/chromium-vaapi.png
%{_datadir}/icons/hicolor/22x22/apps/chromium-vaapi.png
%{_datadir}/icons/hicolor/24x24/apps/chromium-vaapi.png
%{_datadir}/icons/hicolor/32x32/apps/chromium-vaapi.png
%{_datadir}/icons/hicolor/32x32/apps/chromium-vaapi.xpm
%{_datadir}/icons/hicolor/48x48/apps/chromium-vaapi.png
%{_datadir}/icons/hicolor/64x64/apps/chromium-vaapi.png
%{_datadir}/icons/hicolor/128x128/apps/chromium-vaapi.png
%{_datadir}/icons/hicolor/256x256/apps/chromium-vaapi.png
%{_mandir}/man1/chromium-vaapi.1.gz
%dir %{chromiumdir}
%{chromiumdir}/chromium-vaapi
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
%dir %{chromiumdir}/locales
%{chromiumdir}/locales/*.pak
#########################################changelogs#################################################
%changelog
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
