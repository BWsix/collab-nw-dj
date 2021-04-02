import json, base64, io

from django.shortcuts import render, resolve_url
from django.views import View
from django.http import JsonResponse

from PIL import Image
import numpy as np

from .models.model import predict_number as img_to_number

class HomeView(View):
  def get(self, req):
    return render(req, 'home.html')

class ApiView(View):
  def post(self, req):
    body_unicode = req.body.decode('utf-8')
    body = json.loads(body_unicode)

    img_64 = body['dataUrl'].split('base64,')[1]
    img_raw = base64.b64decode(img_64)

    stream = io.BytesIO(img_raw)

    img = Image.open(stream)
    img = img.resize((28, 28))

    # img.save('tester.png')

    img_np = np.array(img)
    img_np = (img_np[:,:,3]/255).flatten()

    result = img_to_number(img_np).flatten()
    result = list(map(float, result))

    max_opp = result.index(max(result))

    data = {
      'result': result,
      'max_opp': max_opp,
    }

    return JsonResponse(data)
