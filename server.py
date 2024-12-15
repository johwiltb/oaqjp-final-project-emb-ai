"""
Provides an emotional detection thingy
"""
from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector
app = Flask('Emotion Detector App')
@app.route('/')
def hello():
    """Catch the initial one"""
    return render_template('index.html')
@app.route('/emotionDetector')
def emotion_detector_route():
    """Handle all the requests"""
    text_to_analyze = request.args['textToAnalyze']

    if not text_to_analyze:
        return jsonify({'error': 'No text provided'}), 400

    emotions = emotion_detector(text_to_analyze)

    if emotions['dominant_emotion'] is None:
        return jsonify({'error': 'Invalid text! Please try again!'}), 400

    response = {
        "anger": emotions['anger'],
        "disgust": emotions['disgust'],
        "fear": emotions['fear'],
        "joy": emotions['joy'],
        "sadness": emotions['sadness'],
        "dominant_emotion": emotions['dominant_emotion']
    }

    output_message = (f"For the given statement, the system response is "
                      f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
                      f"'fear': {response['fear']}, 'joy': {response['joy']}, "
                      f"'sadness': {response['sadness']}. The dominant emotion is "
                      f"<b>{response['dominant_emotion']}</b>.")

    return jsonify(output_message)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
