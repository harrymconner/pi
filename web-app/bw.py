import os

import dotenv
from bitwarden_sdk import BitwardenClient, DeviceType, client_settings_from_dict

dotenv.load_dotenv()

BITWARDEN_ACCESS_TOKEN = os.environ["BITWARDEN_ACCESS_TOKEN"]
API_URL = os.environ["API_URL"]
IDENTITY_URL = os.environ["IDENTITY_URL"]


def get_secret(secret_uuid: str) -> str:
    settings = client_settings_from_dict(
        {
            "apiUrl": API_URL,
            "deviceType": DeviceType.SDK,
            "identityUrl": IDENTITY_URL,
            "userAgent": "Python",
        }
    )
    client = BitwardenClient(settings)

    client.auth().login_access_token(BITWARDEN_ACCESS_TOKEN)

    try:
        secret_data = client.secrets().get(secret_uuid).data
    except Exception as e:
        raise e

    if not secret_data:
        msg = "This error will never be reached. Secret values will never be None."
        raise Exception(msg)

    return secret_data.value
