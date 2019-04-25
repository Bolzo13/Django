from django.db import models

class CatDest(models.Model):
	descrizione = models.CharField(max_length=50)

	def __str__(self):
		return self.descrizione

	class Meta:
		verbose_name = "Categoria Destinatario"
		verbose_name_plural = "Categorie Destinatario"

class Circolare(models.Model):
	NumeroProgressivo = models.SmallIntegerField()
	AnnoScolastico =models.CharField(max_length=15,default="2018/2019")
	Destinatario = models.TextField()
	CategoriaDestinatari = models.ManyToManyField(CatDest)
	Oggetto = models.CharField(max_length=50)
	DataPubblicazione = models.DateField("Data di Pubblicazione")
	Allegato = models.URLField(blank=True,null=True)
	DataScadenza = models.DateField(blank=True,null=True)

	def __str__(self):
		return "Numero: %d"  %self.NumeroProgressivo +" %s"  %self.AnnoScolastico + ", Oggetto: " +  self.Oggetto

	class Meta:
		verbose_name = "Circolare"
		verbose_name_plural = "Circolari"