from .AdminFilter import AdminFilter
from .IsGroupFilter import IsGroupFilter
from .IsPrivate import IsPrivate
from loader import dp

if __name__ == "filters":
    dp.filters_factory.bind(AdminFilter)
    dp.filters_factory.bind(IsGroupFilter)
    dp.filters_factory.bind(IsPrivate)
