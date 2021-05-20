# AWS app for image resizing

## lambda_func_image_resize.py contains image resize code 

## cognito_signup.py code is taking care of Cognito signup. 
In order to use image resize functionality, user has to be signed up with AWS Cognito service.
## lambda_confirm_email.py is taking care of user email confirmation process
Users email confirmation is supported by AWS Cognito Service

## lambda_func_add_picture.py is taking care of saving image attributes
DynamoDb Service is used

## lambda_func_add_picture.py is taking care of saving image attributes
DynamoDb Service is used

## lambda_func_get_all_pics.py is taking care of getting the list of all images from DynamoDb selected table
DynamoDb Service is used

## lambda_func_get_single_pic.py is taking care of getting a single image by the attribute from DynamoDb selected table
DynamoDb Service is used

## lambda_func_search_pictures.py is taking care of getting  images attribute collection from DynamoDb selected table
DynamoDb Service is used


