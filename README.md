# News_article_sorting
In today’s world, data is power. With News companies having terabytes of data stored in
servers, everyone is in the quest to discover insights that add value to the organization.
With various examples to quote in which analytics is being used to drive actions, one that
stands out is news article classification.
Nowadays on the Internet there are a lot of sources that generate immense amounts of
daily news. In addition, the demand for information by users has been growing
continuously, so it is crucial that the news is classified to allow users to access the
information of interest quickly and effectively. This way, the machine learning model for
automated news classification could be used to identify topics of untracked news and/or
make individual suggestions based on the user’s prior interests.

## Table Content ✏️

 - Demo
 - Overview
 - Dataset
 - Installation
 - Deployment
 - Documentation
 - Directory Tree
 - Technology Used
 - Bug/Feature Request
 - Future scope of project  


## Demo ✔️
Heroku:- https://newbackorder.herokuapp.com/


AWS- Elastic Beanstalk:- http://backorder-env.eba-kr5v6w2h.us-east-1.elasticbeanstalk.com/ ("available for 4 hours only")

## Overview 📜
This Flask web app gives us the category of the data which you have provided to the model in the input text box in the application. Which eventually summarises and 
extract keen information and convert them into vectors and gives us the exact category it belongs to for example whether it may be finance, sports or business and 
so on.

## DataSet 📊

To Know more about data and its characterstics you can download dataset from https://www.kaggle.com/competitions/learn-ai-bbc/data

  
## Installation 🗄️

The Code is written in Python 3.9 If you don't have Python installed you can find it [here](https://www.python.org/downloads/). 
If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. 
To install the required packages and libraries, run this command in the project directory after 
[cloning](https://github.com/) the repository:
```bash
pip install -r requirements.txt
```

## Deployement
### Heroku
Login or signup in order to create virtual app. You can either connect your github profile or download ctl to manually deploy this project.
[![](https://i.imgur.com/dKmlpqX.png)](https://heroku.com)

Our next step would be to follow the instruction given on 
[Heroku Documentation](https://devcenter.heroku.com/articles/getting-started-with-python) to deploy a web app.

### AWS(Amazon Web Services)
Login or signup with free tier in order to create virtual amchine(Elastic beanstack) for free. 
Note:- In free trier virtual Machine will only give free service for 720hr almost a month after that you will be charged , so use carefully. 
I usally stop instance when it is not needed to avoid extra charge. so it may happen that deployment link for AWS might not work  
![](https://i.imgur.com/XMFtzYH.png)[![](https://i.imgur.com/cGvkZxw.png)](https://heroku.com)

Our next step would be to follow the instruction given on 
[AWS Elastic Beanstack](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html) to deploy a web app.


## DataBase

![App Screenshot](https://i.imgur.com/zYihnRR.jpg)
![App Screenshot](https://i.imgur.com/yWwLAWp.png)

## Directory Tree

```javascript
├── static 
│   |   |
│   |   ├── css
│   |   ├── forms
│   |   ├── img
│   |   ├── js
│   |   ├── vendor
├── template
│   ├── index.html
│   ├── result.html
│   ├── 500.html
│   ├── 404_error.html
|   ├── 405_error.html
│   ├── error.html
├── Procfile
|
├── README.md
├── application.py
├── gnb.pkl
├── requirements.txt


```
  
## Documentation

[Architecture](https://drive.google.com/file/d/1sp_UYlxHm4Y7CjXxX3dMEm6_S1iZLqOU/view)

[Low Level Documentation](https://drive.google.com/file/d/1U3bhMU0iuImoyYHYrDKhZgDD-jZjIDPe/view)

[High Level Documentation](https://drive.google.com/file/d/1toWy7ZtylAZRn3oogrnbs-5XjZ0faNoS/view)

[Wired Framed Diagram](https://drive.google.com/file/d/1yeH9xKe_6FZkwrdGG0fdJqesWSNoyrD4/view)

[DPR(Detail Documentation Report)](https://drive.google.com/file/d/174CdKcn_BNPgRClGy2V5FjrvcKF0hIAS/view)


## Technologies Used

![](https://forthebadge.com/images/badges/made-with-python.svg)

[<img target="_blank" src="https://flask.palletsprojects.com/en/1.1.x/_images/flask-logo.png" width=170>](https://flask.palletsprojects.com/en/1.1.x/) 
[<img target="_blank" src="https://blog.vizuri.com/hs-fs/hub/342946/file-2231290146-png/Images/Logos/Partners/Amazon_Web_Services/aws_s3_logo.png" width=280>]()
[<img target="_blank" src="https://i.imgur.com/3mZlVf8.jpg" width=280>]()
[<img target="_blank" src="https://seeklogo.com/images/B/bootstrap-logo-69A1CCC10B-seeklogo.com.png" width=200>](https://getbootstrap.com/) 



## Bug/Feature Request
If you find a bug (the website couldn't handle the query and / or gave undesired results), 
kindly open an [issue](https://github.com/) here by including your search query and the expected result


## Contributors <img src="https://raw.githubusercontent.com/TheDudeThatCode/TheDudeThatCode/master/Assets/Developer.gif" width=35 height=25>

- [Sravanthi Shoroff](https://github.com/sravanthishoroff)

## Future Scope

* Use unsupervised and compare the results with both supervised and unsupervised learnings.
* Optimize Flask application.py or create a streamlit app.
* Front-End 




