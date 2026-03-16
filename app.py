from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>MLOps Pipeline Deployment Successful!</h1><p>Student: BIAO YU | ID: 25526462</p><p>Deployed via GitHub Actions & Docker.</p>"

if __name__ == '__main__':
    # 必须监听 0.0.0.0，否则 Docker 外部无法访问
    app.run(host='0.0.0.0', port=8000)