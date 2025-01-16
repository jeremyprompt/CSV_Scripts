from flask import Flask, request, send_file
import pandas as pd
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'temp_uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/concatenate', methods=['POST'])
def concatenate_csvs():
    if 'csv_files' not in request.files:
        return 'No files uploaded', 400
    
    files = request.files.getlist('csv_files')
    dataframes = []
    
    try:
        for file in files:
            if file.filename:
                df = pd.read_csv(file)
                dataframes.append(df)
        
        result = pd.concat(dataframes, ignore_index=True)
        output_path = os.path.join(app.config['UPLOAD_FOLDER'], 'concatenated.csv')
        result.to_csv(output_path, index=False)
        
        return send_file(
            output_path,
            mimetype='text/csv',
            as_attachment=True,
            download_name='concatenated.csv'
        )
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True) 