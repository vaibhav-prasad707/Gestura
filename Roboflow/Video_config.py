from roboflow import Roboflow

rf = Roboflow(api_key="mKSJxFwXpoBkwjqItleo")
project = rf.workspace().project("sign-lang-classification")
model = project.version("1").model

job_id, signed_url, expire_time = model.predict_video(
    "Roboflow\WIN_20250204_04_58_54_Pro.mp4",
    fps=5,
    prediction_type="batch-video",
)

results = model.poll_until_video_results(job_id)

print(results)