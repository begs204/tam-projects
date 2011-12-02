import base64
import hmac, hashlib, urllib

policy_document = 'policy.txt'
pd= open(policy_document,'rU').read()
pd1 = pd.replace('\n','').replace(' ','').replace('\r','')
policy = base64.b64encode(pd1)
print policy
#print urllib.urlencode({'Policy':policy})

aws_secret_key = 'eS+pJ76oxL2QZBIqJOhfFsJmiNVUWmdgwKowoomr'
signature = base64.b64encode(hmac.new(aws_secret_key, policy, hashlib.sha1).digest())
#print base64.b64decode(signature)
print signature
#print urllib.urlencode({'Signature': signature})
