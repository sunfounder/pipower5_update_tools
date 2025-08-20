PiPower5_Globals = {
    # Global variables
    "NAME": "PiPower5",

    # i2c addr
    "APP_I2C_ADDR": 0x5c,
    "BOOT_I2C_ADDR": 0x5d,

    # Board and version register addresses
    # ENDIAN = 'big'
    "BOARD_ID_REG_ADDR": 140,  # 140: id_h, 141: id_l; PiPower 5: 2602
    "APP_VERSION_REG_ADDR": 128,  # 128: major, 129: minor, 130: patch
    "BOOT_VERSION_REG_ADDR": 173,  # 173: major, 174: minor, 175: patch
    "FACTORY_VERSION_REG_ADDR": 176,  # 176: major, 177: minor, 178: patch
    "MIAN_ENTRY_REG_ADDR": 183,  # 183~186: bit3 ~ bit0

    # Boot mode register addresses
    # ENDIAN = 'big'
    "BOOT_VERSION_REG_ADDR_BOOT": 0,
    "FACTORY_VERSION_REG_ADDR_BOOT": 3,
    "APP_VERSION_REG_ADDR_BOOT": 6,
    "BOOT_MODE_BOOT": 9,
    "MIAN_ENTRY_REG_ADDR_BOOT": 10,

    # Application modes
    "FACTORY_APP_MODE": 0,
    "NEW_APP_MODE": 1,
    "UPGRADE_MODE": 2,

    # Application start address
    "NEW_APP_START": 0x08007800,

    # Firmware configuration
    "FIRMWARE_MAX_BYTES": 24 * 1024,  # 24K
}
