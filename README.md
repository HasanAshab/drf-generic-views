# DRF Generic Views
A set of generic views for Django REST Framework.

## Installation
1. Install the package using pip:

```bash
pip install drf-generic-views
```

2. Add `drf_generic_views` to `INSTALLED_APPS`
```python
INSTALLED_APPS = [
    ...,
    "drf_generic_views",
]
```

## Usage

### Mixins

#### MultiDestroyModelMixin

A mixin for multiple deletion of objects. It provides a `destroy` method that deletes all objects in the queryset individually.

It also provides a deletion hook `perform_destroy. It is called with the instance just before it should be deleted.

```python
def perform_destroy(self, instance):
    instance.delete()
```

#### BulkDestroyModelMixin

A mixin for bulk deletion of objects. It provides a `destroy` method that deletes all objects in the queryset with a bulk delete.

It also provides a deletion hook `perform_destroy`. It is called with the queryset just before all objects should be deleted.

```python
def perform_destroy(self, queryset):
    queryset.delete()
```

### Generic Views

#### BulkDestroyAPIView

A view for bulk deletion of objects. It deletes all objects in the queryset with a bulk delete.

```python
from drf_generic_views.generics import BulkDestroyAPIView

class MyBulkDestroyView(BulkDestroyAPIView):
    queryset = MyModel.objects.all()
```

#### ListDestroyAPIView

A view for deleting multiple objects individually from the queryset.

```python
from drf_generic_views.generics import ListDestroyAPIView

class MyListDestroyView(ListDestroyAPIView):
    queryset = MyModel.objects.all()
```

#### ListBulkDestroyAPIView

A view for both list and bulk deletion of objects.

```python
from rest_framework.generics import ListAPIView
from drf_generic_views.generics import ListBulkDestroyAPIView

class MyListBulkDestroyView(ListBulkDestroyAPIView):
    queryset = MyModel.objects.all()
```

--

## Contributing
Contributions are more than welcome! Please open an issue if you have any questions or suggestions.