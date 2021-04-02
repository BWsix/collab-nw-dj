import json, base64, io

from django.shortcuts import render
from django.views import View
from django.http import JsonResponse

from PIL import Image
import numpy as np

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
    print(img_np)
    # result = img_to_number(img_np)

    data = {
      'result': 'some output number'
    }

    return JsonResponse(data)
