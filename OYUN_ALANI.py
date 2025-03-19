from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///oyun_parki.db'
db = SQLAlchemy(app)

# Oyun alanı verileri için model
class OyunAlani(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kullanici_id = db.Column(db.Integer, nullable=False)
    yas = db.Column(db.Integer, nullable=False)
    binis_sayisi = db.Column(db.Integer, default=0)
    hiz = db.Column(db.String(20), default="normal")
    muzik_suresi = db.Column(db.Integer, default=5)

    def to_dict(self):
        return {
            "id": self.id,
            "kullanici_id": self.kullanici_id,
            "yas": self.yas,
            "binis_sayisi": self.binis_sayisi,
            "hiz": self.hiz,
            "muzik_suresi": self.muzik_suresi
        }

# Veritabanını oluştur
with app.app_context():
    db.create_all()

@app.route('/oyun-ekle', methods=['POST'])
def oyun_ekle():
    data = request.json
    yas = data.get("yas")
    
    # Yaşa göre hız ve müzik süresi belirleme
    if yas < 10:
        hiz = "yavaş"
        muzik_suresi = 3
    elif 10 <= yas <= 18:
        hiz = "normal"
        muzik_suresi = 5
    else:
        hiz = "hızlı"
        muzik_suresi = 7

    yeni_oyun = OyunAlani(
        kullanici_id=data.get("kullanici_id"),
        yas=yas,
        binis_sayisi=1,
        hiz=hiz,
        muzik_suresi=muzik_suresi
    )
    db.session.add(yeni_oyun)
    db.session.commit()

    return jsonify({"message": "Biniş kaydedildi!", "data": yeni_oyun.to_dict()}), 201

@app.route('/oyunlar', methods=['GET'])
def oyunlari_getir():
    oyunlar = OyunAlani.query.all()
    return jsonify([oyun.to_dict() for oyun in oyunlar])

if __name__ == '__main__':
    app.run(debug=True)
