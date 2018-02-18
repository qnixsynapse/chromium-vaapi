# Chromium-vaapi
Chromium browser for Fedora Linux with video acceleration patches.
***THIS IS NOT AN OFFICIAL FEDORA BUILD******



****ONLY FOR TESTING****

Patches are taken from various sources. I thank them for the contribution. 

Chromium browser with hardware video decoding will not only increase the battery by minimising the power consumption but also enable 4k video on weak platforms  (If supported).


installing this build requires vaapi driver to be installed in the system.
check with vainfo.
The hardware video decoding with this patch is still disabled. enable it in chrome://flags/#enable-accelerated-video
Check cpu usages in both enabled and disabled state.


AMD GPU provides both vaapi and vdpau. If vainfo gives an error try "export LIBVA_DRIVER_NAME=[codename of your amd gpu(radeonsi,etc)without brackets}

Nvidia user install libva-vdpau-driver

Intel GPU:libva-intel-driver



Build system is provided by travis-ci.org and docker for Fedora image build environment is by alectolytic/rpmbuilder
