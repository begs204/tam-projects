import boto
from boto.s3.connection import S3Connection
conn = S3Connection('AKIAIX2UHY2SA5IG3Q2A','eS+pJ76oxL2QZBIqJOhfFsJmiNVUWmdgwKowoomr')
buckets = conn.get_all_buckets()
print buckets

##works
# s3 = boto.connect_s3()
# buckets = s3.get_all_buckets()
# bucket = s3.get_bucket('meebo_partners')
# my_key = bucket.get_key("demos/code/jb_iframe.py")
# print my_key

#bucket = buckets[2]
#mb_key = bucket.lookup('test_demo')
#mb_key = bucket.keys()
#print mb_key



# keys = bucket.get_all_keys()
# print keys
# key  = keys[0]
# key.set_acl('public-read')



#key = bucket.new_key('examples/index.html')
#key.set_contents_from_filename('/Users/jason/Dropbox/Projects_Other/Python/theknot/index.html')
#bucket.set_acl('public-read')
#key.set_acl('public-read')
