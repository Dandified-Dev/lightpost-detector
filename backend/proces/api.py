from ninja import NinjaAPI, File, UploadedFile
from django.http import HttpResponse
import supervision as sv
from PIL import Image
from io import BytesIO
import requests
from ultralytics import YOLO
import cv2
import numpy as np

model = YOLO("./weights.pt")
app = NinjaAPI()

@app.post("/process-image")
def process_image(request, image: UploadedFile = File(...), confidence: float = 0.6):
    print(f"Received image: {image.name}, confidence: {confidence}")
    # 1 — Load image
    file_bytes = image.read()
    image = cv2.imdecode(np.frombuffer(file_bytes, np.uint8), cv2.IMREAD_COLOR)

    # 2 — Run inference
    results = model(image, conf=confidence)[0]

    # 3 — Convert to supervision detections
    detections = sv.Detections.from_ultralytics(results)

    # 4 — Annotate
    annotator = sv.BoxAnnotator()
    annotated = annotator.annotate(
        scene=image.copy(),
        detections=detections
    )

    # 5 — Encode image as JPEG
    success, buffer = cv2.imencode(".jpg", annotated)
    if not success:
        return HttpResponse("Image encoding failed", status=500)

    # 6 — Return the image
    return HttpResponse(
        buffer.tobytes(),
        content_type="image/jpeg",
    )
