from django.shortcuts import render
from django.http import JsonResponse  
from singletons.logger_singleton import LoggerSingleton  

def example_view(request):  
    logger = LoggerSingleton().get_logger()  
    logger.info("API initialized successfully.")  
    return JsonResponse({"message": "API endpoint accessed successfully!"}) 