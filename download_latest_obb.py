from typing import Any, Dict, List, Optional
import os
import logging
import binascii

import requests
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s.%(funcName)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class QooAppStore():
    VERSION_STR = '8.1.6'
    VERSION_CODE = 316

    device_id: str
    token: str
    logger: logging.Logger

    def __init__(self, device_id: Optional[str] = None, token: Optional[str] = None):
        if not device_id:
            device_id = self.generate_device_id()
        self.device_id = device_id
        self.logger = logging.getLogger(f'{self.__class__}.{self.device_id}')
        self.logger.info(f'Initializing QooAppStore with device_id {self.device_id}')
        if not token:
            token = self.generate_token()
        self.token = token
        self.logger.info(f'Initialized QooAppStore with token {self.token}')

    @staticmethod
    def generate_device_id() -> str:
        return binascii.b2a_hex(os.urandom(8)).decode()

    def build_headers(self) -> Dict[str, str]:
        return {
            'User-Agent': f'QooApp {self.VERSION_STR}',
            'Device-Id': self.device_id
        }

    def generate_token(self) -> str:
        url = 'https://api.qoo-app.com/v6/users'
        query_params = {
            'version_code': self.VERSION_CODE,
        }
        data_params = {
            'device_id': self.device_id,
            'platform_access_token': self.device_id,
            'type': 4,
            'email': 'null',
            'version_code': self.VERSION_CODE
        }
        self.logger.info(f'Requesting QooAppStore token...')
        token_resp = requests.post(url, params=query_params, data=data_params, headers=self.build_headers())
        if token_resp.status_code >= 400:
            raise Exception(f'Unable to generate QooApp token: {token_resp}')
        token = token_resp.json()['token']
        self.logger.info(f'Get QooAppStore token: {token}')
        return token

    def get_app_info(self, package_name: str, sdk_version: int, available_abi: List[str]):
        url = f'https://api.qoo-app.com/v10/apps/{package_name}'
        query_params = {
            'supported_abis': ','.join(available_abi),
            'sdk_version': sdk_version,
            'version_code': self.VERSION_CODE,
        }
        headers = {
            'X-User-Token': self.token,
            **self.build_headers()
        }
        info_resp = requests.get(url, params=query_params, headers=headers)
        if info_resp.status_code >= 400:
            raise Exception(f'Unable to get info for {package_name}: {info_resp}')

        if 'data' not in info_resp.json():
            raise Exception(f'Unable to get info for {package_name}: {info_resp}')

        data = info_resp.json()['data']

        return data


qas = QooAppStore()
app_info = qas.get_app_info('com.YostarJP.BlueArchive', 22, ['arm64-v8a'])
apk_info = app_info['apk']
qoo_app_id = app_info['id']
version_code = apk_info['version_code']

obb_filename = f'main.{version_code}.com.YostarJP.BlueArchive.obb'
obb_link = f'https://d.qoo-apk.com/{qoo_app_id}/obb/{obb_filename}'

logger.info(f'Downloading OBB file from {obb_link} to {obb_filename}')

r = requests.get(obb_link, headers=qas.build_headers())
with open(obb_filename, 'wb') as f:
    f.write(r.content)

logger.info(f'Script finished. OBB file saved to {obb_filename}')
