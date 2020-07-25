# SPDX-License-Identifier: GPL-3.0

import json
import xbmc


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

    def is_master(self):
        req = {"jsonrpc": "2.0", "method": "XBMC.GetInfoBooleans", "params": {"booleans": ["System.IsMaster"]}, "id": 1}
        req_data = json.dumps(req)
        res_data = xbmc.executeJSONRPC(req_data)
        res = json.loads(res_data)
        return res["result"]["System.IsMaster"]

    def engage_master_lock(self):
        if self.is_master():
            xbmc.log("[MasterLock] Master Lock was disengaged. Engaging.")
            xbmc.executebuiltin("Mastermode")
