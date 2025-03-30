import configparser

from loguru import logger

from sdk import WxPusherNotifier, WXReadSDK

if __name__ == "__main__":
    CURL_PATH = "./curl_config.sh"
    CONFIG_PATH = "config.ini"
    READ_NUM = 30
    RESIDENCE_TIME = 60  # 单位秒

    config = configparser.ConfigParser()
    config.read(CONFIG_PATH)
    WXPUSHER_SPT = config.get("WXPUSHER", "SPT")

    pusher = WxPusherNotifier(WXPUSHER_SPT)
    wx = WXReadSDK.from_curl_bash(CURL_PATH)

    def onFail(msg):
        logger.error(msg)
        raise Exception(msg)

    def onFinish(msg):
        logger.info(msg)
        # pusher.push(msg)

    wx.run(
        loop_num=READ_NUM,
        residence_second=RESIDENCE_TIME,
        onFail=onFail,
        onFinish=onFinish,
    )
