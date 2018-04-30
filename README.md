# Chromium-vaapi
Chromium browser for Fedora Linux with video acceleration patches.
Installation Instructions
THIS IS NOT AN OFFICIAL FEDORA BUILD***

ONLY FOR TESTING[Stable ]

To watch DRM videos, download chrome rpm from http://www.google.com/chrome , extract it and copy the libwidevinecdm.so to /usr/share/chromium-browser

Patches are taken from various sources. I thank them for the contribution.

Chromium browser with hardware video decoding will not only increase the battery by minimising the power consumption but also enable 4k video on weak platforms (If supported).

installing this build requires vaapi driver to be installed in the system. check with vainfo. The hardware video decoding with this patch is still disabled. enable it in chrome://flags/#enable-accelerated-video Check cpu usages in both enabled and disabled state.

AMD GPU provides both vaapi and vdpau.
If vainfo gives an error try "export LIBVA_DRIVER_NAME=[codename of your amd gpu(radeonsi,etc)without brackets} 
#AMDGPU users are effected by this bug : https://bugs.chromium.org/p/chromium/issues/detail?id=719213

Nvidia user install libva-vdpau-driver

Intel GPU:libva-intel-hybrid-driver

The copr build doesn't include proprietary codecs like h264. In order to fully test vaapi capabilities install chromium from Github release tab on this repo. 
This package might cause conflicts with similar packages on the system.

From now Added clang support to build chromium with the help of clang instead of gcc. A lot less patching requires and less binary size. Build significantly faster too.
