def get_query_url(query):
    return 'http://php.net/manual/en/function.{}.php'.format(
        query.replace('_', '-')
    )
