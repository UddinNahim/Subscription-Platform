from django.db import models
from account.models import CustomUser

# Create your models here.

class Subscription(models.Model):

    subscriber_name = models.CharField(max_length=255)
    subscription_plan = models.CharField(max_length=255)
    subscription_cost = models.CharField(max_length=255)

    paypal_subscription_id = models.CharField(max_length=255, blank=True, null=True)

    is_active = models.BooleanField(default=False)

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, unique=True)


    def __str__(self):
        return f'Subscription for {self.subscriber_name} - Plan: {self.subscription_plan} - Cost: {self.subscription_cost} - Active: {self.is_active}'
        
