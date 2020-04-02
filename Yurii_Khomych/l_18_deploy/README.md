### Project up to 13.04.2020
[Project ideas](http://www.markammay.com/100-creative-ideas-for-a-website/)
###Projects
1. [Currency aggregator](https://github.com/YuriiKhomych/currency-aggregator)
1. [Blog Django](https://github.com/YuriiKhomych/db2-python-django)
1. [News aggregator](https://github.com/YuriiKhomych/news-aggregator)
##Deploy
1. [Install Docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
1. [Install Docker-Compose](https://docs.docker.com/compose/install/)
1. [AWS](http://aws.amazon.com)
1. [GC](https://cloud.google.com)
1. [Flask blog api tutorial](https://github.com/olawalejarvis/blog_api_tutorial)
1. [AIOHTTP GRAPHQL](https://medium.com/@chimamireme/setting-up-a-modern-python-web-application-with-aiohttp-graphql-and-docker-149c52657142)
1. [Swagger](https://cloud.google.com)
1. [Flask deploy](https://github.com/YuriiKhomych/flask-deploy)
1. [Deployment](https://www.fullstackpython.com/deployment.html)
1. [Setting up a modern python web application with aiohttp, GraphQL and docker](https://medium.com/@chimamireme/setting-up-a-modern-python-web-application-with-aiohttp-graphql-and-docker-149c52657142)
1. [Deploy flask docker nginx](https://ianlondon.github.io/blog/deploy-flask-docker-nginx/)
1. [How to build a web application using Flask and deploy it to the cloud](https://www.freecodecamp.org/news/how-to-build-a-web-application-using-flask-and-deploy-it-to-the-cloud-3551c985e492/)
1. [How To Build and Deploy a Flask Application Using Docker on Ubuntu 18.04](https://www.digitalocean.com/community/tutorials/how-to-build-and-deploy-a-flask-application-using-docker-on-ubuntu-18-04)
1. [Deploying a Python Web App on AWS](https://towardsdatascience.com/deploying-a-python-web-app-on-aws-57ed772b2319)
1. [Flask APPLICATION](https://www.digitalocean.com/community/tutorials/how-to-build-and-deploy-a-flask-application-using-docker-on-ubuntu-18-04)
1. [FLASK APPLICATION TODO](https://www.youtube.com/playlist?list=PLlWXhlUMyooZr5R2u2Zwxt6Pw6iwBo5y5)
1. [Kubernetes](https://www.digitalocean.com/community/tutorials/how-to-build-and-deploy-a-flask-application-using-docker-on-ubuntu-18-04)

##FAQ on Interviews
###Python:
1. Data types
2. Mutable and immutable types
2. Hash
3. Python hashable types
4. How does dict and set works?
5. What object can be a key in dict?
6. Access speed by key in dict or set?
7. How can we define hashable object?
8. Are dictionaries ordered in version 3.6+?
9. List and tuple difference?
10. How does sets work?
11. str, list, dict, set methods examples
13. Collections
14. Standard libraries examples
15. PEP8
16. How can we make variable swap?
17. range and xrange difference
18. Context manager (class, function)
19. Iterators and Generators
20. yield
21. lambda functions
22. Closures (LEGB)
23. classmethod, staticmethod
24. underscores, dunders etc.
25. Decorators
26. Magic methods
27. Difference between `__getattr__` and `__getattribute__`
28. `async` and `await`
29. Multiprocessing and threading
30. Pros and cons of multiple inheritance
31. New style and old style classes
32. MRO
33. `__slots__`
34. How to create immutable class?
35. Shallow and deep copy.
36. Protocol descriptor.
37. Metaclasses
38. type()
39. ABC
40. Python 3 vs 2
41. weakref
42. memoryview
43. garbage collector
44. GIL
45. Modules location
46. wsgi
47. Authentication, Authorization, Identification

### SQL
1. Tables normalization and denormalization
2. Normal forms
3. Indexing
4. explain
5. table view
6. ACID
7. Transaction isolation levels
9. Joins

###HTTP and Services
1. HTTP
2. HTTP headers
3. DNS
4. HTTP request response
5. TCP vs UDP
6. IP
7. Ethernet
8. REST
9. REST vs RESTful
10. Docker
11. Kubernetes
12. Memcached
13. Redis
13. RabbitMQ
14. RabbitMQ Exchanges

### Patterns, algorithms and data structures
1. ORM patterns (Active record, Data mapper)
2. Graph algorithms
3. GRASP
4. Design Patterns
5. Algorithms and data structures
6. Functional programming vs OOP
7. Big O notation

#### Recommended tasks on leetcode:
1. [Task](https://leetcode.com/articles/reverse-integer/)
2. [Task](https://leetcode.com/articles/longest-common-prefix/)
3. [Task](https://leetcode.com/articles/remove-duplicates-from-sorted-array)
4. [Task](https://leetcode.com/articles/remove-element/)
5. [Task](https://leetcode.com/articles/range-sum-of-bst/)
6. [Task](https://leetcode.com/articles/unique-morse-code-words/)
7. [Task](https://leetcode.com/articles/big-countries/)
8. [Task](https://leetcode.com/articles/sort-array-by-parity/)
9. [Task](https://leetcode.com/articles/swap-salary/)
10. [Task](https://leetcode.com/articles/number-of-recent-calls/)
11. [Task](https://leetcode.com/articles/employee-bonus/)
12. [Task](https://leetcode.com/articles/duplicate-emails/)
13. [Task](https://leetcode.com/articles/duplicate-zeros/)
14. [Task](https://leetcode.com/articles/employee-importance/)
15. [Task](https://leetcode.com/articles/first-unique-character-in-a-string/)
16. [Task](https://leetcode.com/articles/binary-search/)

####Deploy app:
```
$ ls -a
$ sudo apt-get update
$ sudo apt-get upgrade 
$ git clone https://github.com/YuriiKhomych/aiohttp_blog.git
$ cd aiohttp_blog/
$ sudo apt install postgresql postgresql-contrib
$ psql
$ psql -U postgres
$ sudo -i -u postgres
$ sudo -u postgres psql
$ sudo apt-get install redis-server
$ systemctl service status postgres
$ systemctlstatus postgres
$ systemctl status postgres
$ systemctl status postgresql
$ systemctl status redis-server.service
$ ls
$ python
$ sudo apt install python3
$ python
$ python3
$ git checkout HEAD^
$ python -m pip install --user virtualenv
$ python -m pip3 install --user virtualenv
$ pip
$ sudo apt install python-pip
$ pip
$ python
$ python3
$ pip3
$ sudo apt install python3-pip
$ sudo pip3 install virtualenv 
$ virtualenv -p python3 myenv
$ ls
$ source myenv/bin/activate
$ pip install -r requirements.txt 
$ sudo apt-get install libpq-dev
$ pip install -r requirements.txt 
$ python
$ python run.py -c config/user_config.toml
$ python db_helpers.py -a
$ sudo -u postgres psql
$ python db_helpers.py -a
$ python run.py -c config/user_config.toml
$ systemctl stop postgresql
$ sudo systemctl stop postgresql
$ sudo systemctl stop redis-server.service 
$ sudo systemctl status redis-server.service 
$ sudo systemctl status redis
$ sudo systemctl status postgresql
$ sudo apt-get update
$ sudo apt-get install     apt-transport-https     ca-certificates     curl     gnupg-agent     software-properties-common
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
$ sudo apt-key fingerprint 0EBFCD88
$ sudo add-apt-repository    "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
$ sudo apt-get update
$ sudo apt-get install docker-ce docker-ce-cli containerd.io
$ sudo docker run hello-world
$ sudo curl -L "https://github.com/docker/compose/releases/download/1.25.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
$ sudo chmod +x /usr/local/bin/docker-compose
$ sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
$ docker-compose --version
$ docker-compose up --build
$ sudo docker-compose up --build
$ git checkout master
$ sudo docker-compose up --build
$ sudo docker-compose up
$ sudo docker-compose up -d
$ docker ps
$ sudo docker ps
$ sudo docker kill 609c2dc7204c
$ sudo docker ps
$ sudo docker-compose down
$ sudo docker-compose up
$ vim Dockerfile 
$ sudo docker-compose up --build
$ sudo docker-compose up --force-recreate
$ git pull
$ sudo docker-compose up --force-recreate
$ sudo docker-compose up 
$ sudo docker-compose up -d
$ docker ps
$ sudo docker ps
$ docker exec -it c7def34e2a43 bash
$ sudo docker exec -it c7def34e2a43 bash
$ history
```
