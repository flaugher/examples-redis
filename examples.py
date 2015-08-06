import redis

# Create and name server
r_server = redis.Redis("localhost")
r_server.set("name", "flaugher")
r_server.get("name")

# Convenience
svr = r_server

# Basic get/set/incr/decr operations
svr.set("counter", 1)
svr.incr("counter")
svr.get("counter")
svr.decr("counter")

# Lists
svr.rpush("members", "Adam")
svr.rpush("members", "Bob")
svr.rpush("members", "Carol")
svr.lrange("members", 0, -1)
svr.llen("members")
svr.lindex("members", 1)
svr.rpop("members")
svr.lrange("members", 0, -1)
svr.lpop("members")
svr.lrange("members", 0, -1)

# Sets
svr.delete("members")
svr.sadd("members", "Adam")
svr.sadd("members", "Bob")
svr.sadd("members", "Carol")
svr.sadd("members", "Adam")  # => 0 (False) since it's a set

# Use set to register "upvotes"
# Key has structure 'object_type:id:attribute'
# Value has structure 'object_type:id'
svr.sadd("story:5419:upvotes", "userid:9102")
svr.sadd("story:5419:upvotes", "userid:12981")
svr.sadd("story:5419:upvotes", "userid:1233")
svr.sadd("story:5419:upvotes", "userid:9102")  # => 0, already voted!
svr.scard("story:5419:upvotes")  # Cardinality, i.e. how many have voted?
svr.smembers("story:5419:upvotes")  # Who has voted?

# A sample command you might find in a Django view
if r_server.sadd("story:%s" % story_id, "userid:%s" % user_id):
    r_server.zincrby("stories:frontpage", "storyid:%s" % story_id, 1)
