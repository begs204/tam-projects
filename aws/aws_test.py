import boto
s3 = boto.connect_s3()
buckets = s3.get_all_buckets()
bucket = buckets[1]
key = bucket.new_key('examples/index.html')
key.set_contents_from_filename('/Users/jason/Dropbox/Projects_Other/Python/theknot/index.html')
bucket.set_acl('public-read')
key.set_acl('public-read')
