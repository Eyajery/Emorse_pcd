from django.db import models

# Create your models here.

class RoomMember(models.Model):
    name = models.CharField(max_length=200)
    uid = models.CharField(max_length=1000)
    room_name = models.CharField(max_length=200)
    insession = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}, {self.uid},{self.room_name},{self.insession}'


class Etudiant(models.Model):
    nom = models.CharField(max_length=100, primary_key=True)
    prenom = models.CharField(max_length=100,default=None)
    date_naissance = models.DateField(default=None)
    email = models.EmailField(default=None)

    class Meta:
        verbose_name_plural = 'etudiants'

    def __str__(self):
        return f'{self.nom} '

class Session(models.Model):
    nom = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    etat = models.CharField(max_length=100,default='absent(e)')

    class Meta:
        verbose_name_plural = 'sessions'

    def __str__(self):
        return f'{self.nom},{self.etat}'


class Detection(models.Model):
    etudiant = models.ForeignKey(Session, on_delete=models.CASCADE,default=None)
    emotion = models.CharField(max_length=255)
    detection_time = models.DateTimeField(auto_now_add=True)
   
    class Meta:
        verbose_name_plural = 'Detection'

    def __str__(self):
        return f'{self.emotion}, {self.detection_time},{self.etudiant.nom}'


class Recommendation(models.Model):
    nom = models.CharField(max_length=200)
    pdf = models.FileField(upload_to='pdf/', default='pdf/chapitre_3.pdf')

    def __str__(self):
        return self.nom
  
    
