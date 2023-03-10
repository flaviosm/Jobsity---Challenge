# **Introduction**

When we needed to give our user a flexibility to integrate csv data ingestion to our cloud application, I had to find a stable and secure way to upload the files, keeping in mind create this kind of infrastructure to be managed on premises solutions, we have to prepare machine and also think about some other task to make it well. by AWS, we have a good opportunity to make it easy and separated as much as possible from our internal cloud environment.

AWS API Gateway binary support makes it possible to send requests with any content type. In order to make that possible the data is encoded in base64, so some manipulation is required before the data can be handled or stored for future use.

The ability to create an AWS Lambda function as an internal handler makes this manipulation and the integration of the requests with our cloud environment resources much easier also The AWS Serverless platform allows you to scale very quickly in response to demand. Below is an example of a serverless design that is fully synchronous throughout the application. During periods of extremely high demand, Amazon API Gateway and AWS Lambda will scale in response to your incoming load:

![servless](https://user-images.githubusercontent.com/25517708/219963217-a855b02c-98ff-4040-934b-5a7825b9ba65.jpg)
# **Architecture**

To promote this kind of integration, I had to setup the RDS instance such as My Sql, create the AWS Lambda function to integrate our binary data to My SQL database and also the most importante of our integration is the **API Gateway endpoint** to send our trips.csv. Below the image of our integration for this project:

![image](https://user-images.githubusercontent.com/25517708/219961732-60c7acf5-6cd0-4366-90cb-60732ce3fd5d.png)

# **Building request**

To make sure if our integration is working well, I created a postman post request to test it! available the file to import and make this tests on this project postman folder!

Endpoint: https://f9ge109rwk.execute-api.us-east-1.amazonaws.com/v1/upload

![PostmanRequest](https://user-images.githubusercontent.com/25517708/219967591-7ad449de-4f5b-4d5d-9b3a-c7245dc1dbe6.jpg)

As you can see after call the post request, I'm returning the status code and also the body of request if sucess or failure:

![image](https://user-images.githubusercontent.com/25517708/219968103-ca2b2f8a-7dfb-4787-9bec-051d38af267c.png)

# **Conclusion**

This kind of integration is powerfull when we need to recieve some files and persist it on our database instance to analyze some information and off course provide a fast way to integrate csv files.




