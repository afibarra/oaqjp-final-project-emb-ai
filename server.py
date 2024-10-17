""" Module which handles Requests to the Emotion Detector """

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    """ Handles Requests to the Root Page """

    return render_template('index.html')

@app.route("/emotionDetector")
def sent_to_detector():
    """ Handles Requests to the Emotion Detector """

    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "<b>Invalid text! Please try again!</b>"

    return f"""
            For the given statement, the system response is 'anger': 
            {response['anger']},
            'disgust': {response['disgust']},
            'fear': {response['fear']},
            'joy': {response['joy']}
            and 'sadness': {response['sadness']}.
            The dominant emotion is <b>{response['dominant_emotion']}</b>.
        """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
