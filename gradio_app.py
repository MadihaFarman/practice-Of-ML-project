import numpy as np
import pandas as pd
import gradio as gr

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# ---------- Gradio Integration ----------
def gradio_predict(gender, ethnicity, parental_level_of_education, lunch, test_preparation_course, reading_score, writing_score):
    data = CustomData(
        gender=gender,
        race_ethnicity=ethnicity,
        parental_level_of_education=parental_level_of_education,
        lunch=lunch,
        test_preparation_course=test_preparation_course,
        reading_score=float(reading_score),
        writing_score=float(writing_score)
    )
    pred_df = data.get_data_as_data_frame()
    predict_pipeline = PredictPipeline()
    results = predict_pipeline.predict(pred_df)
    return f"Predicted Result: {results[0]}"


gradio_interface = gr.Interface(
    fn=gradio_predict,
    inputs=[
        gr.Dropdown(["male", "female"], label="Gender"),
        gr.Dropdown(["group A", "group B", "group C", "group D", "group E"], label="Ethnicity"),
        gr.Dropdown(["associate's degree","bachelor's degree","high school","master's degree","some college","some high school"],label="Parental Level of Education"),
        gr.Dropdown(["standard", "free/reduced"], label="Lunch"),
        gr.Dropdown(["none", "completed"], label="Test Preparation Course"),
        gr.Number(label="Reading Score"),
        gr.Number(label="Writing Score"),
    ],
    outputs="text",
    title="Student Performance Predictor"
)


if __name__ == "__main__":

   gradio_interface.launch()
