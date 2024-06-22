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
