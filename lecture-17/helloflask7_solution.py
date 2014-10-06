# TODO now let's add a form that we can used to submit lyrics.
# TODO import request from flask
from flask import Flask, render_template
from msd.stem import transformLyrics
from sklearn.externals import joblib

app = Flask(__name__)


print 'Loading model...'
pipeline = joblib.load('lyrics_pipeline.pkl')
print 'Model loaded!'

# TODO add a view for the route '/' that renders the template 'lyrics_form.html'
# TODO inspect the template 'lyrics_form.html'

# TODO bind this view to the route '/predictions'
# TODO set this view to use HTTP POST only

def predict_artist():
    # TODO get the lyrics from the body of the POST request

    lyrics = transformLyrics(lyrics)
    print 'predicting artist for %s' % lyrics
    prediction = pipeline.predict([lyrics])
    d = {
        'lyrics': lyrics,
        'artist': prediction[0]
    }
    return render_template('prediction.html', d=d)

if __name__ == '__main__':
    app.debug = True
    app.run()