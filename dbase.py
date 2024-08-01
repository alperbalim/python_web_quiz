
from db import db
import random

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(200), nullable=False)
    option1 = db.Column(db.String(100), nullable=False)
    option2 = db.Column(db.String(100), nullable=False)
    option3 = db.Column(db.String(100), nullable=False)
    option4 = db.Column(db.String(100), nullable=False)
    answer = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'question': self.question,
            'option1': self.option1,
            'option2': self.option2,
            'option3': self.option3,
            'option4': self.option4,
            'answer': self.answer
        }
    def shuffled_options(self):
        options = [self.option1, self.option2, self.option3, self.option4]
        random.shuffle(options)
        return options
    
def create_db():
    db.create_all()

    additional_questions = [
        Question(question="Python programlama dilinde AI geliştirme için en yaygın kullanılan kütüphanelerden biri hangisidir?", option1="NumPy", option2="SciPy", option3="Pandas", option4="TensorFlow", answer="TensorFlow"),
        Question(question="AI geliştirme sürecinde modelin doğruluğunu artırmak için hangi yöntem kullanılır?", option1="Veri temizleme", option2="Veri analizi", option3="Veri artırma", option4="Veri görselleştirme", answer="Veri artırma"),
        Question(question="Bilgisayar görüşünde görüntü sınıflandırma yapmak için en yaygın kullanılan derin öğrenme mimarisi nedir?", option1="RNN", option2="CNN", option3="DNN", option4="GAN", answer="CNN"),
        Question(question="Bir görüntüdeki nesneleri tanımak için kullanılan algoritmaya ne ad verilir?", option1="Görüntü segmentasyonu", option2="Nesne algılama", option3="Yüz tanıma", option4="Görüntü iyileştirme", answer="Nesne algılama"),
        Question(question="Doğal dil işleme (NLP) alanında, metin verilerini sayısal verilere dönüştürmek için hangi yöntem kullanılır?", option1="Tokenization", option2="Lemmatization", option3="Stemming", option4="One-hot encoding", answer="One-hot encoding"),
        Question(question="NLP'de, kelime anlamını temsil etmek için kullanılan vektörlerin oluşturulmasına ne ad verilir?", option1="Word2Vec", option2="Bag of Words", option3="TF-IDF", option4="Sentiment Analysis", answer="Word2Vec"),
        Question(question="Python'da AI modellerini eğitmek için kullanılan en yaygın kütüphane hangisidir?", option1="Keras", option2="Matplotlib", option3="Seaborn", option4="Django", answer="Keras"),
        Question(question="Python'da AI geliştirme sürecinde hiperparametre optimizasyonu yapmak için hangi kütüphane kullanılır?", option1="Scikit-learn", option2="Optuna", option3="TensorFlow", option4="Pandas", answer="Optuna"),
        Question(question="Bilgisayar görüşünde görüntülerin veri seti olarak kullanılması için en yaygın format hangisidir?", option1="JPEG", option2="PNG", option3="TIFF", option4="COCO", answer="COCO"),
        Question(question="Görüntü işleme alanında, bir görüntüdeki kenarları tespit etmek için hangi algoritma kullanılır?", option1="Canny Edge Detection", option2="Hough Transform", option3="Fourier Transform", option4="Convolutional Layer", answer="Canny Edge Detection"),
        Question(question="NLP alanında, kelimelerin sıklığını ve önemini belirlemek için kullanılan yöntem nedir?", option1="Bag of Words", option2="TF-IDF", option3="Word Embeddings", option4="POS Tagging", answer="TF-IDF"),
        Question(question="NLP modellerinde dilin kurallarını öğrenmek ve kullanmak için hangi yöntem kullanılır?", option1="Syntax Parsing", option2="Word Embeddings", option3="Tokenization", option4="Sentiment Analysis", answer="Syntax Parsing"),
        Question(question="AI geliştirme sürecinde kullanılan bir modelin performansını değerlendirmek için hangi metrik kullanılabilir?", option1="Accuracy", option2="Mean Absolute Error", option3="Confusion Matrix", option4="Hepsi", answer="Hepsi"),
        Question(question="AI modellerinde overfitting'i önlemek için kullanılan yöntem hangisidir?", option1="Dropout", option2="Batch Normalization", option3="Data Augmentation", option4="Hepsi", answer="Hepsi"),
        Question(question="Makine öğreniminde, verilerdeki doğrusal ilişkileri modellemek için hangi algoritma kullanılır?", option1="Lineer Regresyon", option2="Logistic Regression", option3="Decision Tree", option4="Random Forest", answer="Lineer Regresyon"),
        Question(question="Destek Vektör Makineleri (SVM) hangi amaçla kullanılır?", option1="Sınıflandırma ve Regresyon", option2="Veri Temizleme", option3="Veri Görselleştirme", option4="Özellik Seçimi", answer="Sınıflandırma ve Regresyon"),
        Question(question="K-En Yakın Komşu (KNN) algoritması hangi tür problem için kullanılır?", option1="Sınıflandırma", option2="Regresyon", option3="Her İkisi", option4="Hiçbiri", answer="Her İkisi"),
        Question(question="K-means algoritması hangi amaçla kullanılır?", option1="Sınıflandırma", option2="Regresyon", option3="Kümeleme", option4="Boyut İndirgeme", answer="Kümeleme"),
        Question(question="Görüntü işleme alanında hangi yöntem, bir görüntünün belirli bölgelerinin maskelenmesi için kullanılır?", option1="Convolutional Neural Networks (CNN)", option2="Fourier Transform", option3="Thresholding", option4="Principal Component Analysis (PCA)", answer="Thresholding"),
        Question(question="Hangi makine öğrenimi algoritması doğrusal olmayan karar sınırları oluşturmak için kullanılır?", option1="Lineer Regresyon", option2="Destek Vektör Makineleri (SVM)", option3="Naive Bayes", option4="K-En Yakın Komşu (KNN)", answer="Destek Vektör Makineleri (SVM)"),
        Question(question="Principal Component Analysis (PCA) hangi amaçla kullanılır?", option1="Boyut İndirgeme", option2="Sınıflandırma", option3="Regresyon", option4="Kümeleme", answer="Boyut İndirgeme"),
        Question(question="Bir görüntünün kenarlarını belirlemek için hangi yöntem kullanılır?", option1="K-Means", option2="PCA", option3="Canny Edge Detection", option4="KNN", answer="Canny Edge Detection"),
        Question(question="Makine öğreniminde, hangi yöntem denetimli öğrenme yöntemlerinden biridir?", option1="K-Means", option2="Principal Component Analysis", option3="Destek Vektör Makineleri (SVM)", option4="Kümeleme", answer="Destek Vektör Makineleri (SVM)"),
        Question(question="Doğal dil işleme alanında, metinlerin kategorize edilmesi için hangi algoritma yaygın olarak kullanılır?", option1="Lineer Regresyon", option2="Destek Vektör Makineleri (SVM)", option3="Naive Bayes", option4="KNN", answer="Naive Bayes"),
        Question(question="Lineer Regresyon modelinin amacı nedir?", option1="Veri kümelerini sınıflandırmak", option2="Doğrusal ilişkileri modellemek", option3="Veri kümelerini kümelemek", option4="Öznitelik seçimi yapmak", answer="Doğrusal ilişkileri modellemek"),
        Question(question="SVM'de karar sınırlarını belirlemek için hangi kavram kullanılır?", option1="Doğrusal regresyon", option2="Karar ağacı", option3="Hiper düzlem", option4="Öznitelik kümesi", answer="Hiper düzlem"),
        Question(question="KNN algoritmasının temel prensibi nedir?", option1="Verilerin ortalamasını hesaplamak", option2="Komşu verileri kullanarak tahmin yapmak", option3="Verileri kümelemek", option4="Verileri görselleştirmek", answer="Komşu verileri kullanarak tahmin yapmak"),
        Question(question="K-Means algoritması hangi tür problemleri çözmek için kullanılır?", option1="Sınıflandırma", option2="Regresyon", option3="Kümeleme", option4="Boyut indirgeme", answer="Kümeleme"),
        Question(question="Görüntü işleme alanında, bir görüntünün belirli bölgelerini maskelemek için hangi yöntem kullanılır?", option1="Filtreleme", option2="Segmentasyon", option3="Eşikleme", option4="Morfolojik işlemler", answer="Eşikleme"),
        Question(question="Makine öğreniminde, modelin performansını değerlendirmek için hangi yöntem kullanılır?", option1="Hata kareler ortalaması (MSE)", option2="Öznitelik seçimi", option3="Veri kümeleme", option4="Veri temizleme", answer="Hata kareler ortalaması (MSE)"),
        Question(question="Principal Component Analysis (PCA) hangi amaçla kullanılır?", option1="Veri sınıflandırma", option2="Doğrusal regresyon", option3="Boyut indirgeme", option4="Veri artırma", answer="Boyut indirgeme"),
        Question(question="Bir görüntünün kenarlarını belirlemek için hangi yöntem kullanılır?", option1="Histogram eşitleme", option2="Fourier dönüşümü", option3="Canny kenar algılama", option4="Gaussian bulanıklığı", answer="Canny kenar algılama"),
        Question(question="Makine öğreniminde denetimli öğrenme yöntemlerinden biri hangisidir?", option1="K-Means", option2="PCA", option3="Destek Vektör Makineleri (SVM)", option4="Veri temizleme", answer="Destek Vektör Makineleri (SVM)"),
        Question(question="Doğal dil işleme alanında, metinlerin kategorize edilmesi için yaygın olarak kullanılan algoritma hangisidir?", option1="Lineer Regresyon", option2="SVM", option3="Naive Bayes", option4="KNN", answer="Naive Bayes")

    ]

    for q in additional_questions:
        db.session.add(q)
    print("Database created!!")
    db.session.commit()

