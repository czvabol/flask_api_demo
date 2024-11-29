from flask_restful import Resource


class BackgroundResource(Resource):
    def __init__(self, **kwargs):
        if 'Container' not in kwargs:
            raise ValueError('Container not provided')

        self.Container = kwargs['Container']
        self.Logger = self.Container.Logger