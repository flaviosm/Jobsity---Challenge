# **Introduction**

When we needed to give our user a flexibility to integrate csv data ingestion to our cloud application, I had to find a stable and secure way to upload the files, keeping in mind create this kind of infrastructure to be managed on premises solutions, we have to prepare machine and also think about some other task to make it well. by AWS, we have a good opportunity to make it easy and separated as much as possible from our internal cloud environment.

AWS API Gateway binary support makes it possible to send requests with any content type. In order to make that possible the data is encoded in base64, so some manipulation is required before the data can be handled or stored for future use.

The ability to create an AWS Lambda function as an internal handler makes this manipulation and the integration of the requests with our cloud environment resources much easier also The AWS Serverless platform allows you to scale very quickly in response to demand. Below is an example of a serverless design that is fully synchronous throughout the application. During periods of extremely high demand, Amazon API Gateway and AWS Lambda will scale in response to your incoming load:

![servless](https://user-images.githubusercontent.com/25517708/219963217-a855b02c-98ff-4040-934b-5a7825b9ba65.jpg)
# **Architecture**

To promote this kind of integration, I had to setup the RDS instance such as My Sql, create the AWS Lambda function to integrate our binary data to My sql database and also the most importante of our integration is the **API Gateway endpoint** to send our trips.csv. Below the image of our integration for this project:

![image](https://user-images.githubusercontent.com/25517708/219961732-60c7acf5-6cd0-4366-90cb-60732ce3fd5d.png)







