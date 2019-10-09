from django.db import models

from multiselectfield import MultiSelectField

from menu_rest_api import settings

THAI_MENU = (('Tom yum goong', 'Tom yum goong'),
             ('Som tum', 'Som tum'),
             ('Tom kha kai', 'Tom kha kai'),
             ('Gaeng daeng', 'Gaeng daeng'),
             ('Pad thai', 'Pad thai'))

RUSSIAN_MENU = (('Borscht', 'Borscht'),
                ('Shchi', 'Shchi'),
                ('Solyanka', 'Solyanka'),
                ('Ukha', 'Ukha'),
                ('Pelmeni', 'Pelmeni'))

FRENCH_MENU = (('Chocolate souffle', 'Chocolate souffle'),
               ('Beef bourguignon', 'Beef bourguignon'),
               ('Flamiche', 'Flamiche'),
               ('Confit de canard', 'Confit de canard'),
               ('Nicoise salad', 'Nicoise salad'))


class OrderModel(models.Model):

    thai_choice = MultiSelectField(choices=THAI_MENU, blank=True)
    russian_choice = MultiSelectField(choices=RUSSIAN_MENU, blank=True)
    french_choice = MultiSelectField(choices=FRENCH_MENU, blank=True)
