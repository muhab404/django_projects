
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


from .models import Customer

def customer_profile(sender, instance, created, **kwargs):
	if created:
        # add the new register to a group customer
		group = Group.objects.get(name='customer')
		instance.groups.add(group)

        # link the new register to a user in customer model
		Customer.objects.create(
			user=instance,
			name=instance.username,
			)
		print('Profile created!')

post_save.connect(customer_profile, sender=User)