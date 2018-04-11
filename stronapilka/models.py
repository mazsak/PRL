from django.db import models
from django_countries.fields import CountryField
from django.utils.encoding import python_2_unicode_compatible

class Uzytkownik(models.Model):
	login = models.CharField(max_length=30)
	haslo = models.CharField(max_length=30)
	email = models.CharField(max_length=30)
	nr_telefonu = models.IntegerField(default=500123456)

class Stadion(models.Model):
	nazwa = models.CharField(max_length=30)
	kraj = CountryField()
	pojemnosc = models.IntegerField(default=10000)

class Zespol(models.Model):
	id_stadionu = models.ForeignKey(Stadion, on_delete=models.CASCADE)
	nazwa = models.CharField(max_length=30)
	trener = models.CharField(max_length=30)
	kraj = CountryField()

class Zawodnik(models.Model):
	Napastnik = 'N'
	Lewy_napastnik = 'LN'
	Prawy_napastnik = 'PN'
	Lewy_skrzydlowy = 'LS'
	Prawy_skrzydlowy = 'PS'
	Srodkowy_pomocnik = 'SP'
	Srodkowy_pomocnik_defensywny = 'SPD'
	Srodkowy_pomocnik_ofensywny = 'SPO'
	Srodkowy_napastnik = 'SN'
	Lewy_pomocnik = 'LP'
	Prawy_pomocnik = 'PP'
	Lewy_obronca = 'LO'
	Prawy_obronca = 'PO'
	Srodkowy_obronca = 'SO'
	Lewy_wahadlowy = 'LW'
	Prawy_wahadlowy = 'PW'
	Bramkarz = 'BR'
	imie = models.CharField(max_length=30)
	nazwisko = models.CharField(max_length=30)
	kraj = CountryField()
	nr_zawodnika_klub = models.IntegerField(default=1)
	nr_zawodnika_reprezentacja = models.IntegerField(default=1)
	pozycja_choices = (
		(Napastnik, 'N'),
		(Lewy_napastnik, 'LN'),
		(Prawy_napastnik, 'PN'),
		(Lewy_skrzydlowy, 'LS'),
		(Prawy_skrzydlowy, 'PS'),
		(Srodkowy_pomocnik, 'SP'),
		(Srodkowy_pomocnik_defensywny, 'SPD'),
		(Srodkowy_pomocnik_ofensywny, 'SPO'),
		(Srodkowy_napastnik, 'SN'),
		(Lewy_pomocnik, 'LP'),
		(Prawy_pomocnik, 'PP'),
		(Lewy_obronca, 'LO'),
		(Prawy_obronca, 'PO'),
		(Srodkowy_obronca, 'SO'),
		(Lewy_wahadlowy, 'LW'),
		(Prawy_wahadlowy, 'PW'),
		(Bramkarz, 'BR'),
	)
	pozycja = models.CharField(
		max_length=20,
		choices = pozycja_choices,
		default = 'N',
	)
	id_zespolu = models.ForeignKey(Zespol, on_delete=models.CASCADE)
	def __str__(self):
        	return '%s %s' % (self.imie, self.nazwisko)


class Liga(models.Model):
	Liga = 'Liga'
	Puchar = 'Play-off'
	Grupy = 'Grupy'
	nazwa = models.CharField(max_length=30)
	typ_choices = (
		(Liga, 'Liga'),
		(Puchar, 'Play-off'),
		(Grupy, 'Grupy'),	
	)
	typ = models.CharField(
		max_length=30,
		choices = typ_choices,
		default = Liga,
	)
	kraj = CountryField()

class Sedzia(models.Model):
	Glowny = 'Glowny'
	Liniowy = 'Liniowy'
	Techniczny = 'Techniczny'
	Zabramkowy = 'Zabramkowy'
	imie = models.CharField(max_length=30)
	nazwisko = models.CharField(max_length=30)
	typ_choices = (
		(Glowny, 'Glowny'),
		(Liniowy, 'Liniowy'),
		(Techniczny, 'Techniczny'),
		(Zabramkowy, 'Zabramkowy'),
	)
	typ = models.CharField(
		max_length=30,
		choices=typ_choices,
		default=Glowny,
	)
	
	

class Mecz(models.Model):
	id_stadionu = models.ForeignKey(Stadion, on_delete=models.CASCADE)
	data = models.DateTimeField('data meczu')

class Gospodarz(models.Model):
	id_zespolu = models.ForeignKey(Zespol, on_delete=models.CASCADE)
	id_meczu = models.ForeignKey(Mecz, on_delete=models.CASCADE)
	gole = models.IntegerField(default=0)
	posiadanie = models.IntegerField(default=50)
	strzaly = models.IntegerField(default=0)
	strzaly_celne = models.IntegerField(default=0)

class Gosc(models.Model):
	id_zespolu = models.ForeignKey(Zespol, on_delete=models.CASCADE)
	id_meczu = models.ForeignKey(Mecz, on_delete=models.CASCADE)
	gole = models.IntegerField(default=0)
	posiadanie = models.IntegerField(default=50)
	strzaly = models.IntegerField(default=0)
	strzaly_celne = models.IntegerField(default=0)

class Zawodnik_mecz(models.Model):
	id_meczu = models.ForeignKey(Mecz, on_delete=models.CASCADE)
	id_zawodnika = models.ForeignKey(Zawodnik, on_delete=models.CASCADE)
	pozycja = models.CharField(max_length=30)

class Zdarzenie(models.Model):
	Bramka = 'Bramka'
	Spalony = 'Spalony'
	Kontuzja = 'Kontuzja'
	Zolta = 'Zolta kartka'
	Czerwona = 'Czerwona kartka'
	Asysta = 'Asysta'
	Karny = 'Rzut karny'
	Karny_niewykorzystany = 'Niewykorzystany karny'
	Wolny = 'Rzut wolny'
	Zmiana = 'Zmiana'
	typ_choices = (
		(Bramka, 'Bramka'),
		(Spalony, 'Spalony'),
		(Kontuzja, 'Kontuzja'),
		(Zolta, 'Zolta kartka'),
		(Czerwona, 'Czerwona kartka'),
		(Asysta, 'Asysta'),
		(Karny, 'Rzut karny'),
		(Karny_niewykorzystany, 'Niewykorzystany karny'),
		(Wolny, 'Rzut wolny'),
		(Zmiana, 'Zmiana'),
	)
	typ_zdarzenia = models.CharField(
		max_length=30,
		choices = typ_choices,
		default = Bramka, 
	)
	minuta = models.IntegerField(default=10)
	id_zawodnik_mecz = models.ForeignKey(Zawodnik_mecz, on_delete=models.CASCADE)

class Sedzia_mecz(models.Model):
	id_sedziego = models.ForeignKey(Sedzia, on_delete=models.CASCADE)
	id_meczu = models.ForeignKey(Mecz, on_delete=models.CASCADE)

class Liga_zespol(models.Model):
	id_ligi = models.ForeignKey(Liga, on_delete=models.CASCADE)
	id_zespolu = models.ForeignKey(Zespol, on_delete=models.CASCADE)
