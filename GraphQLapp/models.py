from django.db import models

class NYC_data(models.Model):
    zip_code=models.CharField(max_length=20)
    street_name=models.CharField(max_length=20)
    block_NO=models.CharField(max_length=20)
    Lot_No=models.CharField(max_length=20)
    Built_Year=models.CharField(max_length=20)
    Building_class=models.CharField(max_length=20)
    Owner=models.CharField(max_length=20)
    State=models.CharField(max_length=20,default='NYC')
    class Meta:
        db_table='NYC_data'