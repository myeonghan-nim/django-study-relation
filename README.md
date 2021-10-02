# README

## M:N modeling

```python
class Doctor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Patient(models.Model):
    name = models.CharField(max_length=100)
    doctors = models.ManyToManyField(Doctor, related_name="patients")

    def __str__(self):
        return self.name
```

## Error vinding

```python
from django.shortcuts import get_object_or_404
```

