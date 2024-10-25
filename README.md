# perplexity-local-api
Api Perplexity (ai seperti chatgpt) unlimited gratis tanpa login

# cara menjalankan program
### 1. salin command dibawah
    pip install -r requirements.txt
### 2. salin command dibawan
    gunicorn -c config.py --bind 0.0.0.0:5000 wsgi:app

# penggunaan
## host & port: 0.0.0.0:5000
## path: /api
## parameter: prompt={{text prompt kalian}}
## full url: http://0.0.0.0:5000/api?prompt={{text prompt kalian}}
catatan: gunakan + sebagai spasi pada text prompt
