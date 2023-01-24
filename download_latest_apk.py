APP_ID = "com.YostarJP.BlueArchive"

import logging
# set up logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s.%(funcName)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

from urllib.request import urlopen, Request
from urllib.parse import urlencode
import json

def download_raw_QooApp_apk(package_id: str) -> bytes:

    query = urlencode(
        {
            "supported_abis": "x86,armeabi-v7a,armeabi",
            "sdk_version": "22",
        }
    )
    res = urlopen(
        Request(
            url=f"https://api.qoo-app.com/v6/apps/{package_id}/download?{query}",
            headers={
                "accept-encoding": "gzip",
                "user-agent": "QooApp 8.1.7",
                "device-id": "80e65e35094bedcc",
            },
            method="GET",
        )
    )
    data = urlopen(res.url).read()
    return data

def download_ba_apk():
    logging.info("downloading latest apk from QooApp")
    apk_data = download_raw_QooApp_apk(APP_ID)
    version = None
    VERSION_MAGIC_PREFIX_BYTES = b'\x01\x01\x01\x01\x01\x00\x00\x00\x0B\x00\x00\x00'

    from zipfile import ZipFile
    import io
    with io.BytesIO(apk_data) as stream:
        with ZipFile(stream) as zip:
            # devs are dumb shit and keep moving the app version around
            with zip.open("assets/bin/Data/globalgamemanagers", "r") as f:
                data = f.read()
                version_prefix_pos = data.find(VERSION_MAGIC_PREFIX_BYTES)
                version_pos = version_prefix_pos + len(VERSION_MAGIC_PREFIX_BYTES)
                # 1.26.183658
                version_length = len('x.xx.xxxxxx')
                version = data[version_pos:version_pos + version_length].decode('utf-8')
                print('Downloaded version:', version)
                UNITY_VERSION_START_POS = 0x30
                # read till 0x00
                unity_version = data[UNITY_VERSION_START_POS:data.find(b'\x00', UNITY_VERSION_START_POS)].decode('utf-8')
                print('Unity version used:', unity_version)
    
    return version, apk_data

def get_latest_version() -> str:
    logging.info('fetching lastest version from yostar server')
    url = 'https://prod-noticeindex.bluearchiveyostar.com/prod/index.json'
    res = urlopen(
        Request(
            url=url,
            method="GET",
        )
    )
    return json.load(urlopen(res.url))['LatestClientVersion']

online_latest_version = get_latest_version()
logging.info(f'Online version: {online_latest_version}')
version, raw_apk_data = download_ba_apk()
with open(f"{APP_ID}-{version if version else 'current'}.apk", "wb") as f:
    f.write(raw_apk_data)

if version != online_latest_version:
    logging.warning('version mismatch')

