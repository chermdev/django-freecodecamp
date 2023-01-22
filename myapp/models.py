from django.db import models
from dataclasses import dataclass

# Create your models here.


@dataclass
class Feature:
    id: int
    name: str
    details: str
    is_true: bool
