# Chromium-vaapi
Chromium browser for Fedora Linux with video acceleration patches.

## THIS IS NOT AN OFFICIAL FEDORA BUILD

### THIS IS FOR TESTING PURPOSES ONLY [ STABLE ]

To watch DRM videos, download chrome rpm from http://www.google.com/chrome , extract it and copy the libwidevinecdm.so to /usr/share/chromium-browser

Patches are taken from various sources. I thank them for the contribution.

Chromium browser with hardware video decoding will not only increase the battery by minimising the power consumption but also enable 4K video ( if supported ) on weaker systems.

Installing this build requires vaapi driver to be installed on the system. check with vainfo. The hardware video decoding with this patch is still disabled, enable it  using this [flag](chrome://flags/#enable-accelerated-video). Compare CPU usages of both enabled and disabled state.

AMD GPU provides both vaapi and vdpau.

If vainfo gives an error try `export LIBVA_DRIVER_NAME="[codename of your amd gpu (radeonsi,etc) without brackets]"`

# AMD GPU users are effected by this [bug](https://bugs.chromium.org/p/chromium/issues/detail?id=719213)

## Required drivers according to respective GPUs: 

- Nvidia: libva-vdpau-driver

- Intel:  libva-intel-hybrid-driver

The copr build doesn't include proprietary codecs like h264. In order to fully test vaapi capabilities install chromium from [Github releases](https://github.com/biswasab/Chromium-vaapi/releases) tab on this repo. 
This package might cause conflicts with similar packages on the system.

From version [66.0.3359.139](https://github.com/biswasab/Chromium-vaapi/tree/66.0.3359.139) onwards, builds will be done with clang only. If you wish build with gcc, you can build it by setting the value of `%global clang` to 0 in [spec file](https://github.com/biswasab/Chromium-vaapi/blob/master/chromium.spec).
