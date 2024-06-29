from django.db import models

# Create your models here.
class Ausbilder(models.Model):
    name = models.CharField("Name", max_length=150)
    adresse = models.CharField(("Adresse"), max_length=150)
    info = models.TextField(("Informationen"))

    class Meta:
        verbose_name = ("Ausbilder")
        verbose_name_plural = ("Ausbilder")

    def __str__(self):
        return self.name

    #def get_absolute_url(self):
    #    return reverse("Ausbilder_detail", kwargs={"pk": self.pk})

class Gruppe(models.Model):
    bezeichnung = models.CharField(("Gruppe"), max_length=20)
    start = models.DateField(("Start der Ausbildung"), auto_now=False, auto_now_add=False)
    ende = models.DateField(("Ende der Ausbildung(Prüfung)"), auto_now=False, auto_now_add=False)
    online = models.BooleanField(("Online"), default=True)

    class Meta:
        verbose_name = ("Gruppe")
        verbose_name_plural = ("Gruppen")

    def __str__(self):
        return f"{self.bezeichnung} ({self.start})"

    #def get_absolute_url(self):
    #    return reverse("Gruppe_detail", kwargs={"pk": self.pk})

class Fach(models.Model):
    bezeichnung = models.CharField(("Bezeichnung"), max_length=50)
    inhalt = models.TextField(("Inhalt"))
    hauptausbilder = models.ForeignKey(Ausbilder, verbose_name=("Hauptausbilder"), on_delete=models.RESTRICT)
    # models.CASCADE - verbundene Datensätze Löschen
    # models.PROTECT - DS kann erste gelöscht werden, wenn keine FK vorhanden sind (restrict)
    # models.DO_NOTHING - Fehlerhafter FK bleibt erhalten (ignore)
    # models.SET_NULL - FK wird auf NULL gesetzt

    class Meta:
        verbose_name = ("Fach")
        verbose_name_plural = ("Fächer")

    def __str__(self):
        return self.bezeichnung

    #def get_absolute_url(self):
    #    return reverse("Fach_detail", kwargs={"pk": self.pk})
class Thema(models.Model):
    bezeichnung = models.CharField(("Bezeichnung"), max_length=50)
    fach = models.ForeignKey(Fach, verbose_name=("Fach"), on_delete=models.RESTRICT)
    inhalt = models.TextField(("Inhalt"))
    laenge = models.IntegerField(("Länge"))

    class Meta:
        verbose_name = ("Thema")
        verbose_name_plural = ("Themen")

    def __str__(self):
        return self.bezeichnung

    def get_absolute_url(self):
        return reverse("Thema_detail", kwargs={"pk": self.pk})

class Schueler(models.Model):
    name = models.CharField(("Schüler"), max_length=250)
    adresse = models.TextField(("Adresse"), blank=True, null=True)
    gruppe = models.ForeignKey(Gruppe, verbose_name=("Gruppe"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Schüler")
        verbose_name_plural = ("Schüler")

    def __str__(self):
        return f"{self.name} ({self.gruppe.bezeichnung})"
        
    def get_absolute_url(self):
        return reverse("Schueler_detail", kwargs={"pk": self.pk})

class Ausbildungseinheit(models.Model):
    bezeichnung = models.CharField(("Thema"), max_length=50)
    thema = models.ForeignKey(Thema, verbose_name=("Thema"), on_delete=models.RESTRICT)
    ausbilder = models.ForeignKey(Ausbilder, verbose_name=("Ausbilder"), on_delete=models.RESTRICT)
    gruppe = models.ForeignKey(Gruppe, verbose_name=("Gruppe"), on_delete=models.RESTRICT)
    datum = models.DateTimeField(("Datum"), auto_now=False, auto_now_add=False)
    laenge = models.IntegerField(("Länge"))

    class Meta:
        verbose_name = ("Ausbildungseinheit")
        verbose_name_plural = ("Ausbildungseinheiten")

    def __str__(self):
        return f"{self.bezeichnung} - ({self.thema}/{self.ausbilder} {self.datum})"

    def get_absolute_url(self):
        return reverse("ausbildungseinheit_detail", kwargs={"pk": self.pk})

class Lernerfolgskontrolle(models.Model):
    schueler = models.ForeignKey(Schueler, verbose_name=("Schüler"), on_delete=models.CASCADE)
    thema = models.ForeignKey(Thema, verbose_name=("Thema"), on_delete=models.CASCADE)
    datum = models.DateTimeField(("Datum"), auto_now=False, auto_now_add=False)
    punkte = models.IntegerField(("Punkte"))

    class Meta:
        verbose_name = ("Lernerfolgskontrolle")
        verbose_name_plural = ("Lernerfolgskontrollen")

    def __str__(self):
        return f"{self.schueler.name} - {self.thema.bezeichnung}"

    def get_absolute_url(self):
        return reverse("Lernerfolgskontrolle_detail", kwargs={"pk": self.pk})
