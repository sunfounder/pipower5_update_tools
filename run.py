from i2c_iap_tool.app import IapToolApp
from globals.pipower5_globals import PiPower5_Globals

if __name__ == '__main__':
    app = IapToolApp(globals=PiPower5_Globals)
    app.run()