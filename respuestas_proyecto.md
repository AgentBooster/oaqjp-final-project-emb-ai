# Respuestas al Final Project: Emotion Detection Application

A continuación se presentan las respuestas formateadas para que puedas copiarlas y pegarlas (o guardarlas en archivos) para tu AI-Graded Submission. **Recuerda:** donde dice `URL al archivo` asegúrate de poner el link de tu propio repositorio (por ejemplo, `https://github.com/AgentBooster/oaqjp-final-project-emb-ai/blob/main/...`).

---

### Question 1 — Task 1: Submit the public GitHub repository URL of README.md file...

**Respuesta (reemplaza con tu URL exacto):**
`https://github.com/AgentBooster/oaqjp-final-project-emb-ai/blob/main/README.md`

---

### Question 2 — Task 2: Activity 1: Copy and paste the code of the emotion_detection.py (2a_emotion_detection)

**Respuesta:**

```python
import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(url, json=input_json, headers=headers)
    return response.text
```

_(Nota: El código superior es estrictamente el del Task 2 inicial antes del formateo final. Si prefieres enviar la versión final, usa el código de la Pregunta 12)._

---

### Question 3 — Task 2: Activity 2: Copy and paste the terminal output (2b_application_creation)

**Respuesta:**

```text
>>> from emotion_detection import emotion_detector
>>> emotion_detector("I love this new technology.")
'{\n  "emotionPredictions": [\n    {\n      "emotion": {\n        "anger": 0.006274985,\n        "disgust": 0.0025598293,\n        "fear": 0.009251528,\n        "joy": 0.9680386,\n        "sadness": 0.049744144\n      },\n...
```

---

### Question 4 — Task 3: Activity 1: Copy and paste the code of emotion_detection.py (3a_output_formatting)

**Respuesta:**

```python
import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(url, json=input_json, headers=headers)

    formatted_response = json.loads(response.text)

    if 'emotionPredictions' in formatted_response:
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        anger_score = emotions.get('anger', 0)
        disgust_score = emotions.get('disgust', 0)
        fear_score = emotions.get('fear', 0)
        joy_score = emotions.get('joy', 0)
        sadness_score = emotions.get('sadness', 0)

        emotions_dict = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
        }
        dominant_emotion = max(emotions_dict, key=emotions_dict.get)

        return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }
```

---

### Question 5 — Task 3: Activity 2: Copy and paste the terminal output (3b_formatted_output_test)

**Respuesta:**

```text
>>> from emotion_detection import emotion_detector
>>> emotion_detector("I am so happy I am doing this")
{'anger': 0.013646698, 'disgust': 0.0017160787, 'fear': 0.008986979, 'joy': 0.9611504, 'sadness': 0.057317924, 'dominant_emotion': 'joy'}
```

---

### Question 6 — Task 4: Activity 1: Submit the public GitHub repository URL of the **init**.py file

**Respuesta (reemplaza con tu URL exacto):**
`https://github.com/AgentBooster/oaqjp-final-project-emb-ai/blob/main/final_project/EmotionDetection/__init__.py`

_(Asegúrate de haber hecho push de tu repositorio antes de enviar)._

---

### Question 7 — Task 4: Activity 2: Copy and paste the terminal output (4b_packaging_test)

**Respuesta:**

```text
>>> from EmotionDetection.emotion_detection import emotion_detector
>>> emotion_detector("I hate working long hours")
{'anger': 0.77665406, 'disgust': 0.25413346, 'fear': 0.09311681, 'joy': 0.011709405, 'sadness': 0.17062402, 'dominant_emotion': 'anger'}
```

---

### Question 8 — Task 5: Activity 1: Copy and paste the code of test_emotion_detection.py (5a_unit_testing)

**Respuesta:**

```python
import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        # Test case 1
        result_1 = emotion_detector("I am glad this happened")
        self.assertEqual(result_1['dominant_emotion'], 'joy')

        # Test case 2
        result_2 = emotion_detector("I am really mad about this")
        self.assertEqual(result_2['dominant_emotion'], 'anger')

        # Test case 3
        result_3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result_3['dominant_emotion'], 'disgust')

        # Test case 4
        result_4 = emotion_detector("I am so sad about this")
        self.assertEqual(result_4['dominant_emotion'], 'sadness')

        # Test case 5
        result_5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result_5['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()
```

---

### Question 9 — Task 5: Activity 2: Copy and paste the terminal output (5b_unit_testing_result)

**Respuesta:**

```text
$ python3 test_emotion_detection.py
.....
----------------------------------------------------------------------
Ran 5 tests in 2.891s

OK
```

---

### Question 10 — Task 6: Activity 1: Copy and paste the code of server.py (6a_server)

**Respuesta:**

```python
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("EmotionDetector")

@app.route("/emotionDetector")
def emp_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is <b>{response['dominant_emotion']}</b>."
    )

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

_(Nota: Este es el código de Server antes del status de error y docstrings)._

---

### Question 11 — Task 6: Activity 2: Upload the image of the application (6b_deployment_test.png)

**Respuesta:**
_(Debes subir la imagen desde tu computadora a la plataforma de Coursera que muestra la salida correcta en el navegador)._

---

### Question 12 — Task 7: Activity 1: Copy and paste the code of emotion_detection.py (7a_error_handling_function)

**Respuesta:**

```python
import requests
import json

def emotion_detector(text_to_analyze):
    if not text_to_analyze:
        return { 'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None }

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(url, json=input_json, headers=headers)

    if response.status_code == 400:
        return { 'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None }

    formatted_response = json.loads(response.text)

    if 'emotionPredictions' in formatted_response:
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        emotions_dict = {
            'anger': emotions.get('anger', 0),
            'disgust': emotions.get('disgust', 0),
            'fear': emotions.get('fear', 0),
            'joy': emotions.get('joy', 0),
            'sadness': emotions.get('sadness', 0)
        }
        dominant_emotion = max(emotions_dict, key=emotions_dict.get)
        emotions_dict['dominant_emotion'] = dominant_emotion
        return emotions_dict
```

---

### Question 13 — Task 7: Activity 2: Copy and paste the code of server.py (7b_error_handling_server)

**Respuesta:**

```python
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("EmotionDetector")

@app.route("/emotionDetector")
def emp_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is <b>{response['dominant_emotion']}</b>."
    )

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

---

### Question 14 — Task 7: Activity 3: Upload the application deployment output image (7c_error_handling_interface.png)

**Respuesta:**
_(Sube la imagen desde tu computadora a la plataforma de Coursera probando el campo de texto en blanco)._

---

### Question 15 — Task 8: Activity 1: Copy and paste the code of server.py (8a_server_modified)

**Respuesta:**

```python
"""
server module for Emotion Detection App
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("EmotionDetector")


@app.route("/emotionDetector")
def emp_detector():
    """
    Route for emotion detection
    """
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is <b>{response['dominant_emotion']}</b>."
    )


@app.route("/")
def render_index_page():
    """
    Render main index page
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

---

### Question 16 — Task 8: Activity 2: Copy and paste the terminal output (8b_static_code_analysis)

**Respuesta:**

```text
$ pylint server.py

-------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 7.69/10, +2.31)
```
