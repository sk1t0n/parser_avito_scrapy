def get_uri(url: str, params: dict) -> str:
    params = '&'.join(
        [f"{k}={str(v).replace(' ', '+')}" for k, v in params.items()])
    uri = f'{url}{params}'
    return uri
