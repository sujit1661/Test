#
# import os
# import subprocess
#
# def download_song(song_name, output_directory):
#     try:
#         # Replace spaces in the song name with '+' for search query
#         formatted_song_name = song_name.replace(" ", "+")
#
#         # Use spotDL to search and download the song
#         command = f'spotdl "{formatted_song_name}" --output "{output_directory}"'
#         subprocess.run(command, shell=True, check=True)
#         print(f"✅ Song '{song_name}' downloaded successfully to {output_directory}!")
#     except Exception as e:
#         print(f"❌ Error downloading '{song_name}': {e}")
# # Ensure this runs only when the script is executed directly
# if __name__ == "__main__":
#     user_input = input("🎵 Enter the name of the song: ")
#
#     # Get the Desktop path dynamically
#     desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
#
#     # Create the output directory if it doesn't exist
#     os.makedirs(desktop_path, exist_ok=True)
#
#     download_song(user_input, desktop_path)

#
# import os
# import subprocess
# from flask import Flask, request, jsonify, send_from_directory, render_template
#
# app = Flask(__name__)
#
# # Directory to save downloaded songs
# SONG_DIRECTORY = "downloads"
# os.makedirs(SONG_DIRECTORY, exist_ok=True)
#
# @app.route('/')
# def index():
#     return render_template("index.html")  # Ensure index.html is inside "templates/"
#
# def download_song(song_name):
#     formatted_song_name = song_name.replace(" ", "+")
#     command = f'spotdl "{formatted_song_name}" --output "{SONG_DIRECTORY}"'
#
#     result = subprocess.run(command, shell=True, capture_output=True, text=True)
#
#     # If the command failed, return None
#     if result.returncode != 0:
#         return None
#
#     # Get the latest downloaded file
#     downloaded_files = sorted(
#         os.listdir(SONG_DIRECTORY),
#         key=lambda x: os.path.getctime(os.path.join(SONG_DIRECTORY, x)),
#         reverse=True
#     )
#     return downloaded_files[0] if downloaded_files else None
#
# @app.route('/download-song', methods=['POST'])
# def download_song_api():
#     song_name = request.json.get("song_name")
#     if not song_name:
#         return jsonify({"error": "No song name provided"}), 400
#
#     file_name = download_song(song_name)
#     if not file_name:
#         return jsonify({"error": "Failed to download song"}), 500
#
#     return jsonify({"song_url": f"/songs/{file_name}"})
#
# @app.route('/songs/<filename>')
# def serve_song(filename):
#     return send_from_directory(SONG_DIRECTORY, filename)
#
# if __name__ == '__main__':
#     app.run(debug=True)


import os
import subprocess
from flask import Flask, request, jsonify, send_from_directory, render_template

app = Flask(__name__)

# Directory to save downloaded songs
SONG_DIRECTORY = "downloads"
os.makedirs(SONG_DIRECTORY, exist_ok=True)

@app.route('/')
def index():
    return render_template("index.html")  # Ensure index.html is inside "templates/"

@app.route('/home')
def home():
    return render_template("home.html")  # ✅ Added route for Home Page

@app.route('/login')
def login():
    return render_template("login.html")  # ✅ Added route for Login Page

@app.route('/top-artist')
def top_artist():
    return render_template("topArtist.html")  # ✅ Added route for Top Artist Page

@app.route('/learn')
def learn():
    return render_template("learn.html")  # ✅ Added route for Learn Page

@app.route('/contact')
def contact():
    return render_template("contact.html")  # ✅ Added route for Contact Page

def download_song(song_name):
    formatted_song_name = song_name.replace(" ", "+")
    command = f'spotdl "{formatted_song_name}" --output "{SONG_DIRECTORY}"'

    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    # If the command failed, return None
    if result.returncode != 0:
        return None

    # Get the latest downloaded file
    downloaded_files = sorted(
        os.listdir(SONG_DIRECTORY),
        key=lambda x: os.path.getctime(os.path.join(SONG_DIRECTORY, x)),
        reverse=True
    )
    return downloaded_files[0] if downloaded_files else None

@app.route('/download-song', methods=['POST'])
def download_song_api():
    song_name = request.json.get("song_name")
    if not song_name:
        return jsonify({"error": "No song name provided"}), 400

    file_name = download_song(song_name)
    if not file_name:
        return jsonify({"error": "Failed to download song"}), 500

    return jsonify({"song_url": f"/songs/{file_name}"})

@app.route('/songs/<filename>')
def serve_song(filename):
    return send_from_directory(SONG_DIRECTORY, filename)

if __name__ == '__main__':
    app.run(debug=True)
