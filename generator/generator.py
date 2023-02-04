import qrcode
from io import BytesIO
import base64
from models.qr_code import QRcode


def generate(data, user):
    image = qrcode.make(data)
    buffer = BytesIO()
    image.save(buffer, format='png')

    inf = base64.b64encode(buffer.getvalue())

    qr = QRcode(qr_code=inf, owner=user)
    return qr