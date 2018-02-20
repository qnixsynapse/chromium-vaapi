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

**NOTE: AMDGPU users are hit with a nasty bug for a long time. It's is merged(hopfully). Still I have added a fix but it seems GPU process fails to initialize sometimes. Best is to restart the browser or enable ignore-gpu-blacklist flag in chrome://flags
https://bugs.chromium.org/p/chromium/issues/detail?id=719213. The patch "amdgpu-fix.patch" once their fix lands into stable builds.

#TODO: Get acurate video parameters(Hopefully in f28 when libva2 is released!)

Nvidia user install libva-vdpau-driver

Intel GPU:libva-intel-driver



Ascended to fedora copr:https://copr.fedorainfracloud.org/coprs/hellbangerkarna/Chromium-Vaapi/
