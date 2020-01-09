from django.db import models
from users.models import Profile

########
# Assumption: isin, lei and legal_name are NOT unique??
# as entries might belong to different users according to functional specs)
########
class Bonds(models.Model):
    isin = models.CharField(max_length=15, verbose_name="isin")
    size = models.PositiveIntegerField()
    currency = models.CharField(max_length=5, verbose_name="currency")
    maturity = models.DateField(auto_now_add=False)
    lei = models.CharField(max_length=50, verbose_name="lei")
    legal_name = models.CharField(max_length=50, verbose_name="legal_name")
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="bonds")

    def __str__(self):
        return f"{self.legal_name} ({self.isin})"

    def __unicode__(self):
        return f"{self.legal_name} ({self.isin})"

    class Meta:
        verbose_name = "Bond"
        verbose_name_plural = "Bonds"
        db_table = "bonds"
