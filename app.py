from flask import Flask, render_template

app = Flask(__name__)

#작품데이터 (제목, 제작년도, 크기, 재료, 작품 설명)
artworks_data = [
    {
        "title": "Accumulated pieces make it personal",
        "year": 2024,
        "size": "110 x 160 x 38cm",
        "materials": "plywood, plastic, compound media",
        "description": """ 이 작품은 개인의 영속성을 찾기 위한 가설의 첫번째 단계인 개인의 핵심을 찾아내는 과정 속에서 제작 되었습니다.
      작가는 개인의 핵심은 고유함이며, 타고난 성향과 살면서 겪는 수많은 순간들이 만나 결합되어 형성된다고 제시합니다.
      이를 물질화, 시각화 한다면 그 순간에 함께한 사물들이 될 수 있을 것입니다. 그 사물들을 수집하여 하나의 코드에 비유한 작품입니다.
      각 물건은 코드의 픽셀에 자리하고, 픽셀들이 모여 만든 유일한 코드는 다른 순간을 겪었다면 다른 사람이 되었을 개인에 비유됩니다.
      각각의 조각이 모여 한 사람을 상징하는 유일한 코드를 만들어 낸다. 라는 생각을 표현한 작품입니다.""",
      "image": "Accumulated_pieces-Full1.JPG"
    },
    {
    "title": "How to live after we are scattered again",
    "year": 2024,
    "size": "variable installation",
    "materials": "resin, compound media",
    "image": "HowToLive_scatter-full1.jpeg"},

    {"title": "Matter cycle; we remain eternal within it.",
     "year": 2024,
     "size": "44 x 47 x 1.5cm",
     "materials": "Full-fusing glass",
     "image": "mattercycle-detail1.jpeg"
    }
]

# 메인 페이지
@app.route('/')
def home():
    return render_template('index.html')

# 작가 소개 페이지
@app.route('/about')
def about_page():
    return render_template('about.html')

# 작품 페이지
@app.route('/artworks')
def artworks_page():
    return render_template('artworks.html', artworks=artworks_data)

# 전시 페이지
@app.route('/exhibitions')
def exhibitions_page():
    return render_template('exhibitions.html')

# 아카이브 페이지
@app.route('/archive')
def archive_page():
    return render_template('archive.html')

if __name__ == '__main__':
    app.run(debug=True)