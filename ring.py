import os
from ring_doorbell import Ring, Auth
from oauthlib.oauth2 import MissingTokenError

cache_file = "token.cache"

def token_updated(token):
    with open(cache_file, "w") as f:
        f.write(json.dumps(token))

def otp_callback():
    auth_code = input("2FA code: ")
    return auth_code

def main():
    if os.path.isfile(cache_file):
        with open(cache_file) as f:
            token = json.load(f)
    else:
        token = None

    auth = Auth("MyProject/1.0", token, token_updated)

    try:
        auth.fetch_token()
    except MissingTokenError:
        auth.fetch_token(otp_callback())

    ring = Ring(auth)
    ring.update_data()

    devices = ring.devices()
    for device in devices['doorbots']:
        print('Doorbot name: {}'.format(device.name))
        print('Battery: {}'.format(device.battery_life))
        print('Wifi: {}'.format(device.wifi_signal_strength))

if __name__ == "__main__":
    main()