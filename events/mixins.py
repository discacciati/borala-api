class FilterByQueryParamsMixin:
    def get_query_options(self, query_params, lookup_dict = {}):
        for param in query_params.keys():
            if not self.querystring_map[param]:
                continue
            
            lookup = self.querystring_map[param]

            lookup_dict[lookup] = query_params[param]

        return lookup_dict

    def get_queryset(self):
        model        = self.get_serializer_class().Meta.model
        query_params = self.request.query_params
        queryset     = model.objects.all()

        if len(query_params.keys()) > 0:
            lookup_dict = self.get_query_options(query_params)
            queryset    = model.objects.filter(**lookup_dict)
            
        return queryset
