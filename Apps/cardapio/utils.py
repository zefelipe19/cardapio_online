from io import BytesIO
import base64
import qrcode

from django.urls import reverse_lazy


def gerate_qr_code(request, slug):
    absolute_url = str(request.build_absolute_uri()).replace("/adm", "/")
    print(absolute_url)

    img = qrcode.make(absolute_url)
    buffer = BytesIO()
    img.save(buffer, format='PNG')
    buffer.seek(0)

    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('/n', '')
    image_data = f"data:image/png;base64, {image_base64}"

    return image_data