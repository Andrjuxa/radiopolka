from core.models import Category


class CategoryApi:

    @classmethod
    def list(cls):
        return Category.objects.all().order_by('name')

    @classmethod
    def by_pk(cls, pk):
        return cls.list().get(pk=pk)
