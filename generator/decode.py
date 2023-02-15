def decode(user_data: list) -> list:
    result = []
    for data in user_data[0].qr_codes:
        qr = data.qr_code
        info = f'data:image/png;base64,{qr.decode("UTF-8")}'
        result.append(info)
    return result