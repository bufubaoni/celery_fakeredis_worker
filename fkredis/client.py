from fakeredis import FakeStrictRedis


class FkRedisClient(FakeStrictRedis):

    def info(self):
        return "info fk redis"
