from django.contrib import admin

from .models import Mecz
admin.site.register(Mecz)

from .models import Zawodnik
admin.site.register(Zawodnik)

from .models import Zawodnik_mecz
admin.site.register(Zawodnik_mecz)

from .models import Sedzia
admin.site.register(Sedzia)

from .models import Sedzia_mecz
admin.site.register(Sedzia_mecz)

from .models import Stadion
admin.site.register(Stadion)

from .models import Zdarzenie
admin.site.register(Zdarzenie)

from .models import Liga
admin.site.register(Liga)

from .models import Uzytkownik
admin.site.register(Uzytkownik)

from .models import Zespol
admin.site.register(Zespol)

from .models import Gospodarz
admin.site.register(Gospodarz)

from .models import Gosc
admin.site.register(Gosc)

from .models import Liga_zespol
admin.site.register(Liga_zespol)
