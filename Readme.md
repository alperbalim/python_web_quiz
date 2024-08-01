Görünüşe göre dosya indirme işlemi sırasında bir hata oluştu. Alternatif olarak, README içeriğini doğrudan buraya yapıştırıyorum. Bu içeriği kendi metin düzenleyicinizde bir dosya olarak kaydedebilirsiniz.

**README.md**
```markdown
# AI Geliştirme Sınavı

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [References](#references)
- [Roadmap](#roadmap)

## Introduction

Bu proje, AI ve makine öğrenimi konularında bir sınav web uygulaması sağlamaktadır. Flask ve SQLAlchemy kullanarak geliştirilmiştir. Kullanıcılar sınav sorularını cevaplar ve sonuçlarını görebilirler. Her sınavda kullanıcıya rastgele 5 soru gösterilir. Ayrıca, her bir sorunun seçenekleri rastgele sıralanır ve kullanıcıların her soruyu cevaplaması zorunludur.

Proje yapısı şu şekildedir:

```bash
├── app.py
├── models.py
├── templates
│   ├── home.html
│   └── result.html
├── instance
│   └── quiz.db
└── README.md
```

## Installation

### System/Dependencies

- **OS**: Ubuntu 22.04
- **Python Version**: 3.10+
- **Flask Version**: 2.0+
- **SQLAlchemy Version**: 1.4+

**Software Dependencies:** 
- Flask
- Flask-SQLAlchemy

### Kurulum Adımları

Proje dosyalarını klonlayın ve gerekli Python paketlerini yükleyin:

```bash
git clone https://github.com/alperbalim/python_web_quiz.git
cd python_web_quiz
pip install -r requirements.txt
```

## Usage

### Uygulamanın Başlatılması

Uygulamayı başlatmak için aşağıdaki komutu kullanın:

```bash
python app.py
```

Tarayıcınızda `http://localhost:5000` adresine giderek uygulamayı kullanabilirsiniz.

## References

- [Flask Documentation](https://flask.palletsprojects.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)

## Roadmap

- Daha fazla soru eklenmesi
- Kullanıcı doğrulama ve oturum yönetimi
- Gelişmiş istatistik ve sonuç analizi