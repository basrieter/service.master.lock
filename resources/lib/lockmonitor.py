# SPDX-License-Identifier: GPL-3.0

import xbmc
import xbmcaddon


class LockMonitor(xbmc.Monitor):
    # noinspection PyUnusedLocal
    def __init__(self, *args, **kwargs):
        super(LockMonitor, self).__init__()
        xbmc.log("[MasterLock] Master Lock monitor started")

    # noinspection PyPep8Naming
    def onScreensaverActivated(self):
        self.engage_master_lock()

    # noinspection PyPep8Naming
    def onDPMSActivated(self):
        self.engage_master_lock()

    def engage_master_lock(self):
        if xbmc.getCondVisibility("System.IsMaster"):
            xbmc.log("[MasterLock] Master Lock was disengaged. Engaging.")
            xbmc.executebuiltin("Mastermode")
            go_home = xbmcaddon.Addon().getSettingBool("navigate_home")
            if go_home:
                xbmc.executebuiltin("ActivateWindow(home)")
