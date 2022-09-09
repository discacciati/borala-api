class serializerByMethodMixin:
    def get_serializer_class(self):
        return self.serializer_map.get(self.request.method)
