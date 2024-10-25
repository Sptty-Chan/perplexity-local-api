# perplexity-local-api
Api Perplexity (ai seperti chatgpt) unlimited gratis tanpa login

# cara menjalankan program
### 1. salin command dibawah
    pip install -r requirements.txt
### 2. salin command dibawan
    gunicorn -c config.py --bind 0.0.0.0:5000 wsgi:app

# table url
| part url | value |
| --------- | --------------- |
| hostname | 0.0.0.0 |
| port | 5000 |
| path | /api |
| parameter | prompt={{string}} |

# full url
    http://0.0.0.0:5000/api?prompt={{string}}


#### catatan:
gunakan + sebagai ganti spasi pada teks prompt kalian, seperti berikut

    http://0.0.0.0:5000/api?prompt=buatkan+cerita+lucu
