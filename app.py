from flask import Flask, request, render_template, send_file, Response
from PIL import Image
import io

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def process_image():
    if request.method == 'POST':
        uploaded_image = request.files['file']
        if uploaded_image:
            try:
                img = Image.open(uploaded_image)
                img1 = img.resize((157, 121))

                canvas_width = 1080
                canvas_height = 720
                canvas = Image.new('RGB', (canvas_width, canvas_height), 'white')
                canvas.paste(img1, (716, 554))

                output_buffer = io.BytesIO()
                canvas.save(output_buffer, format='JPEG')
                output_buffer.seek(0)

                return Response(output_buffer, content_type='image/jpeg')
            except Exception as e:
                return "Error processing image: " + str(e)
        else:
            return "No file uploaded."

    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)