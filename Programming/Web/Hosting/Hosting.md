# Hosting
- Canonical Name (CNAME)
  - Maps one domain name to another
  - Stored in DNS
- Time To Live (TTL)
  - How long to cache query before resolving new one 
- Bucket
  - Basic containers that hold data
  - Access restriction 

# Static Hosting
- Websites which do not require backing server or special rendering engine 

TODO: summarise
https://olds.co/2018/static-hosting-on-gcp/

## Google Cloud Platform
### GCS + CNAME
Pros
Really fast and easy to set up
Supports both IPv4 and IPv6
Points directly at Google’s Global Network
No cost involved beyond standard GCS costs
Cons
No SSL support - This is the biggest gotcha people run into with this approach. You are unable to run your bucket with https
No redirect or rewrite logic - You are unable to create rules that redirect http traffic
Need new buckets for this - You can’t retroactively apply CNAMEs to buckets. The buckets must be created from the start with the domain name
Need to create buckets for both www.example.com and example.com if your usecase requires it and verify each domain manually
Not all DNS providers allow CNAME records to point to the apex record (example.com). Technically an A record must point to the root, but some providers provide a technique called CNAME flattening to allow this. For example Cloud DNS does not support this behavior
### GCS + Cloud Load Balancing (+ Cloud CDN)
This is probably the best, most scalable, most complicated, and most expensive option. Google Cloud’s L7 HTTP(S) load balancers are amazing, like literally. First off they’re global, like truly global. No need to launch an individual load balancer in each region. You can allocate IPv4 and IPv6 addresses to a load balancer which use Google’s premium backbone to make sure that IP address is always local to the user. It’s magic. What’s even more magical is you can also put a GCS Bucket behind one of these load balancers. And to top it all off, with a single click you can enable Cloud CDN for your load balancer. Sales pitch and drooling over, there is a base hourly fee for enabling this method usually clocking in around $18 / month for running one of these load balancers - which for a business should be fine, but not really for the hobbyist.

Pros
You can also run dynamic content off another path - ie have /static pointed to your bucket and /api pointed to a GCE Managed Instance Group running your API. Take note that the load balancers do not rewrite paths when talking to the bucket, if you’re requesting /static/a.jpg you’ll need to make sure /static/a.jpg exists in your bucket too
You can allocate both IPv4 and IPv6 addresses to your load balancer
You can run SSL off your load balancer
Seamless integration with Cloud CDN. Note: I recommend if you employ L7LB + Cloud CDN that you only use a Regional Bucket vs Multi-Regional bucket, you’ll tend to get better performance this way.
Works with existing buckets!
Cons
Managed SSL Certificates are now supported! No managed SSL Certificate support, you must bring your own certificates. You can still use free certificate providers such as Let’s Encrypt for this purpose!
Arguably complicated to get set up (But no issues once it’s running!)
### GCS + CDN Provider
I know the least about this method as I do not generally work with third party CDNs like Fastly. It has similar benefits to the first option with CNAME but adds the possibility of adding SSL.

Pros
Works with existing buckets
Because it can point to yourbucket.storage.googleapis.com you do not have to verify the domain name and allows SSL end to end via https://yourbucket.storage.googleapis.com
Having a CDN is always a good idea to lower storage costs and increase end user performance
Cons
Some CDN providers may also allocate a CNAME record to bind to which brings up root record concerns as outlined above
IPv6 support might not exist
Unknown costs when dealing with third parties
### Firebase Hosting
Firebase Hosting fills in a lot of the gaps that the GCS + CNAME route presents. You get the power of redirects, rewriting, custom domains, free SSL, and a CDN. Firebase projects can tie in directly to a GCP project and can link billing methods. This blog, for example, is hosted with Firebase Hosting. This route is generally the official Google recommendation when GCS + CNAME doesn’t cut it.

Pros
firebase deploy - does it get easier than that?
Free SSL
Redirects, Rewrites, and Headers - Oh my!
Verifying a domain in Firebase Hosting is much more straightforward than in GCS
Cons
No IPv6 support
All content is overwritten each deploy, with buckets your bucket could be massive, Firebase Hosting is definitely for the “smaller” sites.
### Honorary Mention - App Engine Standard
App Engine Standard is another among the “serverless” tools that’s magical. It supports the ability to host static files that do not get passed through your chosen environment (ie Python).

Pros
Controlled scaling - All the above options will scale infinitely without regards to your wallet. App Engine Standard can absolutely scale infinitely as well but it gives you the choice on how much you’re willing to spend to get there.
Abuse Controls - Similar to scaling controls App Engine gives you the ability to block malicious IPs that may be attempting to send too much traffic
A/B Testing - Using App Engines powerful Traffic Splitting tools you can run multiple static sites at the same time at the same host to conduct various A/B tests.
Free SSL! App Engine supports managed certificates or bring your own
Built-in caching
Cons
App Engine also only provides a CNAME record (ghs.googlehosted.com)
If not configured correctly you may incur hourly charges for your site
All content is overwritten each deploy
# Dynamic Hosting